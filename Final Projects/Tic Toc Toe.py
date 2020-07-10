# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 19:25:39 2020

@author: Sourick
"""

from tkinter import *
from tkinter import messagebox
import tkinter.font as font

top = Tk()
top.title("Simple Sudoku Game")
top.geometry("290x270")
top.resizable(0,0)

top.withdraw()

def key(event):
    print("hello")


p1 = simpledialog.askstring("Simple Tik Tac Tue Game", "Player 1 Choice (Only press X or O :")
p2 = simpledialog.askstring("Simple Tik Tac Tue Game", "Player 2 Choice (Only press X or O :")

top.deiconify()
players  = "Player 1 : " + p1 + "\n" + "Player 2 : " + p2

top.config(bg = "yellow")

myfont = font.Font(size=15)


#One Box
text1 = Entry(top,width = "7")
text1.place(x = 20, y = 30,height = "40") 
text1['font'] = myfont

#
text2 = Entry(top,width = "7")
text2.place(x = 110, y = 30,height = "40")
text2['font'] = myfont

text3 = Entry(top,width = "7")
text3.place(x = 200, y = 30,height = "40")
text3['font'] = myfont

text4 = Entry(top,width = "7")
text4.place(x = 20, y = 80,height = "40")
text4['font'] = myfont

text5 = Entry(top,width = "7")
text5.place(x = 110, y = 80,height = "40")
text5['font'] = myfont

text6 = Entry(top,width = "7")
text6.place(x = 200, y = 80,height = "40")
text6['font'] = myfont

text7 = Entry(top,width = "7")
text7.place(x = 20, y = 130,height = "40")
text7['font'] = myfont

text8 = Entry(top,width = "7")
text8.place(x = 110, y = 130,height = "40")
text8['font'] = myfont

text9 = Entry(top,width = "7")
text9.place(x = 200, y = 130,height = "40")
text9['font'] = myfont

label1 = Label(top,text = players,bg = "black", fg = "light green")
label1.place(x = 20, y = 180,height = "40")

text1.bind_all('<Key>', key)
text2.bind_all('<Key>', key)
text3.bind_all('<Key>', key)
text4.bind_all('<Key>', key)
text5.bind_all('<Key>', key)
text6.bind_all('<Key>', key)
text7.bind_all('<Key>', key)
text8.bind_all('<Key>', key)
text9.bind_all('<Key>', key)

top.mainloop()





