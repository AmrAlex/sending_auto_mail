from exchangelib import DELEGATE,Credentials,Configuration, Account, Message, FileAttachment, HTMLBody,NTLM
import os
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
username = 'user name'
password = 'password'
url = 'company url'
email = 'mail '
body='''
                Dear All, </br></br>
                                                            kindly find attached dashboard_files.</br>
                                                            </br>
                                                            BR,</br>
                                                            Amr Ahmed.</br>
                '''

mainPath=os.path.dirname(os.path.abspath(__file__))
mainPath=mainPath+'/input/vas'
attached_file=[]
for filename in os.listdir(mainPath):
    i=filename
    attached=os.path.join(mainPath,i)
    attached_file.append(attached)
def send(filename=None,body=body):
    filename = [] if filename is None else filename
    # print(filename)
    # Recipients
    TO =["amr.ahmed.mostafa17@gmail.com"]
    CC = ["amr.ahmed.mostafa17@gmail.com"]
    BCC = []
    # Email
    subject = "Dash_Board_Files"
    
    attach = attached_file # attach file

    try:
        BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter
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



send()