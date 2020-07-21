# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 19:05:52 2020

@author: Sourick
"""
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

top = Tk()
top.minsize(640,402)
file = None
string_count = 0
top.title("Untitled - Notepad")
top.wm_iconbitmap("notepad_icon.ico")
TextArea = Text(top,font = "verdana")
TextArea.pack(expand=True,fill=BOTH)

def ex():
    top.destroy()
    
def new():
    global file
    file = None
    top.title("Untitled - Notepad")
    TextArea.delete(1.0,END)
    
    
def openf():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    
    if file == "":
        file = None
    else:     
        top.title(os.path.basename(file) + "- SS Notepad")
        TextArea.delete(1.0, END)
        fpt = open(file, "r")
        TextArea.insert(1.0, fpt.read())
        fpt.close()

def save():
    global file
    
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    
        if file == "":
            file = None
        else:
            top.title(os.path.basename(file) + "- SS Notepad")
            fpt = open(file,"w")
            fpt.write(TextArea.get(1.0,END))
            fpt.close()
            
            
    else:
        top.title(os.path.basename(file) + "- SS Notepad")
        fpt = open(file,"w")
        fpt.write(TextArea.get(1.0,END))
        fpt.close()
 
        
def find():
    global string_count
    find = simpledialog.askstring("Find String", "Enter String :")
    textarea1 = str(TextArea.get(1.0,END))
    string_count =  textarea1.count(find)   
    messagebox.showinfo("String Found","The Number of string is : " + str(string_count))
  
def find_replace():
    find = simpledialog.askstring("Find String", "Enter String :")
    replace = simpledialog.askstring("Replace String", "Enter String :")
    textarea1 = str(TextArea.get(1.0,END))
    NEW = textarea1.replace(find,replace)
    
    #Content Overwriting 
    TextArea.delete(1.0,END) 
    TextArea.insert(1.0,NEW)
    
    messagebox.showinfo("String Found","Replace Done!!!")
    
def cut():
    TextArea.event_generate('<Control-x>')

def copy():
    TextArea.event_generate('<Control-c>')
    
def paste():
    TextArea.event_generate('<Control-v>')

def selectALL():
    TextArea.event_generate('<Control-a>')
    
def about():
    message = "Developed By: Soujatya Bhattacharya\n Version : 1.0"
    messagebox.showinfo("About",message)


menubar = Menu(top)

#File Submenu
File = Menu(menubar)
File.add_command(label = "New",command = new)
File.add_command(label = "Open",command = openf)
File.add_command(label = "Save",command = save)
File.add_separator()
File.add_command(label = "Exit", command = ex)
menubar.add_cascade(label="File", menu=File) 


#Edit Submenu
Edit = Menu(menubar)
Edit.add_command(label = "Cut",command = cut)
Edit.add_command(label = "Copy",command = copy)
Edit.add_command(label = "Paste",command = paste)
Edit.add_separator()
Edit.add_command(label = "Find",command = find)
Edit.add_command(label = "Find & Replace",command = find_replace)
Edit.add_command(label = "Select All",command = selectALL)
menubar.add_cascade(label="Edit", menu=Edit) 


#Others
Help = Menu(menubar)
Help.add_command(label="About",command=about)
menubar.add_cascade(label="Help", menu=Help)

top.config(menu = menubar)

#Scrollbar
Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT,  fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)
top.mainloop()
