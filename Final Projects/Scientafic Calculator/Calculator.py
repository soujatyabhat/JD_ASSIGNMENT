# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:38:58 2020

@author: Sourick
"""

import math
from tkinter import *
top = Tk()
top.minsize(670,300)
top.title("Simple Calculator")
top.resizable(0,0)
top.wm_iconbitmap("cal.ico")
top.config(bg = "gray")

def click(event):
    global screen
    text = event.widget.cget("text")
    if text == '=':
        try:
            screen.set(eval(screen.get()))
        except:
            screen.set("Error")
            print("error")
            
    elif text == 'Clear':
        screen.set(" ")
    
    elif text == 'Backspace':
            new_string = ' '
            get_data = str(screen.get())
            count = len(get_data)
            for i in range(0,(count - 1)):
                new_string += get_data[i] 
           
            screen.set(new_string)
            print(new_string)
            new_string = ' '
       
    elif text == 'Sin':
         add_value = float(screen.get())
         screen.set(math.sin(add_value))
         
    elif text == 'Cos':
         add_value = float(screen.get())
         screen.set(math.sin(add_value))

    elif text == 'Tan':
         add_value = float(screen.get())
         screen.set(math.tan(add_value))
         
    elif text == 'Sqrt':
         add_value = int(screen.get())
         screen.set(math.sqrt(add_value))    
         
    elif text == 'Factorial':
          add_value = int(screen.get())
          screen.set(math.factorial(add_value))
         
    elif text == 'Power':
         value = screen.get()
         lenth = len(value)
         if lenth > 2:
             screen.set(" ")
             screen.set("Error")
         else:
             value = int(value)
             n = (value % 10)
             x = (value // 10)
             print(x)
             screen.set(int(math.pow(x,n)))
    else:
        screen.set(screen.get() + text)
        text1.update()
        

screen = StringVar()

text1 = Entry(top,text = "ii",textvariable = screen,font = "DS-Digital 30 bold",justify = RIGHT)
text1.pack(fill='x',padx = "10",pady = "20")

#Row 1

frame1 = Frame(top,bg = "silver")
button01 = Button(top,text = "7",pady = "3",padx = "30",bg = "cyan")
button01.place(x = 30,y = 100)
button01.bind("<Button-1>",click)

button02 = Button(top,text = "8",pady = "3",padx = "30",bg = "cyan")
button02.place(x = 110,y = 100)
button02.bind("<Button-1>",click)

button03 = Button(top,text = "9",pady = "3",padx = "30",bg = "cyan")
button03.place(x = 190,y = 100)
button03.bind("<Button-1>",click)

button04 = Button(top,text = "+",pady = "3",padx = "20",bg= "pink")
button04.place(x = 280,y = 100)
button04.bind("<Button-1>",click)

button05 = Button(top,text = "-",pady = "3",padx = "20",bg= "pink")
button05.place(x = 340,y = 100)
button05.bind("<Button-1>",click)

button06 = Button(top,text = "Sin",pady = "3",padx = "20", bg= "yellow")
button06.place(x = 420,y = 130)
button06.bind("<Button-1>",click)


button07 = Button(top,text = "Cos",pady = "3",padx = "20", bg= "yellow")
button07.place(x = 490,y = 130)
button07.bind("<Button-1>",click)


button08 = Button(top,text = "Tan",pady = "3",padx = "20", bg= "yellow")
button08.place(x = 565,y = 130)
button08.bind("<Button-1>",click)

frame1.pack()


#Row 2

frame2 = Frame(top,bg = "silver")
button11 = Button(top,text = "4",pady = "3",padx = "30",bg = "cyan")
button11.place(x = 30,y = 150)
button11.bind("<Button-1>",click)

button12 = Button(top,text = "5",pady = "3",padx = "30",bg = "cyan")
button12.place(x = 110,y = 150)
button12.bind("<Button-1>",click)

button13 = Button(top,text = "6",pady = "3",padx = "30",bg = "cyan")
button13.place(x = 190,y = 150)
button13.bind("<Button-1>",click)

button14 = Button(top,text = "*",pady = "3",padx = "20",bg= "pink")
button14.place(x = 280,y = 150)
button14.bind("<Button-1>",click)

button15 = Button(top,text = "//",pady = "3",padx = "20",bg= "pink")
button15.place(x = 340,y = 150)
button15.bind("<Button-1>",click)

button16 = Button(top,text = "Sqrt",pady = "3",padx = "18", bg= "yellow")
button16.place(x = 420,y = 165)
button16.bind("<Button-1>",click)


button17 = Button(top,text = "Power",pady = "3",padx = "13", bg= "yellow")
button17.place(x = 492,y = 165)
button17.bind("<Button-1>",click)


button18 = Button(top,text = "Factorial",pady = "3",padx = "7", bg= "yellow")
button18.place(x = 565,y = 165)
button18.bind("<Button-1>",click)


frame2.pack()

#Row 3

frame3 = Frame(top,bg = "silver")

button9 = Button(top,text = "1",pady = "3",padx = "30",bg = "cyan")
button9.place(x = 30,y = 200)
button9.bind("<Button-1>",click)

button10 = Button(top,text = "2",pady = "3",padx = "30",bg = "cyan")
button10.place(x = 110,y = 200)
button10.bind("<Button-1>",click)

button11 = Button(top,text = "3",pady = "3",padx = "30",bg = "cyan")
button11.place(x = 190,y = 200)
button11.bind("<Button-1>",click)

button12 = Button(top,text = "=",pady = "3",padx = "50",bg= "lightgreen")
button12.place(x = 280,y = 200)
button12.bind("<Button-1>",click)

frame3.pack()

#Row 4
frame4 = Frame(top,bg = "silver")
button13 = Button(top,text = "0",pady = "3",padx = "70",bg = "cyan")
button13.place(x = 30,y = 245)
button13.bind("<Button-1>",click)

button14 = Button(top,text = "Clear",pady = "3",padx = "20",bg= "red")
button14.place(x = 190,y = 245)
button14.bind("<Button-1>",click)

button15 = Button(top,text = "Backspace",pady = "3",padx = "28",bg= "orange")
button15.place(x = 280,y = 245)
button15.bind("<Button-1>",click)

frame4.pack()

top.mainloop()