import imaplib
import my_email
import pdb
M = imaplib.IMAP4_SSL('outlook.office365.com')
login = M.login(my_email.email,my_email.password)
print(login)

M.select('inbox')

# typ, data = M.search(None,'SUBJECT "subject"')
# email_id = data
# result, email_data = M.fetch(email_id,'(RCFC22)')
# pdb.set_trace()