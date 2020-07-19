# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 09:34:45 2020

@author: Sourick
"""
from tkinter import *
import smtplib
import random
from tkinter import messagebox
server = True
OTP = 0
top = Tk()
top.geometry("355x400")
top.resizable(0,0)
top.title("Signup")
top.config(bg = "yellow")


def reset(): 
    text1.delete(0, END)
    text2.delete(0, END)
    text3.delete(0, END)
    text4.delete(0, END)
    email.delete(0, END)
    password.delete(0, END)
    confirm_password.delete(0, END)
    otp.delete(0, END)

def sendmail():
    global OTP,server
    OTP = random.randint(100000, 999999)
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login("soujatya.bhat2000@gmail.com","@soujatya123**")
    OTP = str(OTP)
    server.sendmail("soujatya.bhat2000@gmail.com", "candila.ppf105@gmail.com",OTP)
    messagebox.showinfo("Sending Successful","OTP has send to your email")
 

    
def save():
    global otp
    fpt = open("record.txt","a")
    name = text1.get()
    address = text2.get()
    phone_number = text3.get()
    dob =  text4.get()
    mail = email.get()
    password1 = password.get()
    conf_password1 = confirm_password.get()
    otp_new = otp.get()
    if ((len(name) > 0)  and (len(phone_number) > 0) and (len(dob) > 0) and (len(mail) > 0) and (len(password1) > 0) and (len(conf_password1) > 0) (len(otp_new) > 0)):
        if password1 == conf_password1:  
            if OTP == otp_new:
                details = name + ' ' + address + ' ' + str(phone_number) + ' ' + dob + ' ' + str (mail) + ' ' + str(conf_password1) + ' ' +'\n'
                fpt.write(details)
                fpt.close()
                messagebox.showinfo("Conglatunation","Your account has been created")
            else:
                messagebox.showerror("Failure","OTP has not mathched. Press Send OTP button and try again")
                otp.config(text = " ")   
        else:
            messagebox.showerror("Failure","Your account has been created")  
    else:
        messagebox.showerror("Failure","Textboxes are empty")  
        
    text1.delete(0, END)
    text2.delete(0, END)
    text3.delete(0, END)
    text4.delete(0, END)
    email.delete(0, END)
    password.delete(0, END)
    confirm_password.delete(0, END)
    otp.delete(0, END)
    




label1 = Label(top,text = "Enter Your full Name : ",bg = "yellow").place(x = 5, y = 20)
text1 = Entry(top,width = "30")
text1.place(x = 160, y = 20)

label2 = Label(top,text = "Enter Address: ",bg = "yellow").place(x = 17, y = 60)
text2 = Entry(top,width = "30")
text2.place(x = 160, y = 60)

label3 = Label(top,text = "Phone Number : ",bg = "yellow").place(x = 17, y = 100)
text3 = Entry(top,width = "30")
text3.place(x = 160, y = 100)

label4 = Label(top,text = "Enter DOB (dd/mm/yyyy): ",bg = "yellow").place(x = 5, y = 140)
text4 = Entry(top,width = "30")
text4.place(x = 160, y = 140)

label5 = Label(top,text = "Email ID: ",bg = "yellow").place(x = 30, y = 180)
email = Entry(top)
email.place(x = 160, y = 180)
send_otp = Button(text = "Send OTP",command = sendmail).place(x = 290, y = 180)

label6 = Label(top,text = "Enter Password ",bg = "yellow").place(x = 17, y = 220)
password = Entry(top,show = "*",width = "30")
password.place(x = 160, y = 220)


label7 = Label(top,text = "Enter confirm password: ",bg = "yellow").place(x = 5, y = 260)
confirm_password = Entry(top,show = "*",width = "30")
confirm_password.place(x = 160, y = 260)

label7 = Label(top,text = "Enter confirm OTP",bg = "yellow").place(x = 5, y = 300)
otp = Entry(top,width = "30")
otp.place(x = 160, y = 300)

submit = Button(text = "Submit",bg = "green",fg = "white",width = "15",command = save).place(x = 60, y = 340)
reset = Button(text = "Reset",bg = "red",fg = "white",width = "15", command = reset).place(x = 180, y = 340)

    
    
top.mainloop()

