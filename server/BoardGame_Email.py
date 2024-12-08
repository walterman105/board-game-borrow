import os           #for sending mail
import smtplib      #for sending mail

import email        #for receiving mail
import imaplib      #for receiving mail

from email.message import EmailMessage      #for sending mail


class Email:
    def __init__(self):

        email_id='board.game.borrow.app@gmail.com'
        email_pass='tgxc reor gudt bhhr'

    def send_request(data):

        email_id='board.game.borrow.app@gmail.com'
        email_pass='tgxc reor gudt bhhr'

        user = data
        
        recipiants = "lexrichter@gmail.com"       #Email id of the recipiant

        to = [f"{recipiants}"]          

        sub = "BOARDGAMEBORROW Game request"       #Subject of the mail

        a = f"{user} has requested to borrow a game from you. Please login to the BOARDGAMEBORROW app to accept or reject the request."       #Body of the mail

        for i in to:
            
            msg=EmailMessage()
            msg['Subject']= sub
            msg['From']=email_id
            msg['To']= i
            msg.set_content(a)

        with smtplib.SMTP_SSL('smtp.gmail.com',465)as smtp:
                smtp.login(email_id,email_pass)
                smtp.send_message(msg)
                smtp.quit()

    def receive_email():

        sbjectfind = input("Enter the subject of the mail you want to search: ")       #Subject of the mail you want to search

        SERVER = 'imap.gmail.com'

        mail = imaplib.IMAP4_SSL(SERVER)
        mail.login(email_id, email_pass)
        mail.select('inbox')
        status, data = mail.search(None, 'ALL')
        mail_ids = []
        for block in data:
            mail_ids += block.split()

        for i in mail_ids:
            status, data = mail.fetch(i, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    message = email.message_from_bytes(response_part[1])
                    mail_from = message['from']
                    mail_subject = message['subject']
                    if message.is_multipart():
                        mail_content = ''

                        for part in message.get_payload():
                            if part.get_content_type() == 'text/plain':
                                mail_content += part.get_payload()
                    else:
                        mail_content = message.get_payload()
                    print(f'From: {mail_from}')
                    print(f'Subject: {mail_subject}')
                    print(f'Content: {mail_content}')

    # while True:
    #     print("1. Send an email")
    #     print("2. Receive an email")
    #     print("3. Exit")
    #     choice = int(input("Enter your choice: "))

    #     if choice == 1:
    #         send_email()
    #     elif choice == 2:
    #         receive_email()
    #     elif choice == 3:
    #         break
    #     else:
    #         print("Invalid choice. Please try again.")