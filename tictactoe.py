'''
created on mon dec 24 04:41:36 2018

author: atnip
'''

from tkinter import *
from tkinter import messagebox
#the window
tk = Tk()
tk.title("tic tac toe")

grid = []

#x and o turns
click = True

def turn(row_idx, col_idx):
    def wrapper():
        global click
        button = grid[row_idx][col_idx]
        if button["text"] == " " and click == True:
            button["text"] = "X"
            click = False
        elif button["text"] == " " and click == False:
            button["text"] = "0"
            click = True
    return wrapper

#button locations
row_num = 3
col_num = 3
for row_idx in range(row_num):
    row = []
    for col_idx in range(col_num):
        button = Button(tk,text=" ",font=('Times 26 bold'), height = 4,
        width = 8, command =  turn(row_idx, col_idx))
        button.grid(row = row_idx, column = col_idx,sticky = S+N+E+W)
        row.append(button)
    grid.append(row)
#win conditions
    # players = ["X", "0"]
    # for p in players:
    #     if(button1["text"] == p and button2["text"] == p and button3["text"] == p or
    #         button6["text"] == p and button5["text"] == p and button4["text"] == p or
    #         button7["text"] == p and button8["text"] == p and button9["text"] == p or
    #         button1["text"] == p and button4["text"] == p and button7["text"] == p or
    #         button2["text"] == p and button5["text"] == p and button8["text"] == p or
    #         button3["text"] == p and button6["text"] == p and button9["text"] == p or
    #         button1["text"] == p and button5["text"] == p and button9["text"] == p or
    #         button3["text"] == p and button5["text"] == p and button7["text"] == p):
    #         messagebox.showinfo("winner","player {} wins".format(p))
        
'''
#lines
w = Canvas(tk, width=200, height=225)
w.pack()

w.create_line(65, 0, 65, 225)
w.create_line(135, 0, 135, 225)
w.create_line(0, 65, 200000, 400)
w.create_line(0, 150, 200000, 400)
'''

'''button1 = Button(tk,text=" ",font=('Times 26 bold'), height = 4,
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

button5 = Button(tk,font=('Times 26 bold'),text=" ", height = 4,
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

button9.grid(row=2, column=2,sticky = S+N+E+W)'''

tk.mainloop()