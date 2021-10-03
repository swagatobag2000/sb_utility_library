import os
import json
import PyPDF2
import pyttsx3
import img2pdf
from PIL import Image

def ico2png(imagePath, newImagePath = None):
    try:
        if newImagePath == None:
            if ".PNG" in imagePath:
                newImagePath = os.path.normpath(imagePath).replace(".ICO", "")+".png"
            elif ".png" in imagePath:
                newImagePath = os.path.normpath(imagePath).replace(".ico", "")+".png"
        else:
            newImagePath = os.path.dirname(imagePath)+"\\"+newImagePath+".png"
        img = Image.open(imagePath)
        img.save(newImagePath, "png")
    except Exception as e:
        print("Exception: " + str(type(e)) +" "+ str(e))
        print("1. Check the File Extension.")
        print("2. Check the Directory you entered.")

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

def jpg2png(imagePath, newImagePath = None):
    try:
        if newImagePath == None:
            if ".JPG" in imagePath:
                newImagePath = os.path.normpath(imagePath).replace(".JPG", "")+".png"
            elif ".jpg" in imagePath:
                newImagePath = os.path.normpath(imagePath).replace(".jpg", "")+".png"
        else:
            newImagePath = os.path.dirname(imagePath)+"\\"+newImagePath+".png"
        img = Image.open(imagePath).convert("RGB")
        img.save(newImagePath, "png")
    except Exception as e:
        print("Exception: " + str(type(e)) +" "+ str(e))
        print("1. Check the File Extension.")
        print("2. Check the Directory you entered.")

def json2csv(jsonPath, fileName = None):
    try:
        filePath = ""
        filePath = os.path.dirname(jsonPath)+"\\output.csv" if fileName == None else os.path.dirname(jsonPath)+ "\\" + fileName + ".csv"

        with open(jsonPath, 'r') as f:
            data = json.loads(f.read())

        output = ','.join([*data[0]])
        keys = output.split(",")

        for obj in data:
            if list(obj.keys()) != keys:
                raise ValueError("JSON does not contain same set of keys. Cannot convert to CSV")

        for obj in data:
            output += f'\n'
            for key in keys:
                output += f'{obj[key]},'
            output = output[:-1]

        with open(filePath, 'w') as f:
            f.write(output)

    except ValueError as v:
        print("Exception: " + str(type(v)) +" "+ str(v))
        print("1. Check the File Extension.")
        print("2. Check the Directory you entered.")
    except Exception as e:
        print("Exception: " + str(type(e)) +" "+ str(e))
        print("1. Check the File Extension.")
        print("2. Check the Directory you entered.")

def pdf2audio(pdfPath, fileName = None, gen = "male"):
    try:
        filePath = os.path.dirname(pdfPath)+"\\output.mp3" if fileName == None else os.path.dirname(pdfPath)+ "\\" + fileName + ".mp3"
        pdfReader = PyPDF2.PdfFileReader(open(pdfPath, 'rb'))
        gender = 0 if gen.lower() == "male" else 1 if gen.lower() == "female" else None
        
        speaker = pyttsx3.init()
        speaker.setProperty('rate', 150)
        speaker.setProperty('volume', 1.0)
        speaker.setProperty('voice', speaker.getProperty('voices')[gender].id)

        print("Current Speaking Rate: ", speaker.getProperty('rate'))
        print("Current Volume: ", speaker.getProperty('volume'))
        print("Current Voice: ", gen)

        for page in range(pdfReader.numPages):
            text =  pdfReader.getPage(page).extractText()
            # speaker.say(text)
            speaker.runAndWait()
        speaker.stop()

        speaker.save_to_file(text, filePath)
        speaker.runAndWait()

    except Exception as e:
        print("Exception: " + str(type(e)) +" "+ str(e))
        print("1. Check the File Extension.")
        print("2. Check the Directory you entered.")

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

def png2ico(imagePath, newImagePath = None):
    try:
        if newImagePath == None:
            if ".PNG" in imagePath:
                newImagePath = os.path.normpath(imagePath).replace(".PNG", "")+".ico"
            elif ".png" in imagePath:
                newImagePath = os.path.normpath(imagePath).replace(".png", "")+".ico"
        else:
            newImagePath = os.path.dirname(imagePath)+"\\"+newImagePath+".ico"
        img = Image.open(imagePath)
        img.save(newImagePath, "ico")
    except Exception as e:
        print("Exception: " + str(type(e)) +" "+ str(e))
        print("1. Check the File Extension.")
        print("2. Check the Directory you entered.")

def jpg2png(imagePath, newImagePath = None):
    try:
        if newImagePath == None:
            if ".PNG" in imagePath:
                newImagePath = os.path.normpath(imagePath).replace(".PNG", "")+".jpeg"
            elif ".png" in imagePath:
                newImagePath = os.path.normpath(imagePath).replace(".png", "")+".jpeg"
        else:
            newImagePath = os.path.dirname(imagePath)+"\\"+newImagePath+".jpeg"
        img = Image.open(imagePath).convert("RGB")
        img.save(newImagePath, "jpeg")
    except Exception as e:
        print("Exception: " + str(type(e)) +" "+ str(e))
        print("1. Check the File Extension.")
        print("2. Check the Directory you entered.")