# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 19:25:39 2020

@author: Sourick
"""

from tkinter import *
from tkinter import messagebox
import tkinter.font as font

top = Tk()
top.title("Free Tic Tac Toe")
top.geometry("300x320")
top.resizable(0,0)
canvas = Canvas()
top.config(bg = "yellow")
top.withdraw()

cell_counter = tie =  0

Switch = 0
players_score = player1_score = player2_score = 0

def checking():    

    value1 = text1.get()
    value2 = text2.get()
    value3 = text3.get()
    value4 = text4.get()
    value5 = text5.get()
    value6 = text6.get()
    value7 = text7.get()
    value8 = text8.get()
    value9 = text9.get()
    
    if cell_counter != 9:
        
        if((value1 == 'X') and (value2 == 'X') and (value3 == 'X') 
        or (value1 == 'O') and (value2 == 'O') and (value3 == 'O')):
            declear_winner(value1)
        
        elif((value4 == 'X') and (value5 == 'X') and (value6 == 'X') 
        or (value4 == 'O') and (value5 == 'O') and (value6 == 'O')):
            declear_winner(value5)
        
        elif((value7 == 'X') and (value8 == 'X') and (value9 == 'X') 
        or (value7 == 'O') and (value8 == 'O') and (value9 == 'O')):
            declear_winner(value7)
        
        elif((value1 == 'X') and (value5 == 'X') and (value9 == 'X') 
        or (value1 == 'O') and (value5 == 'O') and (value9 == 'O')):
            declear_winner(value1)
        
        elif((value3 == 'X') and (value5 == 'X') and (value7 == 'X') 
        or (value3 == 'O') and (value5 == 'O') and (value7 == 'O')):
            declear_winner(value3)
            
        elif((value1 == 'X') and (value4 == 'X') and (value7 == 'X') 
        or (value1 == 'O') and (value4 == 'O') and (value7 == 'O')):
            declear_winner(value4)
            
        elif((value2 == 'X') and (value5 == 'X') and (value8 == 'X') 
        or (value2 == 'O') and (value5 == 'O') and (value8 == 'O')):
            declear_winner(value2)
   
        elif((value3 == 'X') and (value6 == 'X') and (value9 == 'X') 
        or (value3 == 'O') and (value6 == 'O') and (value9 == 'O')):
            declear_winner(value3)
    
    else:
            declear_winner(0)
    
    
def lock():
    global cell_counter
    cell_counter += 1
    value1,value2,value3,value4,value5 = text1.get(),text2.get(),text3.get(),text4.get(),text5.get()
    value6,value7,value8,value9 = text6.get(),text7.get(),text8.get(),text9.get()
    if (len(value1) > 0):
        text1['state'] = 'disabled'
    if (len(value2) > 0):
        text2['state'] = 'disabled'
    if (len(value3) > 0):
        text3['state'] = 'disabled'    
    if (len(value4) > 0):
        text4['state'] = 'disabled'
    if (len(value5) > 0):
        text5['state'] = 'disabled'
    if (len(value6) > 0):
        text6['state'] = 'disabled'  
    if (len(value7) > 0):
        text7['state'] = 'disabled'
    if (len(value8) > 0):
        text8['state'] = 'disabled'
    if (len(value9) > 0):
        text9['state'] = 'disabled'      
    print(cell_counter)
    checking()
        
    
def declear_winner(player):
    global player1_score,player2_score,players_score
    if player == player1 : 
        name =  "Player 1 is Win"
        player1_score = player1_score + 1
        
    elif player == player2:
        name = "Player 2 is Win" 
        player2_score = player2_score + 1
    
    else:
        name = "Match has been Tie"
        
    messagebox.showinfo("Result",name)
    players_score  = "Scores " + "\n Player 1 :" + str(player1_score) + " Player 2 :" + str(player2_score)
    label2.config(text = players_score)


def reset():
    global cell_counter = messagebox.askquestion("Confirmation","Do You Want to play again ?")
    if n == 'yes' :  
        text1['state'] = 'normal'
        text2['state'] = 'normal'
        text3['state'] = 'normal'
        text4['state'] = 'normal'
        text5['state'] = 'normal'
        text6['state'] = 'normal'
        text7['state'] = 'normal'
        text8['state'] = 'normal'
        text9['state'] = 'normal'
        text1.delete(0, END)
        text2.delete(0, END)
        text3.delete(0, END)
        text4.delete(0, END)
        text5.delete(0, END)
        text6.delete(0, END)
        text7.delete(0, END)
        text8.delete(0, END)
        text9.delete(0, END)
        cell_counter = 0
    
  
player1 = simpledialog.askstring("Simple Tik Tac Tue Game", "Player 1 Choice (Only press X or O :")
player2 = simpledialog.askstring("Simple Tik Tac Tue Game", "Player 2 Choice (Only press X or O :")

top.deiconify()
players  = "Player 1 : " + player1 + "\n" + "Player 2 : " + player2

#Formattings
canvas.create_line(5, 75, 320, 75,width = 8)
canvas.create_line(5, 125, 320, 125,width = 8)
canvas.create_line(105, 6, 105, 200,width = 8)
canvas.create_line(196, 6, 196, 200,width = 8)
canvas.pack()
myfont = font.Font(size=15)


#One Box
text1 = Entry(top,text = ".", width = "7",fg = "#7F00FF")
text1.place(x = 20, y = 30,height = "40") 
text1['font'] = myfont

#
text2 = Entry(top,text = "..",width = "7")
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


button1 = Button(top,text = "Make Final",bg = "Green",fg = "White",height = "2",command = lock).place(x = 116,y = 180)
button2 = Button(top,text = "New Game",bg = "Red",fg = "White",height = "2",width = "8",command = reset).place(x = 210,y = 180)

players_score  = "Scores " + "\n Player 1 :" + str(player1_score) + " Player 2 :" + str(player2_score)

label2 = Label(top,text = players_score,bg = "Blue", fg = "white")
label2.place(x = 60, y = 240,height = "50",width = "190")


top.mainloop()





