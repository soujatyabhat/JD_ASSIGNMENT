# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 19:55:15 2020

@author: Sourick
"""
import smtplib
import random
server = True
OTP = 0
def sendmail():
    global OTP,server
    OTP = random.randint(100000, 999999)
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login("soujatya.bhat2000@gmail.com","@soujatya123**")
    OTP = str(OTP)
    server.sendmail("soujatya.bhat2000@gmail.com", "candila.ppf105@gmail.com",OTP)

    
    
print("User Signup System")
fpt = open("add.txt","a")
sendmail()
name = input("Enter your full name :")
address = input("Enter your address :")
phonenumber = int(input("Enter Phone Number : "))
DOB = input("Enter DOB :")
email = input("Enter Email ID :")
password = input("Enter Password : ")
confirm_password = input("Enter  Confirm  Password : ")
a = int(input("Enter 6 digit OTP :"))

details = name + ' ' + address + ' ' + str(phonenumber) + ' ' + DOB + ' ' + str (email) + ' ' + str(confirm_password) + ' ' +'\n'
if password == confirm_password:
    if OTP == str(a):
        fpt.write(details)
        print("Account has created")
    else:
        print("OTP has not matched")

else:
    print("Password not matched")

fpt.close()
    


