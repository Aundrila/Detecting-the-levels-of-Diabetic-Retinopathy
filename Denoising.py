#!/usr/bin/python
from PIL import Image
import os, sys
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import numpy as np
import cv2
#from matplotlib import pyplot as plt
from timeit import default_timer as timer




def denoise():
	cnt=0
	path = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/rotate0_90/"
	dirs = os.listdir( path )
	path2 = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Re/0/"
	for item in dirs:
		if os.path.isfile(path + item):
			img = cv2.imread(path + item)
			b, g, r = cv2.split(img)  # get b,g,r
			rgb_img = cv2.merge([r, g, b])  # switch it to rgb

			# Denoising
			dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

			b, g, r = cv2.split(dst)  # get b,g,r
			rgb_dst = cv2.merge([r, g, b])  # switch it to rgb

			cv2.imwrite(path2 + item, dst)
			cnt=cnt+1
			print(cnt)
	path = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/rotate1_90/"
	dirs = os.listdir( path )
	path2 = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Re/1/"
	for item in dirs:
		if os.path.isfile(path + item):
			img = cv2.imread(path + item)
			b, g, r = cv2.split(img)  # get b,g,r
			rgb_img = cv2.merge([r, g, b])  # switch it to rgb

			# Denoising
			dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

			b, g, r = cv2.split(dst)  # get b,g,r
			rgb_dst = cv2.merge([r, g, b])  # switch it to rgb

			cv2.imwrite(path2 + item, dst)
			cnt=cnt+1
			print(cnt)

	path = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/rotate2_90/"
	dirs = os.listdir( path )
	path2 = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Re/2/"
	for item in dirs:
		if os.path.isfile(path + item):
			img = cv2.imread(path + item)
			b, g, r = cv2.split(img)  # get b,g,r
			rgb_img = cv2.merge([r, g, b])  # switch it to rgb

			# Denoising
			dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

			b, g, r = cv2.split(dst)  # get b,g,r
			rgb_dst = cv2.merge([r, g, b])  # switch it to rgb

			cv2.imwrite(path2 + item, dst)
			cnt=cnt+1
			print(cnt)

	path = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/rotate3_90/"
	dirs = os.listdir( path )
	path2 = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Re/3/"
	for item in dirs:
		if os.path.isfile(path + item):
			img = cv2.imread(path + item)
			b, g, r = cv2.split(img)  # get b,g,r
			rgb_img = cv2.merge([r, g, b])  # switch it to rgb

			# Denoising
			dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

			b, g, r = cv2.split(dst)  # get b,g,r
			rgb_dst = cv2.merge([r, g, b])  # switch it to rgb

			cv2.imwrite(path2 + item, dst)
			cnt=cnt+1
			print(cnt)

	path = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Newfolder/rotate4_90/"
	dirs = os.listdir( path )
	path2 = "/home/bitcoin/Downloads/Diabetic_Ratinopathy_Data/Re/4/"
	for item in dirs:
		if os.path.isfile(path + item):
			img = cv2.imread(path + item)
			b, g, r = cv2.split(img)  # get b,g,r
			rgb_img = cv2.merge([r, g, b])  # switch it to rgb

			# Denoising
			dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

			b, g, r = cv2.split(dst)  # get b,g,r
			rgb_dst = cv2.merge([r, g, b])  # switch it to rgb

			cv2.imwrite(path2 + item, dst)
			cnt=cnt+1
			print(cnt)
start = timer()
denoise()
end = timer() - start
print("%f seconds" %end)

#img = cv2.imread('H:/xampp/htdocs/DiabeticRetinopathy/new_images/img/12_right.jpeg')

#b,g,r = cv2.split(img)           # get b,g,r#
#rgb_img = cv2.merge([r,g,b])     # switch it to rgb

# Denoising
#dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

#b,g,r = cv2.split(dst)           # get b,g,r
#rgb_dst = cv2.merge([r,g,b])     # switch it to rgb

#cv2.imwrite("H:/xampp/htdocs/DiabeticRetinopathy/Denoised_Images/12_right_denoised.jpeg", dst)




			
