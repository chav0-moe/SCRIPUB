#import numpy as np
import potrace
from potrace import POTRACE_CORNER, Path
from PIL import Image

class raw_img():
    def __init__(self, bool_trace, img, colour): 
        self.bool_trace = bool_trace
        self.img = img
        self.colour = colour
        
          
    def get_path(self):
        #width, height = self.img.size
        #self.img = self.img.resize((width*3, height*3))
        img_bmp = potrace.Bitmap(self.img)
        img_path = img_bmp.trace()
        #print('Img traced')
        self.path = img_path