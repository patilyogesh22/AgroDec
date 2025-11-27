from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import sys
from tkinter.ttk import *
from tkinter import *
import mysql.connector
from tkinter import messagebox

window=Tk()
window.title("Agrodec : Crop Detection System")
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
window.geometry("%dx%d"%(sw,sh))


mydb=mysql.connector.connect(host='localhost',
                             database='agrodec',
                             user='root',
                             password='root',
                             charset='utf8')

cursor=mydb.cursor()

#bg
bg=ImageTk.PhotoImage(file="Image\\udash.jpg")
l=Label(image=bg)
l.place(x=-2,y=-2)

def croppredict():
    os.system('ucroppredict.py')

def diseasedetection():
    os.system('udiseasepredict.py')
    
def weatherforecast():
    os.system('weatherforecast.py')
    
def nutrientanalysis():
    messagebox.showinfo("Not Available In these Version", "For Better Use Please Upgrade to Smart AgroDec+")
    
def cropmonitor():
    messagebox.showinfo("Not Available In these Version", "For Better Use Please Upgrade to Smart AgroDec+")
    
def cropdetails():
    messagebox.showinfo("Not Available In these Version", "For Better Use Please Upgrade to Smart AgroDec+")
    
def datamanagement():
    messagebox.showinfo("Not Available In these Version", "For Better Use Please Upgrade to Smart AgroDec+")
    
def feedback():
    messagebox.showinfo("Not Available In these Version", "For Better Use Please Upgrade to Smart AgroDec+")

def costestimation():
    messagebox.showinfo("Not Available In these Version", "For Better Use Please Upgrade to Smart AgroDec+")
 
def reports():
    messagebox.showinfo("Not Available In these Version", "For Better Use Please Upgrade to Smart AgroDec+")
def login():
    window.destroy()
    os.system("Login.py")

def Showall():
    class A(Frame):
        def __init__(self, parent):
            Frame.__init__(self, parent)
            self.CreateUI()
            self.LoadTable()
            self.grid(sticky=(N, S, W, E))
            parent.grid_rowconfigure(0, weight=1)
            parent.grid_columnconfigure(0, weight=1)
            
        def CreateUI(self):
            tv= Treeview(self)
            tv['columns']=('Enroll', 'Name', 'Mobile', 'Address', 'Email', 'Adhar','Gender','Validity','QRcode')
            tv.heading('#0',text='Enroll',anchor='center')
            tv.column('#0',anchor='center')
            tv.heading('#1', text='Name', anchor='center')
            tv.column('#1', anchor='center')
            tv.heading('#2', text='Mobile', anchor='center')
            tv.column('#2', anchor='center')
            tv.heading('#3', text='Address', anchor='center')
            tv.column('#3', anchor='center')
            tv.heading('#4', text='Email', anchor='center')
            tv.column('#4', anchor='center')
            tv.heading('#5', text='Adhar', anchor='center')
            tv.column('#5', anchor='center')
            tv.heading('#6', text='Gender', anchor='center')
            tv.column('#6', anchor='center')
            tv.heading('#7', text='Validity', anchor='center')
            tv.column('#7', anchor='center')
            tv.heading('#8', text='QRcode', anchor='center')
            tv.column('#8', anchor='center')
            tv.grid(sticky=(N,S,W,E))
            self.treeview = tv
            self.grid_rowconfigure(0,weight=1)
            self.grid_columnconfigure(0,weight=1)
        def LoadTable(self):
            Select="Select * from student"
            cursor.execute(Select)
            result=cursor.fetchall()
            name=""
            email=""
            address=""
            adhar=""
            mobile=""
            dob=""
            amount=""
            gen=""
            account=""
           
            for i in result:
                name=i[1]
                email=i[2]
                address=i[3]
                adhar=i[4]
                mobile=i[5]
                dob=i[6]
                amount=i[7]
                gen=i[8]
                account=i[0]
                
               
                self.treeview.insert("",'end',text=account,values=(name,email,address,adhar,mobile,dob,amount,gen))

    window=Tk()
    w=window.winfo_screenwidth()
    h=window.winfo_screenheight()
    window.title("Student Details")
    A(window)
    


