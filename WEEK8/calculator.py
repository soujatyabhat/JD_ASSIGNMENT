# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 07:36:59 2020

@author: Sourick
"""

from tkinter import *
Top = Tk()
select = ' '
Top.title("Calculator")
Top.geometry("300x250")
Top['bg'] = "yellow"
label1 = Label(Top,text = "Enter first number : ", bg = "yellow", fg = "blue")
label1.place(x = 20, y = 30)
txt1 = Entry(Top)
txt1.place(x = 150, y = 30)

label2 = Label(Top,text = "Enter second number : ", bg = "yellow", fg = "blue")
label2.place(x = 20, y = 70)
txt2 = Entry(Top)
txt2.place(x = 150, y = 70)
radio = StringVar()
radio.set(' ')
val = IntVar()
def selection():
    global select
    select = radio.get()
    print(select)
    
def action():
    result = 0
    value1 = int(txt1.get())
    value2 = int(txt2.get())
    if select == '+':
        result = value1 + value2
    elif select == '-':
        result = value1 - value2
    elif select == "*":
        result = value1 * value2
    elif select == "/":
        result = value1 // value2
        
    label3.configure(text= "Result : " + str(result))
    
def clean():
    Top.destroy()
    
r1 = Radiobutton(Top,text = "+", value = '+' ,variable = radio, command = selection,state=NORMAL,bg = "yellow")
r1.place(x = 40 , y = 120)
r2 = Radiobutton(Top,text = "-", value = '-' , variable = radio,command = selection,state=NORMAL,bg = "yellow")
r2.place(x = 100 , y = 120)
r3 = Radiobutton(Top,text = "*", value = '*',variable = radio, command = selection,state=NORMAL,bg = "yellow")
r3.place(x = 160 , y = 120)
r4 = Radiobutton(Top,text = "/", value = '/',variable = radio, command = selection,state=NORMAL,bg = "yellow")
r4.place(x = 220 , y = 120)
button1  = Button(Top,text = "Calculate", command = action, width = "10")
button1.place(x = 40, y = 160)
button2  = Button(Top,text = "Exit", command = clean, width = "10")
button2.place(x = 160, y = 160)
label3 = Label(Top,text = "Result : ", fg = "red", width = "30")
label3.place(x = 40, y = 200)
Top.mainloop()


