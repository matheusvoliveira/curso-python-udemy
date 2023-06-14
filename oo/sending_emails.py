import smtplib
import pdb
import getpass
import my_email


smtp_object = smtplib.SMTP('smtp.office365.com',587)
smtp_object.ehlo()


smtp_object.starttls()
email = my_email.email
smtp_object.login(email, my_email.password)

pdb.set_trace()