#Heading
H=Label(window,text=" AGRODEC : Crop Detection System ",width=0,height=0,font=("comic sans ms",20,"bold"),relief=GROOVE)
H.config(bg="black",fg="white")
H.place(x=510,y=15)

p=Label(window,text="Welcome, User",width=0,height=0,font=("comic sans ms",17,"bold"),relief=GROOVE)
p.config(bg="black",fg="white")
p.place(x=1310,y=15)

user1=ImageTk.PhotoImage(file="Image\\user.png")
user=Button(image=user1)
user.place(x=1490,y=16)

#cropidentification
img1=ImageTk.PhotoImage(file="Image\\crop.png")
add=Label(image=img1)
add.place(x=180,y=140)
addn=Button(window,text="CROP\n IDENTIFICATION",width=10,height=0,font=("comic sans ms",10,"bold"),command=croppredict)
addn.config(bg="white",fg="black")
addn.place(x=170,y=240)

#nutrientanalysis
img2=ImageTk.PhotoImage(file="Image\\teacher.png")
show=Label(image=img2)
show.place(x=480,y=140)
shown=Button(window,text="NUTRIENT\n ANALYSIS",width=10,height=0,font=("comic sans ms",10,"bold"),command=nutrientanalysis)
shown.config(bg="white",fg="black")
shown.place(x=470,y=240)

#Diseasedetection
img3=ImageTk.PhotoImage(file="Image\\file.png")
add=Label(image=img3)
add.place(x=1200,y=140)
addn=Button(window,text="DISEASE\n DETECTION",width=10,height=0,font=("comic sans ms",10,"bold"),command=diseasedetection)
addn.config(bg="white",fg="black")
addn.place(x=1190,y=240)

#Cropgrowthmonitor
img4=ImageTk.PhotoImage(file="Image\\road.png")
show=Label(image=img4)
show.place(x=900,y=140)
shown=Button(window,text="CROP\n GROWTH MONITOR",width=10,height=0,font=("comic sans ms",10,"bold"),command=cropmonitor)
shown.config(bg="white",fg="black")
shown.place(x=890,y=240)

#Weatherforecast
img5=ImageTk.PhotoImage(file="Image\\rain.png")
add=Label(image=img5)
add.place(x=180,y=400)
addn=Button(window,text="WEATHER\n FORECASTING",width=10,height=0,font=("comic sans ms",10,"bold"),command=weatherforecast)
addn.config(bg="white",fg="black")
addn.place(x=170,y=500)

#feedback
img6=ImageTk.PhotoImage(file="Image\\logout.png")
show=Label(image=img6)
show.place(x=1200,y=400)
shown=Button(window,text="FEEDBACK /\n QUERY",width=10,height=0,font=("comic sans ms",10,"bold"),command=feedback)
shown.config(bg="white",fg="black")
shown.place(x=1190,y=500)

#cropdetails
img7=ImageTk.PhotoImage(file="Image\\money.png")
add=Label(image=img7)
add.place(x=480,y=400)
addn=Button(window,text="CROP\n DETAILS",width=10,height=0,font=("comic sans ms",10,"bold"),command=cropdetails)
addn.config(bg="white",fg="black")
addn.place(x=470,y=500)


#costestimation
img8=ImageTk.PhotoImage(file="Image\\history.png")
show=Label(image=img8)
show.place(x=900,y=400)
shown=Button(window,text="COST\n ESTIMATION",width=10,height=0,font=("comic sans ms",10,"bold"),command=costestimation)
shown.config(bg="white",fg="black")
shown.place(x=890,y=500)

#logout
log=Button(window,text="Logout",width=10,height=0,font=("comic sans ms",10,"bold"),command=login)
log.config(bg="white",fg="black")
log.place(x=1420,y=730)


#L1=Label(window,text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n",width=0,height=0,font=("Comic sans ms",10,"bold"))
#L1.config(fg="black")
#L1.place(x=672,y=55)

window.mainloop()
