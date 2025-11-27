import tkinter as tk
from tkinter import filedialog
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_mail():
    # login credentials
    email = "narayanbhadaniya14@gmail.com"
    password = "hjwn kkag mzlv eojk"

    # target email address
    target_email = "darkknightrise2023@gmail.com"

    # email content
    subject = "Your Bus Buss is Generated SuccesFully"
    message = "Your Bus Pass is Here"

    # photo attachment
    photo_attachment = filedialog.askopenfilename()

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
        print("Mail Sended")

    # create the server and send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, target_email, msg.as_string())
    server.quit()

# create the application
app = tk.Tk()
app.title('Send Mail with Photo Attachment')

# create the widgets
'''
label_email = tk.Label(app, text='Email:')
label_password = tk.Label(app, text='Password:')
label_target_email = tk.Label(app, text='Target Email:')
label_subject = tk.Label(app, text='Subject:')
label_message = tk.Label(app, text='Message:')
'''

'''
entry_email = tk.Entry(app)
entry_password = tk.Entry(app, show='*')
entry_target_email = tk.Entry(app)
entry_subject = tk.Entry(app)
entry_message = tk.Entry(app)
'''

button_send = tk.Button(app, text='Send Mail', command=send_mail)

# grid the widgets
'''
label_email.grid(row=0, column=0)
label_password.grid(row=1, column=0)
label_target_email.grid(row=2, column=0)
label_subject.grid(row=3, column=0)
label_message.grid(row=4, column=0)

entry_email.grid(row=0, column=1)
entry_password.grid(row=1, column=1)
entry_target_email.grid(row=2, column=1)
entry_subject.grid(row=3, column=1)
entry_message.grid(row=4, column=1)
'''
button_send.grid(row=1, column=1)

# run the application
app.mainloop()
