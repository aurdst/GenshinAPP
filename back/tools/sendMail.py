import tkinter as tk
import smtplib

import os
from dotenv import load_dotenv

import socket
socket.getaddrinfo('127.0.0.1', 8080)

def send_mail():
    smtp_serv = os.getenv('EMAIL_HOST', "smtp.office365.com") 
    smtp_port =  os.getenv('EMAIL_PORT', "587") 
    smtp_pass = os.getenv('EMAIL_HOST_PASSWORD', "")
    smtp_username = os.getenv('EMAIL_SENDER', "aureliendestailleur@outlook.fr")


    #Adress of sender and recipent 
    sender = os.getenv('EMAIL_SENDER', "aureliendestailleur@outlook.fr")
    recipent = 'lefebvremaximee@gmail.com'

    #Mail content
    subject = "Test"
    body = "test test"

    #Connect of SMTP server and sending mail
    with smtplib.SMTP(smtp_serv, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_pass)
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail(sender, recipent, message)
        print("mail send")

window = tk.Tk()
button = tk.Button(window, text='Envoyer', command=send_mail)
button.pack()

window.mainloop()