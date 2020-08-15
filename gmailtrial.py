import smtplib,ssl
smtp_server='smtp.gmail.com'
port=465
sender='ajay724sabareesh@gmail.com'
receiver='krishnaranganathan4@gmail.com'
message="""it works bitch """
password=input("enter your password")
context=ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(sender,password)
    server.sendmail(sender,receiver,message)    
