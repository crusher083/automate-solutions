import PyPDF2

with open('dictionary.txt', 'r') as f:
    d = [line.rstrip() for line in f]
pdfFileObj = open('allminutes_encrypted.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(pdfFileObj)
d.append('SWORDFISH')
if pdf.isEncrypted:
    for w in d:
        if pdf.decrypt(w):
            print(f"Done! Password is {w}")
            break
        elif pdf.decrypt(w.lower()):
            print(f"Done! Password is {w.lower()}")
            break
    if pdf.isEncrypted:
        print('Pass not found!')
else:
    print('Pass not needed!')
