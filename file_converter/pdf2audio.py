import os
import PyPDF2
import pyttsx3

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

pdf2audio(r'C:\Users\Swagato\Downloads\sample.pdf', "opp", "male",)