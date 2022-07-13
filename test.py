import potrace
import numpy
from numpy import asarray
from PIL import Image

#Get image
img = Image.open('Complex_Contour.png')

#Convert image to greyscale
img_grey = img.convert('L')

#Get numpy array from image
data = asarray(img_grey)

#Convert to bitmap with potrace function
bmp = Bitmap(data) #--This line is causing the error, perhaps because the numpy array input is not of the correct format

#Reconstruct image from numpy array
#pilImage = Image.fromarray(data)
#pilImage = pilImage.save('check.png')

#Trace bitmap for vectorization
path = bmp.trace()
