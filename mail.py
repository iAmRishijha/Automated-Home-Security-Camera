import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "rishi2382002@gmail.com"    
sender_password = "qgshsfinwgxwmsef"

recipient_email = ""
with open('email.txt', 'r') as file:
    recipient_email = file.read()
file.close()

email_server = "smtp.gmail.com"
port = 587

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = "Automated Security Camera"

body = "!! There is/are stranger(s) outside your house !!"
message.attach(MIMEText(body, 'plain'))

with smtplib.SMTP(email_server, port) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())

print("Email sent successfully.")
