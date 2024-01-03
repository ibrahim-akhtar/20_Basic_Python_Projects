# Project 01
# Email Sender

from email.message import EmailMessage
import ssl
import smtplib

email_sender = '<email>'
email_password = '<password>'
#To get the email and password for the python
#1. go to your gmail account
#2. click on security (will be there on left hand side)
#3. scroll under it and "on" the 2-step verification
#4. after switching it on (or if its already on) the go app passwords which will be in the same section
#5. will ask you to login again (by providing your actual email and pd)
#6. after logging in it will redirect you to window and at the bottom you'll see a drop down menu of 'select app'
#7. click on it and select option - "other" and give it a name say "Python"
#8. after that click on generate
#9. then it will give you the app password, copy paste it in line 9
#10. and then click on done

email_receiver = '<email>'
# if you have another email great if not go to this website and create a temp email
# https://temp-mail.org/en/ and it will generate you a temp email
# now copy the address and paste it in line 22

subject = 'This is the subject of the mail'
body = """
And this here is the body/content of the mail
"""

em = EmailMessage()     #instance created
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())     #converts the instance em to string

#run the code, if you dont get any error - means that it worked
#go the temp mail website and refresh the inbox (not the tab)
#there should be a message by you