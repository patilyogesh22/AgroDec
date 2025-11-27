from tkinter import messagebox
from tkinter.ttk import Progressbar
import time
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
import os
import mysql.connector
import re
import hashlib
import pymysql

window=Tk()
window.title("Register to Agrodec")
window.config(bg="skyblue")

w=window.winfo_screenwidth()-800
h=window.winfo_screenheight()-400
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
wpos=(sw/2)-(w/2)
hpos=(sh/2)-(h/2)
window.geometry("%dx%d+%d+%d"%(w,h,wpos,hpos))

bg=ImageTk.PhotoImage(file="Image\\agrolog.jpg")
bgl=Label(window,image=bg)
bgl.place(x=-2,y=-3)

# Connect to the MySQL database
db = pymysql.connect(host="localhost", user="root", password="root", database="agrodec",charset='utf8')
cursor = db.cursor()

def register():
    # Get the form fields
    user = name.get()
    psw1 = psw.get()
    repsw = cpsw.get()

    if user and psw1 and repsw:
            # Check if the user already exists
            query = "SELECT * FROM register WHERE username=%s"
            cursor.execute(query, (user,))
            result = cursor.fetchone()
            
            if result:
                messagebox.showinfo("User Already Exixst", "You already Register Please Login to your Account")
                window.destroy()
                os.system("Login.py")
                name.delete(0, tk.END)
                psw.delete(0, tk.END)
                cpsw.delete(0, tk.END)
                
            else:
                # Insert the new user into the database
                query = "INSERT INTO register (username, password, repassword) VALUES (%s, %s, %s)"
                cursor.execute(query, (user, psw1, repsw))
                db.commit()
                # Show a success message
                messagebox.showinfo("Registration successful", "You have successfully registered.")

                # Clear the form fields
                name.delete(0, tk.END)
                psw.delete(0, tk.END)
                cpsw.delete(0, tk.END)
                window.destroy()
                os.system("Login.py")

    else:
        # Show an error message
        messagebox.showerror("Error", "Please fill in all fields.")

def login():
    window.destroy()
    os.system("Login.py")
    
l1=Label(window,text="REGISTER TO AGRO DEC",font=("comic sans ms",18,"bold"))    
l1.place(x=240,y=10)     
#label
nameL=Label(window,text="Enter Username:",width=0,height=0,font=("comic sans ms",20,"bold"))
nameL.config(bg="skyblue",fg="Black")
nameL.place(x=150,y=100)
passL=Label(window,text="Enter Password :",width=0,height=0,font=("comic sans ms",20,"bold"))
passL.config(bg="skyblue",fg="Black")
passL.place(x=150,y=200)
cpassL=Label(window,text="Enter RePassword :",width=0,height=0,font=("comic sans ms",20,"bold"))
cpassL.config(bg="skyblue",fg="Black")
cpassL.place(x=150,y=300)

#entry
var1=StringVar()
name=Entry(window,textvariable=var1,width=16,font=("comic sans ms",18,"bold"))
name.config(bg="white",fg="black")
name.place(x=420,y=100)
var2=StringVar()
psw=Entry(window,textvariable=var2,show="*",width=16,font=("comic sans ms",18,"bold"))
psw.config(bg="white",fg="black")
psw.place(x=420,y=200)
var3=StringVar()
cpsw=Entry(window,textvariable=var3,show="*",width=16,font=("comic sans ms",18,"bold"))
cpsw.config(bg="white",fg="black")
cpsw.place(x=420,y=300)

#button
ok=Button(window,text="REGISTER",width=0,height=0,font=("comic sans ms",15,"bold"),command=register)
ok.config(bg="white",fg="black")
ok.place(x=270,y=365)
can=Button(window,text="CANCEL",width=0,height=0,font=("comic sans ms",15,"bold"),command=window.destroy)
can.config(bg="white",fg="black")
can.place(x=400,y=365)

#forgot password
pas=Label(window,text="Already a user..?",font=("comic sans ms",12,"bold"))
pas.config(bg="white",fg="red")
pas.place(x=250,y=440)
rst=Button(window,text="Login",width=0,height=0,font=("comic sans ms",10,"bold"),command=login)
rst.config(bg="white",fg="black")
rst.place(x=420,y=440)

window.mainloop()
