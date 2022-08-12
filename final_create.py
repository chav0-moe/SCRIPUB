from carta.session import Session
from io import BytesIO
import base64
from vect_img import vect_img
from PIL import Image

class final_create():
    
    @classmethod
    def pil2data(self, img):                          #Converts PIL image to datauri
        data = BytesIO()
        img.save(data, "PNG")
        #print(data)
        data64 = base64.b64encode(data.getvalue())
        return u'data:img/png;base64,'+data64.decode('utf-8')
        
    @classmethod
    def get_background_xml(self, background_arr):       #Creates xml code for the png images to be embedded into the svg image
        xml_lines = ""
        for back_img in background_arr:
            back_data = final_create.pil2data(back_img)
            xml_lines = xml_lines + '<image xlink:href="'+back_data+'" width="100%" height="100%" class="bg-image"/> \n'
        return xml_lines
    
    @classmethod
    def create(self, output, background_arr, vect_img_arr):     #Pass an output file name, a background image array (PIL images), and an array of vect_img objects to be vectorized and combined
        with open(output, "w") as fp:
            fp.write(
                '<svg version="1.1"' +
                ' xmlns="http://www.w3.org/2000/svg"' +
                ' xmlns:xling="http://www.w3.org/1999/xlink"' +
                ' width="%d" height="%d"' % (6824, 3600) +
                ' viewBox="0 0 %d %d">' % (6824, 3600) +
                '\n' +
                final_create.get_background_xml(background_arr)
                
            )
            parts = []
            
            for img in vect_img_arr:
                for curve in img.path:
                    fs = curve.start_point
                    parts.append("M%f,%f" % (fs.x, fs.y))
                    for segment in curve.segments:
                        if segment.is_corner:
                            a = segment.c
                            parts.append("L%f,%f" % (a.x, a.y))
                            b = segment.end_point
                            parts.append("L%f,%f" % (b.x, b.y))
                        else:
                            a = segment.c1
                            b = segment.c2
                            c = segment.end_point
                            parts.append("C%f,%f %f,%f %f,%f" % (a.x, a.y, b.x, b.y, c.x, c.y))
                    parts.append("z")
                parts.append("--endOfPath--")
                parts.append(img.colour)
            
            x = 0
            paths_to_write = ""
            while x < len(parts):
                if parts[x] == "--endOfPath--":
                    x += 1
                    fp.write('<path stroke="none" fill="' + parts[x] + '" fill-rule="evenodd" fill-opacity="1" d="%s"/> \n' % (paths_to_write))
                    paths_to_write = ""
                    x += 1
                else:
                    paths_to_write = paths_to_write + parts[x]
                    x += 1
                
            fp.write("</svg>")
            
        
    @classmethod
    #def from_session(self, session):  #Method that fetches the images from the session and stores them in an array of vect_img objects
    def from_session(self):
            back_arr = []
            img_array = []
            
            back = Image.open('Complex_raster.png')
            #back2 = Image.open('map_scale.png')
            im = Image.open('Complex_Contour.png')
            im2 = Image.open('Simple_Contours.png')
        
            img = vect_img(im, '#00ba37')
            img2 = vect_img(im2, 'red')
        
            back_arr.append(back)
            #back_arr.append(back2)
            img_array.append(img)
            img_array.append(img2)
    
            final_create.create('created_vector.svg', back_arr, img_array)
    
