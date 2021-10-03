import os
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