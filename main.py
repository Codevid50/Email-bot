import smtplib
from email.message import EmailMessage
import json
import os
from datetime import datetime


file_name = 'email.json'

email_list = []

if os.path.exists(file_name):
    with open(file_name, 'r') as f:
        try:
            email_list = json.load(f)
        except json.JSONDecodeError:
            email_list = []

sender = input('Enter you Email:- ').strip()
app_password = input("Enter your email app password: ").strip()

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender, app_password)

while True:
    receiver = input('Enter receiver email:- ').strip()
    subject = input('Enter the Subject:- ').strip()
    message = input('Enter the message:- ').strip()

    if not receiver or not subject or not message:
        print("All fields are required.")
        continue

    email = EmailMessage()
    email['From'] = sender
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)

    

    server.send_message(email)
    print("---Email sent successfully--- \n")

    

    email_data = { 
            "receiver": receiver,
            "subject": subject,
            "message": message,
            "time": datetime.now().strftime("%H:%M:%S")
        }
    
    email_list.append(email_data)
    
    with open(file_name, 'w') as f:
        json.dump(email_list, f, indent=4)
    print('<---Email saved successfully--->')

    another_email = input('Do you want to send another email (yes/no):- ').strip().lower()
    if another_email == 'no':
        break
    
server.quit()
print('Program Ended')
