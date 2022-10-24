#!/usr/bin/python
from PIL import Image
import os, sys
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

path = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/DR/DR/3/"
dirs = os.listdir( path )
path2 = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/03/"
def resize():

    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path2+item)
            imResize = im.resize((256,256), Image.ANTIALIAS)
            imResize.save(f + '.JPEG', quality=90)

resize()
