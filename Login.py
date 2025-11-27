from tkinter import messagebox
from tkinter.ttk import Progressbar
import time
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
import os
import mysql.connector

window=Tk()
window.title("Login to Agrodec")
window.config(bg="skyblue")

w=window.winfo_screenwidth()-820
h=window.winfo_screenheight()-400
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
wpos=(sw/2)-(w/2)
hpos=(sh/2)-(h/2)
window.geometry("%dx%d+%d+%d"%(w,h,wpos,hpos))

bg=ImageTk.PhotoImage(file="Image\\agrolo.jpg")
bgl=Label(window,image=bg)
bgl.place(x=-2,y=-3)

def register():
    window.destroy()
    os.system("Register.py")


def login():
    user=name.get()
    passw=psw.get()

    if user=="admin":
        db = mysql.connector.connect(host="localhost", user="root", password="root", database="agrodec",charset="utf8")
        cursor = db.cursor()
        
        query = f"SELECT * FROM register WHERE username = '{user}' AND password = '{passw}'"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Success", "Login successful!")
            window.destroy()
            os.system("ADashboard.py")
            
        else:
            messagebox.showerror("Error", "Invalid username or password")
            var1.set('')
            var2.set('')
            name.focus()
            
    elif user!="admin":
        db = mysql.connector.connect(host="localhost", user="root", password="root", database="agrodec",charset="utf8")
        cursor = db.cursor()
        
        query = f"SELECT * FROM register WHERE username = '{user}' AND password = '{passw}'"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Success", "Login successful!")
            window.destroy()
            os.system("UDashboard.py")
            
        else:
            messagebox.showerror("Error", "Invalid username or password")
            var1.set('')
            var2.set('')
            name.focus()        

    else:
        messagebox.showinfo("VERIFICATION", "No User Found")
    

l1=Label(window,text="LOGIN TO AGRO DEC",font=("comic sans ms",18,"bold"))    
l1.place(x=240,y=10)     
#label
nameL=Label(window,text="Enter Username:",width=0,height=0,font=("comic sans ms",20,"bold"))
nameL.config(bg="skyblue",fg="Black")
nameL.place(x=150,y=150)
passL=Label(window,text="Enter Password :",width=0,height=0,font=("comic sans ms",20,"bold"))
passL.config(bg="skyblue",fg="Black")
passL.place(x=150,y=250)

#entry
var1=StringVar()
name=Entry(window,textvariable=var1,width=16,font=("comic sans ms",18,"bold"))
name.config(bg="white",fg="black")
name.place(x=400,y=150)
var2=StringVar()
psw=Entry(window,textvariable=var2,show="*",width=16,font=("comic sans ms",18,"bold"))
psw.config(bg="white",fg="black")
psw.place(x=400,y=250)

#button
ok=Button(window,text="OK",width=0,height=0,font=("comic sans ms",15,"bold"),command=login)
ok.config(bg="white",fg="black")
ok.place(x=270,y=340)
can=Button(window,text="CANCEL",width=0,height=0,font=("comic sans ms",15,"bold"),command=window.destroy)
can.config(bg="white",fg="black")
can.place(x=370,y=340)

#forgot password
pas=Label(window,text="NEW USER...",font=("comic sans ms",13,"bold"))
pas.config(bg="white",fg="red")
pas.place(x=240,y=420)
rst=Button(window,text="REGISTER HERE",width=0,height=0,font=("comic sans ms",11,"bold"),command=register)
rst.config(bg="white",fg="black")
rst.place(x=400,y=415)

window.mainloop()
