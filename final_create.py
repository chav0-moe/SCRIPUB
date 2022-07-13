from carta.session import Session

class final_create():
    
    @classmethod
    def from_session(session):
        #Call method (PNG_group method) to fetch PNG images from CARTA (Tangwa), storing them in a png_group object
        png_group(session)
        
        #Instantiate SVG_group object, passing it the png_group object
        
        #Call class method in this class to combine the SVGs and background PNG, passing it the PNG_group and SVG_group objects
        combine()
        
    @classmethod
    def combine(png_group, svg_group): #Combine an image from the png_group with all the vectorized svg images in svg_group
        print ('combine')