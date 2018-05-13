# this uses the grid configuration

import tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
#
# tkinter._test()

main_window = tkinter.Tk()

main_window.title("Country Destroyer")
main_window.geometry("640x480+8+200")

label = tkinter.Label(main_window, text="Choose a country to destroy.\n(Important: Cannot be undone)")
label.grid(row=0, column=0)

left_frame = tkinter.Frame(main_window)
left_frame.grid(row=1, column=1)

canvas = tkinter.Canvas(left_frame, relief="raised", borderwidth=1)
canvas.grid(row=1, column=0)

right_frame = tkinter.Frame(main_window)
right_frame.grid(row=1, column=2, sticky="n")

button1 = tkinter.Button(right_frame, text="Iran")
button2 = tkinter.Button(right_frame, text="Russia")
button3 = tkinter.Button(right_frame, text="Syria")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)


# configure columns

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.grid_columnconfigure(2, weight=1)

left_frame.config(relief="sunken", borderwidth=1)
right_frame.config(relief="sunken", borderwidth=1)
left_frame.grid(sticky="ns")
right_frame.grid(sticky="new")

right_frame.columnconfigure(0, weight=1)
button1.grid(sticky="ew")
button2.grid(sticky="ew")
button3.grid(sticky="ew")
main_window.mainloop()
