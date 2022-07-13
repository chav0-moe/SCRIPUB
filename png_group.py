#from carta.session import Session
from numpy import asarray
from PIL import Image #Might not be necessary
class png_group():
    
    def __init__(self, Session):
        self.sess = Session
        png_array = []
        
    @classmethod
    #def get_pngs(session):
    def get_pngs():
        #print('getimg')
        #populate png_array here by getting images from session object
        
        #The following code is just using test images
        img_back = Image.open('Complex_raster.png')
        img_for = Image.open('Complex_Contour.png')
        
        numpdata = asarray(img_back)
        background = png_single(numpdata)
        png_array.append(background)
        
        numpdata = asarray(img_for)
        foreground = png_single(numpdata)
        png_array.append(foreground) 
        #End of test images
    
    @classmethod
    def make_grey(png) -> png_single:
        img = Image.fromarray(png.data)
        grey_img = img.convert('L')
        grey_nump = asarray(grey_img)
        return grey_nump
      
    def get_size():
        return len(png_array)
    
    def get_image(x):
        return png_array[x]