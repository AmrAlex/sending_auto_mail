from exchangelib import DELEGATE,Credentials,Configuration, Account, CalendarItem, Message, Mailbox, FileAttachment, HTMLBody,NTLM, GSSAPI, SSPI
import re
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
import os,sys
import getpass
username = 'user_name'
password = 'passwor'
url = 'company url'
email = 'mail'

class EmailSender:
    
    @staticmethod 
    def send(filename=None,body=""):
        filename = [] if filename is None else filename
       # print(filename)
       # Recipients
        TO = ['amr.ahmed.mostafa17@gmail.com']
        CC = ['amr.ahmed.mostafa17@gmail.com']
        BCC = []
        # Email
        subject = "CTC CallSR"
        
        attach = filename # attach file

        try:
            credentials = Credentials(username, password )
            config = Configuration(service_endpoint=url, credentials=credentials, auth_type=NTLM)
            account = Account(email, credentials=credentials, autodiscover=False, config=config)

            m = Message(
                account=account,
                subject=subject,
                body=HTMLBody(body),
                to_recipients=TO,
                cc_recipients=CC,  
                bcc_recipients=BCC,  
            )


            if len(attach)>0:
                for f in attach:
                    for f in attach:
                        with open(f,'rb') as fil:
                            file = FileAttachment(name=os.path.basename(f), content=fil.read())
                            m.attach(file)

            m.send()
        except Exception as ex:
            print("Failed to send mail")
            print(ex)
        else:
            print("Successfully sent email")



