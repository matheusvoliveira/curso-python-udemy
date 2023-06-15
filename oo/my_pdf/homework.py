import PyPDF4
import pdb
import re

with open('Find_the_Phone_Number.pdf', 'rb') as f:
    pdf_reader = PyPDF4.PdfFileReader(f)

all_text = ''
for n in range(pdf_reader.numPages):
    pages = pdf_reader.getPage(n)
    pages_text = pages.extractText()

    # all_text = all_text+' '+pages_text
# print(all_text)
#
# phone = re.search(r'\d{3}', all_text)
# print(phone)

