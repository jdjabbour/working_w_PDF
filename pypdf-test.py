import PyPDF2

pdfFileObj = open("Employee Summary.pdf", "rb")

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage()

print pageObj.extractText()

pdfFileObj.close()