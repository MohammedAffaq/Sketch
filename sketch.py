import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "image.jpg"
def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])
#it is a 2 dimensional array formula to convert image to gray

def dodge(front,back):
    final_sketch = front*255/(255-back)
    #if image is greater than 255 is there , it will convert it to 255
    final_sketch[final_sketch>255]=255
    final_sketch[back==255]=255
    #to convert any suitable existing column to categorical type we use aspect function
    return final_sketch.astype('uint8')
    # here uint is for 8 bit signed integer 

ss = imageio.imread(img)   #to read the given image
gray = rgb2gray(ss)   # image is converted to gray scale
i=255-gray  # 0,0,0 is for the darkest colour and 255,255,255 is for the brightest colour which is white

blur= scipy.ndimage.filters.gaussian_filter(i,sigma=15) # it convert it into blur image 
#sigma is the intensity of blurness of image  
r= dodge(blur,gray)  # this function convert our image to sketch by taking 2 parameters as blur and gray

cv2.imwrite('image-sketch.png',r)