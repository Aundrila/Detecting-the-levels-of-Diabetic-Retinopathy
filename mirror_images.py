from PIL import Image
import os, sys
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from timeit import default_timer as timer


def flip_image():
	cnt=0
	path = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/00/"
	dirs = os.listdir( path )
	path2 = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/mirror0/"
	for item in dirs:
		if os.path.isfile(path+item):
		    image_obj = Image.open(path+item)
		    f, e = os.path.splitext(path2+item)
		    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
		    rotated_image.save(f + '_m.JPEG')
		    cnt=cnt+1
		    print(cnt, end="")
		    print(": Succeeded Mirroring Image %s " % path+item)
	
	path = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/01/"
	dirs = os.listdir( path )
	path2 = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/mirror1/"
	for item in dirs:
		if os.path.isfile(path+item):
		    image_obj = Image.open(path+item)
		    f, e = os.path.splitext(path2+item)
		    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
		    rotated_image.save(f + '_m.JPEG')
		    cnt=cnt+1
		    print(cnt, end="")
		    print(": Succeeded Mirroring Image %s " % path+item)
	
	path = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/02/"
	dirs = os.listdir( path )
	path2 = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/mirror2/"
	for item in dirs:
		if os.path.isfile(path+item):
		    image_obj = Image.open(path+item)
		    f, e = os.path.splitext(path2+item)
		    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
		    rotated_image.save(f + '_m.JPEG')
		    cnt=cnt+1
		    print(cnt, end="")
		    print(": Succeeded Mirroring Image %s " % path+item)
	
	path = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/03/"
	dirs = os.listdir( path )
	path2 = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/mirror3/"
	for item in dirs:
		if os.path.isfile(path+item):
		    image_obj = Image.open(path+item)
		    f, e = os.path.splitext(path2+item)
		    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
		    rotated_image.save(f + '_m.JPEG')
		    cnt=cnt+1
		    print(cnt, end="")
		    print(": Succeeded Mirroring Image %s " % path+item)

	path = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/04/"
	dirs = os.listdir( path )
	path2 = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/mirror4/"
	for item in dirs:
		if os.path.isfile(path+item):
		    image_obj = Image.open(path+item)
		    f, e = os.path.splitext(path2+item)
		    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
		    rotated_image.save(f + '_m.JPEG')
		    cnt=cnt+1
		    print(cnt, end="")
		    print(": Succeeded Mirroring Image %s " % path+item)

start = timer()
flip_image()
end = timer() - start
print("Time = %f seconds" %end)
