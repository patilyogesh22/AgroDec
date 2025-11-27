
'''
import smtplib

sender = "darkknightrise2023@gmail.com"
receiver = "narayanbhadaniya14@gmail.com"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
    server.login("d190ff01517766", "20cffafcfc6b46")
    server.sendmail(sender, receiver, message)
    print("Mail Sended Succesfully")
'''


'''import base64
from pathlib import Path

import mailtrap as mt

welcome_image = Path(__file__).parent.joinpath("welcome.png").read_bytes()

mail = mt.Mail(
    sender=mt.Address(email="mailtrap@example.com", name="Mailtrap Test"),
    to=[mt.Address(email="your@email.com", name="Your name")],
    cc=[mt.Address(email="cc@email.com", name="Copy to")],
    bcc=[mt.Address(email="bcc@email.com", name="Hidden Recipient")],
    subject="You are awesome!",
    text="Congrats for sending test email with Mailtrap!",
    html="""
    <!doctype html>
    <html>
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
      </head>
      <body style="font-family: sans-serif;">
        <div style="display: block; margin: auto; max-width: 600px;" class="main">
          <h1 style="font-size: 18px; font-weight: bold; margin-top: 20px">
            Congrats for sending test email with Mailtrap!
          </h1>
          <p>Inspect it using the tabs you see above and learn how this email can be improved.</p>
          <img alt="Inspect with Tabs" src="cid:welcome.png" style="width: 100%;">
          <p>Now send your email using our fake SMTP server and integration of your choice!</p>
          <p>Good luck! Hope it works.</p>
        </div>
        <!-- Example of invalid for email html/css, will be detected by Mailtrap: -->
        <style>
          .main { background-color: white; }
          a:hover { border-left-width: 1em; min-height: 2em; }
        </style>
      </body>
    </html>
    """,
    category="Test",
    attachments=[
        mt.Attachment(
            content=base64.b64encode(welcome_image),
            filename="welcome.png",
            disposition=mt.Disposition.INLINE,
            mimetype="image/png",
            content_id="welcome.png",
        )
    ],
    headers={"X-MT-Header": "Custom header"},
    custom_variables={"year": 2023},
)

client = mt.MailtrapClient(token="your-api-key")
client.send(mail)
'''


'''
import smtplib
content="Hello World"
mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
sender='darkknightrise2023@gmail.com'
recipient='narayanbhadaniya14@gmail.com'
mail.login('darkknightrise2023@gmail.com','DarkKnight@23')
header='To:'+receipient+'\n'+'From:' \
+sender+'\n'+'subject:testmail\n'
content=header+content
mail.sendmail(sender, recipient, content)
mail.close()
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_mail(subject, body, to, gmail_user, gmail_password, attachments=None):
    try:
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = to
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'html'))

        if attachments:
            for attachment in attachments:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(open(attachment, 'rb').read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(attachment.split("/")[-1]))
                msg.attach(part)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to, msg.as_string())
        server.close()

        print ('Email sent!')
    except Exception as e:
        print ('Something went wrong...', e)

subject = "Subject of the email"
body = "Body of the email"
to = ["darkknightrise2023@gmail.com"]
gmail_user = "narayanbhadaniya14@gmail.com"
gmail_password = "hjwn kkag mzlv eojk"
attachments = ["C:/Users/niran/OneDrive/Desktop/python.txt", "C:/Users/niran/OneDrive/Desktop/python.txt"]

send_mail(subject, body, to, gmail_user, gmail_password, attachments)

