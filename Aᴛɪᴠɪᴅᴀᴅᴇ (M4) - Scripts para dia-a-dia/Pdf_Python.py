import PyPDF2


pdfFileObj = open ( 'ParticulaDinamica.pdf', 'rb') #Abrir o arquivo de pdf e armazenalo na variavel
pdfReader = PyPDF2.PdfFileReader (pdfFileObj)   #Fazendo a leitura por meio de função da bbl pypdf2


pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):  # Fazendo a Leitura pra copiar 
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)


pdfOutputFile = open('testandoPDF.pdf', 'wb')  #Criando um novo Pdf
pdfWriter.write(pdfOutputFile)          #Escrevendo no novo Pdf
pdfOutputFile.close()           #Fechando o novo PDF
    
