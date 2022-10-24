from PIL import Image
import os, sys
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True



def rotate():
	cnt = 0
	path = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Try/04/"
	dirs = os.listdir( path )
	path2 = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Try/4/"
	for item in dirs:
		if os.path.isfile(path+item):
		    image_obj = Image.open(path+item)
		    f, e = os.path.splitext(path2+item)
		    rotated_image = image_obj.rotate(90)
		    rotated_image.save(f + '_90.JPEG')
		    cnt = cnt+1
		    print(cnt, end="")
		    print(": Succeeded Rotating 90° Image %s " % path+item)

	for item in dirs:
		if os.path.isfile(path+item):
		    image_obj = Image.open(path+item)
		    f, e = os.path.splitext(path2+item)
		    rotated_image = image_obj.rotate(180)
		    rotated_image.save(f + '_180.JPEG')
		    cnt = cnt+1
		    print(cnt, end="")
		    print(": Succeeded Rotating 180° Image %s " % path+item)
	for item in dirs:
		if os.path.isfile(path+item):
		    image_obj = Image.open(path+item)
		    f, e = os.path.splitext(path2+item)
		    rotated_image = image_obj.rotate(270)
		    rotated_image.save(f + '_270.JPEG')
		    cnt = cnt+1
		    print(cnt, end="")
		    print(": Succeeded Rotating 270° Image %s " % path+item)


rotate()
