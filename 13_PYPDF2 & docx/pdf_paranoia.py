import PyPDF2
import os


def encrypt(path):
    pdf_wrt = PyPDF2.PdfFileWriter()
    for foldername, subfolder, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.pdf'):
                pdf = open(filename, 'rb')
                pdf_read = PyPDF2.PdfFileReader(pdf)
                for num in range(pdf_read.numPages):
                    page = pdf_read.getPage(num)
                    pdf_wrt.addPage(page)
                pdf_wrt.encrypt(input(f'Please input password for {filename}'))
                pdf_out = open(f'{filename[:-4]}' + '_encrypted.pdf', 'wb')
                pdf_wrt.write(pdf_out)


def decrypt(path, passw):
    suffix = '_encrypted.pdf'
    pdf_wrt = PyPDF2.PdfFileWriter()
    for foldername, subfolder, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(suffix):
                pdf = open(filename, 'rb')
                pdf_read = PyPDF2.PdfFileReader(pdf)
                if pdf_read.isEncrypted:
                    if pdf_read.decrypt(passw):
                        for num in range(pdf_read.numPages):
                            page = pdf_read.getPage(num)
                            pdf_wrt.addPage(page)
                            pdf_out = open(f'{filename[:-len(suffix)]}' + '_decrypt.pdf', 'wb')
                            pdf_wrt.write(pdf_out)
                    else:
                        print(f'{passw} is wrong for {filename}')
encrypt('D://Python')