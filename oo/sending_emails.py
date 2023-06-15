import smtplib
import pdb
import getpass
import my_email
import smtplib
from email.mime.text import MIMEText
import my_email
# faz o chamado o link varia de provedor gmail/yahoo/outlook
smtp_object = smtplib.SMTP('smtp.office365.com',587)
smtp_object.ehlo()

#loga na conta com email e senha
smtp_object.starttls()
email = my_email.email
smtp_object.login(email, my_email.password)

# from_adress = email
# to_adress = email
# subject = input('Enter the subject: ')
# message = input('Enter the message: ')
# msg = 'Subject: '+subject+'\n'+message
#
# smtp_object.sendmail(from_adress,to_adress,msg)
# smtp_object.quit()
#aqui especificamos o assunto e a mensagem que queremos
from_address = email
to_address = email
subject = input('Enter the subject: ')
message = input('Enter the message: ')

msg = MIMEText(message)
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = subject
#aqui onde finaliza o processo enviando o email
smtp_object.send_message(msg)
smtp_object.quit()
pdb.set_trace()