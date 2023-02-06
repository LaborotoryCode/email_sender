import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
#SSL port

password = input("Enter Your Password: ")
#Password for sender_email


sender_email = 'ayaanaanyajain@gmail.com'
receiver_emails = ['ayaan_jain@s2021.ssts.edu.sg']

message = """\
Subject: SMTP e-mail test

This is a test e-mail message sent via Python.
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
  #closes connection for security
  server.login(sender_email, password)
  #send email now
  server.sendmail(sender_email, receiver_emails, message)

print("Email sent")
