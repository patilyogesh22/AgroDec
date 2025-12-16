from tkinter import *
from tkinter.filedialog import asksaveasfile,askopenfile
import tkinter as tk
from PIL import Image,ImageTk
from tkcalendar import Calendar as cal
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime
from tkinter import Entry, Tk
from tkinter import messagebox
import tkinter.font as tkFont
import time

window=Tk()
window.title("Add Student")
window.config(bg="Skyblue")

sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
w=sw-550
h=sh-200
wpos=(sw/2)-(w/2)
hpos=(sh/2)-(h/2)
window.geometry("%dx%d+%d+%d"%(w,h,wpos,hpos))

#bg
bg=ImageTk.PhotoImage(file="Image\\Student.jpg")
l=Label(image=bg)
l.place(x=-200,y=-200)

mydb=mysql.connector.connect(host='localhost',
                             database='Medicaps',
                             user='root',
                             password='root',
                             charset='utf8')

cursor=mydb.cursor()

#dropdown
def gender(event):
    option=selected.get()
    return option
    print(option)
    
#save query
def saveindb():
    b1["state"]=NORMAL
    b2["state"]=NORMAL
    b3["state"]=NORMAL
    b4["state"]=NORMAL
    b5["state"]=NORMAL
    fenroll=E1.get()
    fname=E2.get()
    fmobile=E3.get()
    faddress=E4.get()
    femail=E5.get()
    fadhar=E8.get()
    fgender=selected.get()
    fsession=E10.get()
    
    '''dobvar=var.get()
    a=datetime.strptime(dobvar,"%m%d%y")
    dat=(a.strftime('%Y-%m-%d'))'''

    
    
    query = "INSERT INTO student(Enroll,Name,Mobile,Address,Email,Adhar,Gender,validity) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    args = (fenroll,fname,fmobile,faddress,femail,fadhar,fgender,fsession)
    
    try:
        cursor.execute(query,args)
        mydb.commit()
        idd=1
        for i in range(1,idd+1):
            print(i)
            idd=i+1
         
        messagebox.showinfo("SUCCESSFULLY INSERTED", "Record of Student Inserted Successfully")

    except Error as error:
        print("Failed to insert record into table {}".format(error))#print(error)
        messagebox.showinfo("code error")
    finally:
        cursor.close()
        mydb.close()

#update query
def updateindb():
    b1["state"]=NORMAL
    b2["state"]=NORMAL
    b3["state"]=NORMAL
    b4["state"]=NORMAL
    b5["state"]=NORMAL
    fenroll=E1.get()
    fname=E2.get()
    fmobile=E3.get()
    faddress=E4.get()
    femail=E5.get()
    fadhar=E8.get()
    fgender=selected.get()

    update="Update student set Name=%s,Mobile=%s,Address=%s,Email=%s,Adhar=%s,Gender=%s where Enroll=%s"
    values=(fname,fmobile,faddress,femail,fadhar,fgender,fenroll)

    try:
        cursor.execute(update,values)
        mydb.commit()
        messagebox.showinfo("SUCCESSFULLY UPDATED", "Record updated successfully")

    except Error as error:
        print("Failed to update record into table {}".format(error))#print(error)
        messagebox.showinfo("code error")
    finally:
        cursor.close()
        mydb.close()



def saver():
    files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file = askopenfile(filetypes = files, defaultextension = files)
    image=Image.open(file.name)
    image=image.resize((100, 100), Image.ANTIALIAS)
    img= ImageTk.PhotoImage(image)
    
def upload():
    files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file = askopenfile(filetypes = files, defaultextension = files)
    image=Image.open(file.name)
    image=image.resize((100, 100), Image.ANTIALIAS)
    img= ImageTk.PhotoImage(image)
    box=Label(window,image=img)
    box.image=img
    box.place(x=600,y=100)
    
    
down=True
var=StringVar()
def down():
    global down
    if down:
        var.set(str(cal.get_date()))
        cal.place(x=280,y=330,height=320,width=320)
        down=False
            
    else:
        var.set(str(cal.get_date()))
        cal.place(x=0,y=0,height=0,width=0)
        down=True

    
def new():
    E1["state"]=NORMAL
    E2["state"]=NORMAL
    E3["state"]=NORMAL
    E4["state"]=NORMAL
    E5["state"]=NORMAL
    E8["state"]=NORMAL
    E9["state"]=NORMAL
    img1["state"]=NORMAL
    b2["state"]=NORMAL
    b5["state"]=NORMAL
    #var.set("")
    var1.set("")
    var2.set("")
    var3.set("")
    var4.set("")
    var5.set("")
    var8.set("")
    E1.focus()
    
    
    
def update():
    b3["state"]=NORMAL
    
def delete():
    b4["state"]=NORMAL
    
def search():
    b5["state"]=DISABLED
    b1["state"]=DISABLED
    b2["state"]=DISABLED
    b6["state"]=DISABLED
    b4["state"]=NORMAL
    b3["state"]=NORMAL
    
#heading
H=Label(window,text="MEDICAPS STUDENT BUS SERVICE",height=0,width=0,font=("comic sans ms",25,"bold"))
H.config(bg="white",fg="black")
H.place(x=215,y=10)

#firstname
l1=Label(window,text="Enter Enrollment",width=0,height=0,font=("comic sans ms",20,"bold"))
l1.config(bg="White",fg="black")
l1.place(x=120,y=150)
var1=StringVar()
E1=Entry(window,textvariable=var1,width=25,font=("comic sans ms",18,"bold"))
E1.config(bg="white",fg="black")
E1.place(x=400,y=155)

