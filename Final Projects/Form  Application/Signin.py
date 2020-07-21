# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 12:45:38 2020

@author: Sourick
"""

from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("230x160")
top.resizable(0,0)
top.title("Signin")
top.config(bg = "cyan")

a = ' '
flag1 = 0
fpt = ''
def opn():
    global fpt
    fpt = open("record.txt","r")

def reset():
    email.delete(0, END)
    password.delete(0, END)
    
def check(a):
    global new_list
    new_list = list(a.split(' '))
    email_check = new_list.count(email.get())
    password_check = new_list.count(password.get())
    if email_check > 0 and password_check > 0:
        return True
    else:
        return False
    
def add():  
    opn()
    global fpt,flag1,new_list,a
    for line in fpt:
        a = line
        flag = check(a)
        if flag == True:
            flag1 = 1
            break
    if flag1 == 1:
         messagebox.showinfo("Conglatunation","Welcome to our portal")
         messagebox.showinfo("Information","Please goto the user_details application")
         file = open("about.txt","w")
         file.write(a)
         file.close()
         top.destroy()
    else:
         messagebox.showerror("Failure","Password or Email has not matched")
         password.delete(0, END)
    fpt.close()   
            
    
label1 = Label(top,text = "Email ID : ",bg = "cyan").place(x = 20, y = 20)
email = Entry(top)
email.place(x = 84, y = 20)

label2 = Label(top,text = "Password: ",bg = "cyan").place(x = 20, y = 60)
password = Entry(top,show = "*")
password.place(x = 84, y = 60)

submit = Button(text = "Submit",bg = "green",fg = "white",width = "8",command = add).place(x = 40, y = 100)
reset = Button(text = "Reset",bg = "red",fg = "white",width = "8",command = reset).place(x = 120, y = 100)

top.mainloop()
