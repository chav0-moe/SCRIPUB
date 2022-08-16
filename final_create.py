from carta.session import Session
from io import BytesIO
import io
import base64
from vect_img import vect_img
from PIL import Image
from threading import Thread
from time import sleep, perf_counter

class final_create():
    
    vect_array = []

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
            back_data = final_create.pil2data(back_img)
            xml_lines = xml_lines + '<image xlink:href="'+u'data:img/png;base64,'+back_data+'" width="100%" height="100%" class="bg-image"/> \n'
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
            
            for image in vect_img_arr:
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
    def populate_array(self, image, colour):
        vect = vect_img(image, colour)
        final_create.vect_array.append(vect)
        
    
    @classmethod
    #def from_session(self, session):  #Method that fetches the images from the session and stores them in an array of vect_img objects
    def from_session(self):
    
            ########################################################### -- Testing code. Tangwa's code will be placed here
            #Three arrays are to be generated here: One for the background images, one for the foreground images that are to be vectorized, and another that contains the colour value of those foreground images
            #The foreground and colour arrays can be combined into a single object for simpler code
            
            back_arr = []
            #before_vect_array = []
            #colour_array = []
            vect_img_arr = []
            threads = []
            
            back = Image.open('Complex_raster.png')
            back_arr.append(back)
            #back2 = Image.open('map_scale.png')
            
            im = Image.open('Complex_Contour.png')
            im2 = Image.open('Simple_Contours.png')
            im3 = Image.open('Complex_Contour.png')
            im4 = Image.open('Complex_Contour.png')
            im5 = Image.open('Complex_Contour.png')
            #im6 = Image.open('C5.png')
            #im7 = Image.open('C6.png')
            #im8 = Image.open('C7.png')
            #im9 = Image.open('C8.png')
            
            img = vect_img(im, '#00ba37')
            img2 = vect_img(im2, 'red')
            img3 = vect_img(im3, 'red')
            img4 = vect_img(im4, 'red')
            img5 = vect_img(im5, 'red')
            #img6 = vect_img(im6, 'red')
            #img7 = vect_img(im7, 'red')
            #img8 = vect_img(im8, 'red')
            #img9 = vect_img(im9, 'red')

            vect_img_arr.append(img)
            vect_img_arr.append(img2)
            vect_img_arr.append(img3)
            vect_img_arr.append(img4)
            vect_img_arr.append(img5)
            
            
            
            
            #back_arr.append(back2)
            #img_array.append(img)
            #img_array.append(img2)
            
            #before_vect_array.append(im)
            
            #before_vect_array.append(im2)
            #before_vect_array.append(im3)
            #before_vect_array.append(im4)
            #before_vect_array.append(im5)
            #before_vect_array.append(im6)
            #before_vect_array.append(im7)
            #before_vect_array.append(im8)
            #before_vect_array.append(im9)
            
            #colour_array.append('#00ba37')
            
            #colour_array.append('#00ba37')
            #colour_array.append('red')
            #colour_array.append('red')
            #colour_array.append('red')
            #colour_array.append('red')
            #colour_array.append('red')
            #colour_array.append('red')
            #colour_array.append('red')
            
            ###########################################################
            
            start_time = perf_counter()
            
            #for n in range(0, len(before_vect_array)):
                #t = Thread(target=final_create.populate_array, args=(before_vect_array[n],colour_array[n],))
                #threads.append(t)
                #t.start()
                #print('new thread started')
            
            for vec in vect_img_arr:
                t = Thread(target=vec.get_path)
                threads.append(t)
                t.start()
            
            for t in threads:
                t.join()
            
            end_time = perf_counter()
            print(f'It took {end_time- start_time: 0.2f} seconds to complete.')
    
            final_create.create('created_vector.svg', back_arr, final_create.vect_array)
    