#secondname
l2=Label(window,text="Enter Full Name",width=0,height=0,font=("comic sans ms",20,"bold"))
l2.config(bg="white",fg="black")
l2.place(x=120,y=200)
var2=StringVar()
E2=Entry(window,textvariable=var2,width=25,font=("comic sans ms",18,"bold"))
E2.config(bg="white",fg="black")
E2.place(x=400,y=205)

#address
l3=Label(window,text="Enter Mobile No.",width=0,height=0,font=("comic sans ms",20,"bold"))
l3.config(bg="white",fg="black")
l3.place(x=120,y=250)
var3=StringVar()
E3=Entry(window,textvariable=var3,width=25,font=("comic sans ms",18,"bold"))
E3.config(bg="white",fg="black")
E3.place(x=400,y=255)

#adhar no
l4=Label(window,text="Enter Full Address",width=0,height=0,font=("comic sans ms",20,"bold"))
l4.config(bg="white",fg="black")
l4.place(x=120,y=300)
var4=StringVar()
E4=Entry(window,textvariable=var4,width=25,font=("comic sans ms",18,"bold"))
E4.config(bg="white",fg="black")
E4.place(x=400,y=305)

#Mobile no
l5=Label(window,text="Enter Email Id",width=0,height=0,font=("comic sans ms",20,"bold"))
l5.config(bg="white",fg="black")
l5.place(x=120,y=350)
var5=StringVar()
E5=Entry(window,textvariable=var5,width=25,font=("comic sans ms",18,"bold"))
E5.config(bg="white",fg="black")
E5.place(x=400,y=355)


#adhar
l8=Label(window,text="Enter Adhar No.",width=0,height=0,font=("comic sans ms",20,"bold"))
l8.config(bg="white",fg="black")
l8.place(x=120,y=400)
var8=StringVar()
E8=Entry(window,textvariable=var8,width=25,font=("comic sans ms",18,"bold"))
E8.config(bg="white",fg="black")
E8.place(x=400,y=405)

#Session
l10=Label(window,text="Enter Your Session",width=0,height=0,font=("comic sans ms",20,"bold"))
l10.config(bg="white",fg="black")
l10.place(x=120,y=500)
var10=StringVar()
E10=Entry(window,textvariable=var10,width=25,font=("comic sans ms",18,"bold"))
E10.config(bg="white",fg="black")
E10.place(x=400,y=505)

#gender
l9=Label(window,text="Select Your Gender",width=0,height=0,font=("comic sans ms",20,"bold"))
l9.config(bg="white",fg="black")
l9.place(x=120,y=450)
helv36 = tkFont.Font(family='comic sans ms', size=15)
options = 'Male Female Others'.split()
selected = tk.StringVar(window, value=options[0])
E9 = tk.OptionMenu(window, selected, *options,command=gender)
E9.config(font=helv36) # set the button font
helv20 = tkFont.Font(family='comic sans ms', size=15)
menu = window.nametowidget(E9.menuname)  # Get menu widget.
menu.config(font=helv20)  # Set the dropdown menu's font
E9.place(x=400,y=455)




#buttons
b1=Button(window,text=" NEW ",width=0,height=0,font=("comic sans ms",15,"bold"),command=new)
b1.config(bg="white",fg="black")
b1.place(x=100,y=590)
b2=Button(window,text=" SAVE ",width=0,height=0,font=("comic sans ms",15,"bold"),command=saveindb,state=DISABLED)
b2.config(bg="white",fg="black")
b2.place(x=250,y=590)
b3=Button(window,text="UPDATE",width=0,height=0,font=("comic sans ms",15,"bold"),command=updateindb,state=DISABLED)
b3.config(bg="white",fg="black")
b3.place(x=400,y=590)
b4=Button(window,text="DELETE",width=0,height=0,font=("comic sans ms",15,"bold"),command=delete,state=DISABLED)
b4.config(bg="white",fg="black")
b4.place(x=550,y=590)
b5=Button(window,text="SEARCH",width=0,height=0,font=("comic sans ms",15,"bold"),command=search,state=DISABLED)
b5.config(bg="white",fg="black")
b5.place(x=700,y=590)
b6=Button(window,text=" EXIT ",width=0,height=0,font=("comic sans ms",15,"bold"),command=window.destroy)
b6.config(bg="white",fg="black")
b6.place(x=850,y=590)


#upload
img1= Button(window,text="Upload Image",font=("comic sans ms",12,"bold"), command=lambda:upload())
img1.place(x=810,y=220)

'''
#calendar
l6=Label(window,text="Select Date",width=0,height=0,font=("comic sans ms",15,"bold"))
l6.config(bg="skyblue",fg="black")
l6.place(x=100,y=300)
cal=Calendar(window,selectmode="day",year=2021,month=9,day=16)
bc1=Button(window,text="⏬",width=0,height=0,command=down)
bc1.config(bg="white")
bc1.place(x=472,y=305)        
var=StringVar()
l7=Label(window,textvariable=var,width=22,height=0)
l7.config(bg="white")
l7.place(x=320,y=307)
'''

#textbox state
E1["state"]=DISABLED
E2["state"]=DISABLED
E3["state"]=DISABLED
E4["state"]=DISABLED
E5["state"]=DISABLED
E8["state"]=DISABLED
E9["state"]=DISABLED
img1["state"]=DISABLED



window.mainloop()
