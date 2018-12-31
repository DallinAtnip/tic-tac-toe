from tkinter import *

#the window
root = Tk()

#root window details
root.title("tic tac toe")
root.geometry("200x225")

#lines
w = Canvas(root, width=200, height=225)
w.pack()

w.create_line(65, 0, 65, 225)
w.create_line(135, 0, 135, 225)
w.create_line(0, 65, 200000, 400)
w.create_line(0, 150, 200000, 400)

#loop
root.mainloop()