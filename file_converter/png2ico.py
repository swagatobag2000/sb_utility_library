import os
from PIL import Image

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