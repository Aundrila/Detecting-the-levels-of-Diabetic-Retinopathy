from PIL import Image
import os, sys
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True



def rotate():
	cnt = 0
	path = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/00/"
	dirs = os.listdir( path )
	path2 = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/rotate0_180/"
	for item in dirs:
		if os.path.isfile(path+item):
		    image_obj = Image.open(path+item)
		    f, e = os.path.splitext(path2+item)
		    rotated_image = image_obj.rotate(180)
		    rotated_image.save(f + '_180.JPEG')
		    cnt = cnt+1
		    print(cnt, end="")
		    print(": Succeeded Rotating 180° Image %s " % path+item)

	path = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/01/"
	dirs = os.listdir( path )
	path2 = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/rotate1_180/"
	for item in dirs:
		if os.path.isfile(path+item):
		    image_obj = Image.open(path+item)
		    f, e = os.path.splitext(path2+item)
		    rotated_image = image_obj.rotate(180)
		    rotated_image.save(f + '_180.JPEG')
		    cnt = cnt+1
		    print(cnt, end="")
		    print(": Succeeded Rotating 180° Image %s " % path+item)

	path = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/02/"
	dirs = os.listdir( path )
	path2 = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/rotate2_180/"
	for item in dirs:
		if os.path.isfile(path+item):
		    image_obj = Image.open(path+item)
		    f, e = os.path.splitext(path2+item)
		    rotated_image = image_obj.rotate(180)
		    rotated_image.save(f + '_180.JPEG')
		    cnt = cnt+1
		    print(cnt, end="")
		    print(": Succeeded Rotating 180° Image %s " % path+item)

	path = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/03/"
	dirs = os.listdir( path )
	path2 = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/rotate3_180/"
	for item in dirs:
		if os.path.isfile(path+item):
		    image_obj = Image.open(path+item)
		    f, e = os.path.splitext(path2+item)
		    rotated_image = image_obj.rotate(180)
		    rotated_image.save(f + '_180.JPEG')
		    cnt = cnt+1
		    print(cnt, end="")
		    print(": Succeeded Rotating 180° Image %s " % path+item)

	path = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/04/"
	dirs = os.listdir( path )
	path2 = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/rotate4_180/"
	for item in dirs:
		if os.path.isfile(path+item):
		    image_obj = Image.open(path+item)
		    f, e = os.path.splitext(path2+item)
		    rotated_image = image_obj.rotate(180)
		    rotated_image.save(f + '_180.JPEG')
		    cnt = cnt+1
		    print(cnt, end="")
		    print(": Succeeded Rotating 180° Image %s " % path+item)

rotate()
