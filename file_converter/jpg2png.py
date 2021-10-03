import os
from PIL import Image

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