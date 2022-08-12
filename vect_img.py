#import numpy as np
import potrace
from potrace import POTRACE_CORNER, Path
from PIL import Image

class vect_img():
    def __init__(self, img, colour): 
        self.img = img
        self.colour = colour
        self.path = vect_img.get_path(img)
    
    @classmethod
    def get_path(self, img):
        img_bmp = potrace.Bitmap(img)
        img_path = img_bmp.trace()
        print('Img traced')
        return img_path

    
        