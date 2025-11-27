from tkinter import *
import random
import smtplib
from PIL import Image, ImageTk

window=Tk()
window.title("OTP Verifier")
window.config(bg="Skyblue")

rw=550
rh=430
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
wpos=(sw/2)-(rw/2)
hpos=(sh/2)-(rh/2)
window.geometry("%dx%d+%d+%d"%(rw,rh,wpos,hpos))
window.maxsize(2560,1600)
window.minsize(650,450)

def generate_otp():
    return str(random.randint(100000, 999999))

def send_email(email, otp):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("name@gmail.com", "password")
    message = "Your otp is "+otp
    server.sendmail('Mail for You', email, message)
    server.quit()

def verify_otp():
    user_otp = e2.get()
    if user_otp == otp:
        L2.config(text='OTP Verified', fg='green')
    else:
        L2.config(text='OTP Incorrect', fg='red')

def send_otp():
    global otp
    otp = generate_otp()
    email = e1.get()
    send_email(email, otp)
    L1.config(text='OTP Sent')

#image
#alarm=ImageTk.PhotoImage(file="Images\\Pass.jpg")
#add=Label(image=alarm)
#add.place(x=270,y=75)

#mail
l1=Label(window,text="Enter Your Email:",width=0,height=0,font=("Comic Sans MS",15,"bold","underline"))
l1.configure(bg="Skyblue",fg="black")
l1.place(x=40,y=220)
e1=Entry(window,font=(5))
e1.configure(bg="white",fg="Black")
e1.place(x=250,y=225)
b1=Button(window,text="Send OTP",width=10,height=0,font=(30),command=send_otp)
b1.config(bg="white",fg="Blue")
b1.place(x=500,y=220)
L1=Label(window,text=" ",width=0,height=0,font=("Comic Sans MS",8,"bold"))
L1.configure(bg="Skyblue",fg="black")
L1.place(x=300,y=260)

#otp
l3=Label(window,text="Enter 6-digit OTP:",width=0,height=0,font=("Comic Sans MS",15,"bold","underline"))
l3.configure(bg="Skyblue",fg="black")
l3.place(x=40,y=300)
e2=Entry(window,font=(5))
e2.configure(bg="white",fg="Black")
e2.place(x=250,y=305)
b1=Button(window,text="Verify OTP",width=10,height=0,font=(30),command=verify_otp)
b1.config(bg="white",fg="Blue")
b1.place(x=500,y=300)
L2=Label(window,text=" ",width=0,height=0,font=("Comic Sans MS",8,"bold"))
L2.configure(bg="Skyblue",fg="black")
L2.place(x=300,y=340)


 #head label
h=Label(window,text="Email OTP Verification",width=0,height=0,font=("comic sans ms",20,"bold"))
h.config(bg="white",fg="Black")
h.place(x=190,y=20)

 #head label
h=Label(window,text="Developed By Narayan Bhadaniya 📩",width=0,height=0,font=("comic sans ms",20,"bold"))
h.config(bg="skyblue",fg="Black")
h.place(x=100,y=400)

window.mainloop()
