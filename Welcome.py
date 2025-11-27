from tkinter.ttk import Progressbar
import time
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
import os
import pymysql

window=Tk()
window.title("AgroDec : Agriculture Detection")
window.config(bg="skyblue")

w=window.winfo_screenwidth()-300
h=window.winfo_screenheight()-200
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
window.geometry("%dx%d"%(sw,sh))
window.maxsize(1600,1000)

bg=ImageTk.PhotoImage(file="Image\\wel1.jpg")
bgl=Label(window,image=bg)
bgl.place(x=0,y=0)

def display():
    for i in range(1,11):
        window.update_idletasks()
        P['value']+=10
        time.sleep(0.4)
        L['text']=P['value'],'%'
        L.config(bg="white")
        
    window.destroy()
    os.system("Login.py")


L1=Label(window,text="WELCOME TO AGRODEC",width=0,height=0,font=("Comic Sans Ms",35,"bold"))
L1.config(bg="White",fg="Black")
L1.place(x=490,y=10)


L2=Label(window,text="AD Version-0.1",width=0,height=0,font=("Comic Sans Ms",10,"bold"))
L2.config(bg="white",fg="Black")
L2.place(x=1400,y=750)

Load=Label(window,text="Loading ",width=0,height=0,font=("Comic Sans Ms",15,"bold"))
Load.place(x=700,y=750)

L=Label(window,font=("Comic Sans Ms",15,"bold"))
L.place(x=800,y=750)

P=Progressbar(window,orient=HORIZONTAL,length=300,mode='determinate',value=0)
P.place(x=620,y=720)

display()
window.mainloop()
