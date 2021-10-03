import PyPDF2
import os

def pdf2text(pdfPath, txtFileName = None):
    try:
        textPath = ""
        if txtFileName == None:
            textPath = os.path.normpath(pdfPath).replace(".pdf", "")+".txt"
        else:
            textPath = os.path.dirname(pdfPath)+"\\"+txtFileName+".txt"

        pdfobj = open(pdfPath, 'rb')
        pdfread = PyPDF2.PdfFileReader(pdfobj)

        pages, words = pdfread.numPages, 0
        
        for i in range(pages):
            pageObj = pdfread.getPage(i)
            with open(textPath, 'a+') as f: 
                f.write(pageObj.extractText() + "\n\n")
            for w in pageObj.extractText().split("\n"):
                words += len(w.split())
                            
        pdfobj.close()  
        print(f"Number of Pages: {pages}\nTotal Words: {words}")
    except Exception as e:
        print("Exception: " + str(type(e)) +" "+ str(e))
        print("1. Check the File Extension.")
        print("2. Check the Directory you entered.")
