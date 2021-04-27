import smtplib
import json

f = open( "credential.json", 'r')

cred_data = json.load(f)
sender_email = cred_data["email"]
sender_email_password = cred_data["password"]

print(F"{sender_email}\n{sender_email_password}")

server = smtplib.SMTP('smtp.gmail.com', 587)
server. starttls()
server.login(sender_email,sender_email_password)

reciever = "amanverma03328@gmail.com"
message = "This is a trial message. If you see it hoorra your basic python email bot is complete."

server.sendmail(sender_email, reciever, message)

f.close()
