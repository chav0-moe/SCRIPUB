import potrace
from potrace import POTRACE_CORNER, Path
from PIL import Image

class raw_img():
    def __init__(self, bool_trace, img, colour): 
        self.bool_trace = bool_trace                #Determines whether the image should be traced or not
        self.img = img
        self.colour = colour                        #Original colour of image, only applies to images that need to be vectorized (bool_trace = True)
        
    def get_path(self):                             #Runs the Potrace vectorization algorithm, produces a Path object
        img_bmp = potrace.Bitmap(self.img)          #Creates Bitmap object, where the image is in greyscale format
        img_path = img_bmp.trace()
        #print('Img traced')
        self.path = img_path