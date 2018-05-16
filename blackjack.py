import random
import tkinter


def load_images(card_images):
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]
    extension = "png"
    for pack in range(3):  # add extra packs of cards
        for suit in suits:
            for card in range(1, 11):
                name = "cards/{}_{}.{}".format(str(card), suit, extension)
                image = tkinter.PhotoImage(file=name)
                card_images.append((card, image))
            for card in face_cards:
                name = "cards/{}_{}.{}".format(str(card), suit, extension)
                image = tkinter.PhotoImage(file=name)
                card_images.append((10, image))


def _deal_card(frame):
    # pop the next card off the top of the deck
    next_card = deck.pop(0)
    # add the card to the back of the pack
    deck.append(next_card)
    # add the image to a label and display the label
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    return next_card


def score_hand(hand):
    # calculate the total score of all cards in the list/hand
    # only one ace can have the value 11, and this will be reduced to 1 if the hand would bust.
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we would bust, check if there is an ace and subtract 10 if there is.
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
    else:
        result_text.set("It's a draw!")


def deal_player():
    player_hand.append(_deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")

    # the following code was replaced as it was aimed at learning about global and local variables
    # global player_score
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += card_value
    # # if we would bust, check if there is an ace and subtract
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer wins!")

# Challenge:
# to add a new button to the program with the text new game now the button should call a function
# that clears the cards from the screen it resets the players and dealers hands and then starts
# a new game now the easiest way to clear the contents of a frame is to destroy the frame and
# create a new one with the same name and in fact that's why the program has a player_card_frame
# and dealer_card_frame inside the card frame itself so that's it go away and create a new button
# with the text new game and again the functionality clear the cards from the Screen reset the player
# and dealers hands and then start a new game


def initial_deal():
    # initialise game by dealing first cards
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand

    # destroy card frames
    dealer_card_frame.destroy()
    player_card_frame.destroy()

    # re-create card frames for new game
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    # clear the dealer and players hands for new game
    dealer_hand = []
    player_hand = []
    initial_deal()

    # clear the result text from previous game
    result_text.set("")


def shuffle():
    random.shuffle(deck)


# start game when called from external program
def play():
    # initialise game by dealing first cards
    initial_deal()

    tkinter.mainloop()


# set up the screen and frames for the dealer and player
main_window = tkinter.Tk()
main_window.title("Black Jack")
main_window.geometry("640x480")
main_window.configure(background="green")

result_text = tkinter.StringVar()
result = tkinter.Label(main_window, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(main_window, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# embedded from to hold the player card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

button_frame = tkinter.Frame(main_window)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=2)

shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=3)
# Load cards
cards = []
load_images(cards)

# Create a new deck of cards and shuffle them
deck = list(cards)
shuffle()

# Create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

# run program if this file executed
if __name__ == "__main__":
    play()
