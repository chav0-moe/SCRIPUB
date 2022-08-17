from carta.session import Session
from io import BytesIO
import io
import base64
from raw_img import raw_img
from PIL import Image
from threading import Thread
from time import sleep, perf_counter

class final_create():

    @classmethod
    def pil2data(self, img):                          #Converts PIL image to datauri
        data = BytesIO()
        img.save(data, "PNG")
        #print(data)
        data64 = base64.b64encode(data.getvalue())
        #return u'data:img/png;base64,'+data64.decode('utf-8')
        return data64.decode('utf-8')
        
    @classmethod
    def data2pil(self, data):                       #Converts datauri to a PIL image
        #Assuming base64_str is the string value without 'data:image/jpeg;base64,'
        img = Image.open(io.BytesIO(base64.decodebytes(bytes(data, "utf-8"))))
        return img

    #@classmethod
    #def rgb2hex(self, rgb_tuple):
        #r, g, b = rgb_tuple
        #return "#{:02x}{:02x}{:02x}".format(r,g,b)

    @classmethod
    def get_background_xml(self, background_arr):       #Creates xml code for the png images to be embedded into the svg image
        xml_lines = ""
        for back_img in background_arr:
            back_data = final_create.pil2data(back_img.img)
            xml_lines = xml_lines + '<image xlink:href="'+u'data:img/png;base64,'+back_data+'" width="100%" height="100%" class="bg-image"/> \n'
        return xml_lines

    @classmethod
    def create(self, output, img_arr):     #Pass an output file name, a background image array (PIL images), and an array of vect_img objects to be vectorized and combined
        back_arr = []
        vect_arr = []
        for img in img_arr:
            if img.bool_trace == True:
                vect_arr.append(img)
            if img.bool_trace == False:
                back_arr.append(img)
        
        with open(output, "w") as fp:
            fp.write(
                '<svg version="1.1"' +
                ' xmlns="http://www.w3.org/2000/svg"' +
                ' xmlns:xling="http://www.w3.org/1999/xlink"' +
                ' width="%d" height="%d"' % (6824, 3600) +
                ' viewBox="0 0 %d %d">' % (6824, 3600) +
                '\n' +
                final_create.get_background_xml(back_arr)
                
            )
            parts = []
            
            for image in vect_arr:
                for curve in image.path:
                    fs = curve.start_point
                    #print (fs.x)
                    #print (fs.y)
                    #pixel_colour = image.img.getpixel((fs.x, fs.y))[0:3]
                    #hex_value = final_create.rgb2hex(pixel_colour)
                    #print (hex_value)
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
                parts.append(image.colour)
                #parts.append(hex_value)
            
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
    
            ########################################################### -- Testing code. Tangwa's code will be placed here
            #Three arrays are to be generated here: One for the background images, one for the foreground images that are to be vectorized, and another that contains the colour value of those foreground images
            #The foreground and colour arrays can be combined into a single object for simpler code
            
            #back_arr = []
            #vect_img_arr = []
            image_arr = []
            threads = []
            
            back = Image.open('Complex_raster.png')
            image_arr.append(raw_img(False, back, None))
            #back_arr.append(back)
            #back2 = Image.open('map_scale.png')
            
            im = Image.open('Complex_Contour.png')
            #im2 = Image.open('Simple_Contours.png')
            
            image_arr.append(raw_img(True, im, '#00ba37'))
            #img2 = vect_img(im2, 'red')

            #vect_img_arr.append(img)
            #vect_img_arr.append(img2)
            
            ###########################################################
            
            start_time = perf_counter()
            
            
            for image in image_arr:
                if image.bool_trace == True:
                    t = Thread(target=image.get_path)
                    threads.append(t)
                    t.start()
                    print("New thread started")
            
            for t in threads:
                t.join()
            
            end_time = perf_counter()
            print(f'It took {end_time- start_time: 0.2f} seconds to complete.')
    
            final_create.create('created_vector.svg',image_arr)
    
