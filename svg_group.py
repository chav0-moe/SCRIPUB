import numpy as np
import potrace
class svg_group():
    
    def __init__(self, png_group): 
        self.png_list = png_group
        svg_array = []
        for x in png_list.get_size():
            #print(x)
            svg_array[x] = svg_group.vectorize(png_group.getimage(x))
            #populate svg array with vectorized images
    
    @classmethod
    def make_bmp(img):
        img_bmp = potrace.Bitmap(img.data)
        return img_bmp
    
    @classmethod
    def vectorize(png):
        
        #img_svg = svg_single()
    #get data from png_single and convert it into newdata
        img_svg = svg_single(newdata)
        return img_svg
    
    def get_size():
        return len(svg_array)
    
    def get_image(x):
        return svg_array[x]