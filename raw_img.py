#import numpy as np
import potrace
from potrace import POTRACE_CORNER, Path
from PIL import Image

class raw_img():
    def __init__(self, bool_trace, img, colour): 
        self.bool_trace = bool_trace
        self.img = img
        self.colour = colour
        #self.path = vect_img.get_path(img)
    
    #@classmethod                            
    #def get_path(self, img):
        #img_bmp = potrace.Bitmap(img)
        #img_path = img_bmp.trace()
        #print('Img traced')
        #return img_path
        
          
    def get_path(self):
        img_bmp = potrace.Bitmap(self.img)
        img_path = img_bmp.trace()
        print('Img traced')
        self.path = img_path