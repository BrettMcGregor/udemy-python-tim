# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

mystring = "ANZAC day with the family, Brisbane, 2018"
text = set(mystring)
vowels = {"a", "e", "i", "o", "u"}

no_vowels = text.difference(vowels)
print(sorted(no_vowels))

no_vowels2 = []
for char in mystring:
    if char in vowels:
        continue
    else:
        no_vowels2.append(char)

print(sorted(no_vowels2))
