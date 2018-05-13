# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

import tkinter

main_window = tkinter.Tk()

main_window.title("Calculator Demo")
main_window.geometry("240x320+8+200")
main_window.wm_minsize(240, 320)
main_window["padx"] = 8
main_window["pady"] = 8

row_weights = [1, 1, 1, 1, 1, 1]
column_weights = [1, 1, 1, 1]

# Grid definition
for i in range(6):
    main_window.rowconfigure(i, weight=row_weights[i])

for j in range(4):
    main_window.columnconfigure(j, weight=column_weights[j])


# Frame for result
result_frame = tkinter.Frame(main_window)
result_frame.grid(row=0, column=0, columnspan=4, sticky="nsew")
result_frame.config(border=3, relief="sunken")

# Result
result = tkinter.Entry(main_window)
result.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Buttons
button_list = [("C", 1, 0, 1), ("CE", 1, 1, 1),
               ("7", 2, 0, 1), ("8", 2, 1, 1), ("9", 2, 2, 1), ("+", 2, 3, 1),
               ("4", 3, 0, 1), ("5", 3, 1, 1), ("6", 3, 2, 1), ("-", 3, 3, 1),
               ("1", 4, 0, 1), ("2", 4, 1, 1), ("3", 4, 2, 1), ("*", 4, 3, 1),
               ("0", 5, 0, 1), ("=", 5, 1, 2), ("/", 5, 3, 1)]

for b in button_list:
    for i in range(len(button_list)):
        n, r, c, s = button_list[i]
        n = tkinter.Button(main_window, text=n)
        n.grid(row=r, column=c, columnspan=s, sticky="nsew")

# Verbose version of button generation
# button_C = tkinter.Button(main_window, text="C")
# button_C.grid(row=1, column=0, sticky="nsew")
# button_CE = tkinter.Button(main_window, text="CE")
# button_CE.grid(row=1, column=1, sticky="nsew")
#
# button_7 = tkinter.Button(main_window, text="7")
# button_7.grid(row=2, column=0, sticky="nsew")
# button_8 = tkinter.Button(main_window, text="8")
# button_8.grid(row=2, column=1, sticky="nsew")
# button_9 = tkinter.Button(main_window, text="9")
# button_9.grid(row=2, column=2, sticky="nsew")
# button_plus = tkinter.Button(main_window, text="+")
# button_plus.grid(row=2, column=3, sticky="nsew")
#
# button_4 = tkinter.Button(main_window, text="4")
# button_4.grid(row=3, column=0, sticky="nsew")
# button_5 = tkinter.Button(main_window, text="5")
# button_5.grid(row=3, column=1, sticky="nsew")
# button_6 = tkinter.Button(main_window, text="6")
# button_6.grid(row=3, column=2, sticky="nsew")
# button_minus = tkinter.Button(main_window, text="-")
# button_minus.grid(row=3, column=3, sticky="nsew")
#
# button_1 = tkinter.Button(main_window, text="1")
# button_1.grid(row=4, column=0, sticky="nsew")
# button_2 = tkinter.Button(main_window, text="2")
# button_2.grid(row=4, column=1, sticky="nsew")
# button_3 = tkinter.Button(main_window, text="3")
# button_3.grid(row=4, column=2, sticky="nsew")
# button_multiply = tkinter.Button(main_window, text="*")
# button_multiply.grid(row=4, column=3, sticky="nsew")
#
# button_0 = tkinter.Button(main_window, text="0")
# button_0.grid(row=5, column=0, sticky="nsew")
# button_equals = tkinter.Button(main_window, text="=")
# button_equals.grid(row=5, column=1, columnspan=2, sticky="nsew")
# button_divide = tkinter.Button(main_window, text="/")
# button_divide.grid(row=5, column=3, sticky="nsew")

main_window.mainloop()
