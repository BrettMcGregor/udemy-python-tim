import tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
#
# tkinter._test()

main_window = tkinter.Tk()

main_window.title("Country Destroyer")
main_window.geometry("640x480")

label = tkinter.Label(main_window, text="Choose a country to destroy.\n(Important: Cannot be undone)")
label.pack(side="top")

left_frame = tkinter.Frame(main_window)
left_frame.pack(side="left", anchor="n", fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(left_frame, relief="raised", borderwidth=1)
canvas.pack(side="left", anchor="n")

right_frame = tkinter.Frame(main_window)
right_frame.pack(side="right", anchor="n", expand=True)

button1 = tkinter.Button(right_frame, text="Iran")
button2 = tkinter.Button(right_frame, text="Russia")
button3 = tkinter.Button(right_frame, text="Syria")
button4 = tkinter.Button(right_frame, text="North Korea")
button1.pack(side="top")
button2.pack(side="top")
button3.pack(side="top")
button4.pack(side="top")

main_window.mainloop()
