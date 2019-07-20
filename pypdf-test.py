import PyPDF2

pdfFileObj = open("VN2p_2012.pdf", "rb")

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage()

print pageObj.extractText()

pdfFileObj.close()