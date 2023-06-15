import PyPDF4
import pdb


f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF4.PdfFileReader(f)
print(pdf_reader.numPages)

page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()

pdf_writer = PyPDF4.PdfFileWriter()
pdf_writer.addPage(page_one)

pdf_output = open('Some_BrandNew_Doc.pdf', 'wb')
pdf_writer.write(pdf_output)

f.close()
pdf_output.close()

f = open('Working_Business_Proposal.pdf','rb')

pdf_text = []
pdf_reader = PyPDF4.PdfFileReader(f)

for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    pdf_text.append(page.extractText())

print(pdf_text[1])
pdb.set_trace()