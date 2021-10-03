import os
from PIL import Image

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