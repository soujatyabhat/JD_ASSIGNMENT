# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 23:37:50 2020

@author: Sourick
"""
from tkinter import *
top = Tk()
top.title("Tic Toc Toe")
top['bg'] = 'green'
top.geometry("200x200")
label2 = Label(top, text = "Simple Tic Tac Toe Game").place(x = 30, y = 9)
text1 = Entry(top , width = "8").place(x = 10, y = 40)
text2 = Entry(top , width = "8").place(x = 70, y = 40)
text3 = Entry(top , width = "8").place(x = 130, y = 40)

text1 = Entry(top , width = "8").place(x = 10, y = 70)
text2 = Entry(top , width = "8").place(x = 70, y = 70)
text3 = Entry(top , width = "8").place(x = 130, y = 70)

text1 = Entry(top , width = "8").place(x = 10, y = 100)
text2 = Entry(top , width = "8").place(x = 70, y = 100)
text3 = Entry(top , width = "8").place(x = 130, y = 100)

label3 = Label(top, text = "Player 1 is Win",fg = "blue",bg = "black", width = "24").place(x = 10, y = 130)
label4 = Label(top, text = "Player 1 is : X \n Player is : 0",fg = "yellow",bg = "black", width = "14",height = "2").place(x = 10, y = 160)
button1 = Button(top, text = "Reset", bg = "red", fg = "white",width = "8",height = "2").place(x = 120, y = 160)
top.mainloop()

