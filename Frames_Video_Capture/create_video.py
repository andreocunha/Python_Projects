import cv2
import numpy as np
import glob
 
img_array = []
for filename in glob.glob('./Frames/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter('video.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 10, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()