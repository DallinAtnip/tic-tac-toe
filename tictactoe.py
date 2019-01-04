'''
created on mon dec 24 04:41:36 2018

author: atnip
'''

from tkinter import *
import tkinter.messagebox

#the window
tk = Tk()
tk.title("tic tac toe")
#tk.geometry("200x225")

click = True

def turn(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "0"
        click = True

    elif(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
        button6["text"] == "X" and button5["text"] == "X" and button4["text"] == "X" or
        button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
        button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
        button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
        button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
        tkinter.messagebox.showinfo("Player X Wins!")
        quit

    elif(button1["text"] == "0" and button2["text"] == "0" and button3["text"] == "0" or
        button6["text"] == "0" and button5["text"] == "0" and button4["text"] == "0" or
        button7["text"] == "0" and button8["text"] == "0" and button9["text"] == "0" or
        button1["text"] == "0" and button4["text"] == "0" and button7["text"] == "0" or
        button2["text"] == "0" and button5["text"] == "0" and button8["text"] == "0" or
        button3["text"] == "0" and button6["text"] == "0" and button9["text"] == "0" or
        button1["text"] == "0" and button5["text"] == "0" and button9["text"] == "0" or
        button3["text"] == "0" and button5["text"] == "0" and button7["text"] == "0"):
        tkinter.messagebox.showinfo("Player 0 Wins!")
        quit

'''
#lines
w = Canvas(tk, width=200, height=225)
w.pack()

w.create_line(65, 0, 65, 225)
w.create_line(135, 0, 135, 225)
w.create_line(0, 65, 200000, 400)
w.create_line(0, 150, 200000, 400)
'''
#buttons
buttons=StringVar()

button1 = Button(tk,text=" ",font=('Times 26 bold'), height = 4,
width = 8, command=lambda:turn(button1))

button1.grid(row=0, column=0,sticky = S+N+E+W)

button2 = Button(tk,text=" ",font=('Times 26 bold'), height = 4,
width = 8, command=lambda:turn(button2))

button2.grid(row=0, column=1,sticky = S+N+E+W)

button3 = Button(tk,text=" ",font=('Times 26 bold'), height = 4,
width = 8, command=lambda:turn(button3))

button3.grid(row=0, column=2,sticky = S+N+E+W)

button4 = Button(tk,text=" ",font=('Times 26 bold'), height = 4,
width = 8, command=lambda:turn(button4))

button4.grid(row=1, column=0,sticky = S+N+E+W)

button5 = Button(tk,text=" ",font=('Times 26 bold'), height = 4,
width = 8, command=lambda:turn(button5))

button5.grid(row=1, column=1,sticky = S+N+E+W)

button6 = Button(tk,text=" ",font=('Times 26 bold'), height = 4,
width = 8, command=lambda:turn(button6))

button6.grid(row=1, column=2,sticky = S+N+E+W)

button7 = Button(tk,text=" ",font=('Times 26 bold'), height = 4,
width = 8, command=lambda:turn(button7))

button7.grid(row=2, column=0,sticky = S+N+E+W)

button8 = Button(tk,text=" ",font=('Times 26 bold'), height = 4,
width = 8, command=lambda:turn(button8))

button8.grid(row=2, column=1,sticky = S+N+E+W)

button9 = Button(tk,text=" ",font=('Times 26 bold'), height = 4,
width = 8, command=lambda:turn(button9))

button9.grid(row=2, column=2,sticky = S+N+E+W)

#loop
tk.mainloop()



