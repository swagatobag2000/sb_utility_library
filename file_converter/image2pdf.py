import os
import img2pdf

def image2pdf(imagePath, fileName = None):
    try:
        filePath = ""
        filePath = os.path.dirname(imagePath)+"\\output.pdf" if fileName == None else os.path.dirname(imagePath)+ "\\" + fileName + ".pdf"

        with open(filePath, "wb") as f:
            f.write(img2pdf.convert(imagePath))
                
    except Exception as e:
        print("Exception: " + str(type(e)) +" "+ str(e))
        print("1. Check the File Extension.")
        print("2. Check the Directory you entered.")