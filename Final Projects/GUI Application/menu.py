# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 13:26:13 2020

@author: Sourick
"""

def run1():
    os.startfile('signup.py')
   
def run2():
    os.startfile('signin.py')
    
import os
from tkinter import *
top = Tk()
top.geometry("200x100")
top.title("Menu")
top.config(bg = "pink")
submit = Button(text = "Submit",bg = "green",fg = "white",width = "8",command=run1).place(x = 25, y = 20)
reset = Button(text = "Reset",bg = "blue",fg = "white",width = "8",command=run2).place(x = 105, y = 20)

top.mainloop()

