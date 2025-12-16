import mysql.connector
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont
from PIL import Image,ImageTk
import os
import qrcode
from io import BytesIO
from tkinter import filedialog
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Replace the below details with your actual MySQL details
mysql_details = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'agrodec'
}

def get_student_data(Enroll):
    cnx = mysql.connector.connect(**mysql_details)
    cursor = cnx.cursor()
    query = "SELECT Enroll, Name, Mobile, Address, Email, Adhar, Gender, validity FROM student WHERE Enroll = %s"
    cursor.execute(query, (Enroll,))
    result = cursor.fetchone()
    cursor.close()
    cnx.close()
    return result


def generate_pass(student_data,Enroll):
    image = Image.open('D:/Bus Pass/Image/Pass.png') # Replace with the path to your template image
    draw = ImageDraw.Draw(image)

    # Draw college logo
    college_logo = Image.open('D:/Bus Pass/Image/medilogo.png') # Replace with the path to your college logo image
    image.paste(college_logo, (5,5))

    # Draw Profile pic
    profile = Image.open(f'D:/Bus Pass/Profile/{Enroll}.png') # Replace with the path to your college logo image
    image.paste(profile, (10,150))


    # Write college name
    font = ImageFont.truetype('comic.ttf', 30)
    draw.text((190, 10), "MEDI-CAPS STUDENT BUS PASS", font=font,fill='red')
    draw.text((180, 18), "____________________________", font=font,fill='red')
    draw.text((180, 50), "MEDI-CAPS UNIVERSITY, INDORE", font=font,fill='red')

    # Write student name, enrollment no., branch, etc.
    # Modify this according to your actual data fields
    for i, field in enumerate(('Enroll', 'Name', 'Mobile', 'Address', 'Email', 'Adhar', 'Gender','Session')):
        font = ImageFont.truetype('comic.ttf', 20)
        draw.text((190, 100 + i * 30), f'{field}: {student_data[i]}', font=font,fill='black')

   

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=6,
        border=4,
    )
    qr.add_data(student_data[0]) # Assuming QR Verify Code is the 11th data field
    qr.make(fit=True)
    img_qr = qr.make_image(fill_color="black", back_color="white")
    image.paste(img_qr, (560, 120))

     #scan now
    font = ImageFont.truetype('comic.ttf', 20)
    draw.text((600, 105), "Scan Now", font=font,fill='black')

    # Draw registerar sign logo
    font = ImageFont.truetype('comic.ttf', 25)
    draw.text((590, 320), "Registrar", font=font,fill='black')
    registerar_sign = Image.open('D:/Bus Pass/Image/sign.png') # Replace with the path to your registerar sign logo image
    image.paste(registerar_sign, (590, 295))

    # Save the image
   # image.save('C:/Users/niran/OneDrive/Desktop/Bus Pass/Pass'+ '{student_data[0]}.png')
    image.save('D:/Bus Pass/Pass/' + student_data[0] + '.png')
    
def send_mail(target_email,photo_attachment):
    # login credentials
    email = "yogeshpatil22@gmail.com"
    password = "Great@12345"

    # target email address
    #target_email = "darkknightrise2023@gmail.com"

    # email content
    subject = "Your Bus Buss is Generated SuccesFully"
    message = "Your Bus Pass is Here"

    # photo attachment
    #photo_attachment = filedialog.askopenfilename()

    # prepare the email
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = target_email
    msg['Subject'] = subject

    # attach the message
    msg.attach(MIMEText(message, 'plain'))

    # open the file in binary mode
    with open(photo_attachment, 'rb') as attachment:
        # add the attachment
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)

        # define the attachment's filename
        part.add_header('Content-Disposition', f'attachment; filename={photo_attachment}')

        # attach the attachment
        msg.attach(part)
        messagebox.showinfo("BUS PASS Mailed", "BUS PASS MAILED UCCESSFULLY")

    # create the server and send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, target_email, msg.as_string())
    server.quit()

def mail(enrollment_no=None):
    if enrollment_no is None:
        Enroll = name.get()
        enrollment_no = Enroll

    image_path = f"Pass\\{enrollment_no}.png"
    recipients = f"{enrollment_no}+@medicaps.ac.in"
    send_mail(recipients, image_path)

def generate_bus_pass():
    Enroll = name.get()
    student_data = get_student_data(Enroll)
    if student_data:
        generate_pass(student_data,Enroll)
        messagebox.showinfo("BUS PASS GENERATED", "BUS PASS GENERATED SUCCESSFULLY")
        
    else:
        messagebox.showinfo("BUS PASS ERROR",f'No student found with enrollment no {Enroll}')

# Example usage
window=tk.Tk()
window.title("Medi-Caps Bus Pass Generate")
window.config(bg="skyblue")
w=window.winfo_screenwidth()-800
h=window.winfo_screenheight()-400
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
wpos=(sw/2)-(w/2)
hpos=(sh/2)-(h/2)
window.geometry("%dx%d+%d+%d"%(w,h,wpos,hpos))


bg=ImageTk.PhotoImage(file="Image\\Medilogin.png")
bg=Label(window,image=bg)
bg.place(x=-2,y=-3)

l1=Label(window,text="GENERATE BUS PASS",font=("comic sans ms",18,"bold"))    
l1.place(x=240,y=10)

#label
nameL=Label(window,text="Enter Enrollment No:",width=0,height=0,font=("comic sans ms",20,"bold"))
nameL.config(bg="Black",fg="White")
nameL.place(x=200,y=150)

#entry
var1=StringVar()
name=Entry(window,textvariable=var1,width=25,font=("comic sans ms",18,"bold"))
#var1.set("EN21CS304068")
name.config(bg="white",fg="black")
name.place(x=150,y=250)

#button
ok=Button(window,text="GENERATE",width=0,height=0,font=("comic sans ms",15,"bold"),command=generate_bus_pass)
ok.config(bg="white",fg="black")
ok.place(x=100,y=340)
can=Button(window,text="CANCEL",width=0,height=0,font=("comic sans ms",15,"bold"),command=window.destroy)
can.config(bg="white",fg="black")
can.place(x=530,y=340)
ok=Button(window,text="GENERATE AND MAIL",width=0,height=0,font=("comic sans ms",15,"bold"),command=mail)
ok.config(bg="white",fg="black")
ok.place(x=250,y=340)

window.mainloop()

