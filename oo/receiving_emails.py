import imaplib
import my_email
import pdb
import email


M = imaplib.IMAP4_SSL('outlook.office365.com')
login = M.login(my_email.email,my_email.password)
print(login)

M.select('inbox')

typ, data = M.search(None,'SUBJECT "subject"')
email_id = data
print(typ, data[0][0])
import imaplib
import my_email
import pdb
M = imaplib.IMAP4_SSL('outlook.office365.com')
login = M.login(my_email.email,my_email.password)
print(login)
# M.select especfica a categoria do email que quer como inbox/enviado/span
M.select('inbox')
# M.search procura um termo em alguma parte do texto como o exemplo que é pythonfans no titulo do email
typ, data = M.search(None,'SUBJECT "pythonfans"')
email_id = data[0]
print(typ, data)
result, email_data = M.fetch(email_id, '(RFC822)')
# essa parte é pra decodificar e printar o email que queremos
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')
email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():

    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)

pdb.set_trace()
