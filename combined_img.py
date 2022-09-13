from carta.session import Session
from io import BytesIO
import io
import base64
from raw_img import raw_img
from PIL import Image
from threading import Thread
from time import sleep, perf_counter
from layers import Layers

class combined_img():

    def __init__(cls, image_array, width, height):
        cls.image_array = image_array
        
        cls.img_width = width            #Original size of image is 1138 by 511 on Martin's device
        cls.img_height = height
    
    @classmethod
    def resize(cls, im, w, h):
        #width, height = im.size
        newsize = (w, h)
        #newsize = (cls.img_width, cls.img_height)
        new_img = im.resize(newsize)
        return new_img
    
    @classmethod
    def remove_transparency(cls, im):
        new_img = Image.new('RGBA', im.size, (255,255,255))
        new_img.paste(im, (0, 0), im)
        return new_img
    
    @classmethod
    def pil2data(cls, img):                          #Converts PIL image to datauri
        data = BytesIO()
        img.save(data, "PNG")
        data64 = base64.b64encode(data.getvalue())
        #return u'data:img/png;base64,'+data64.decode('utf-8')
        return data64.decode('utf-8')
        
    @classmethod
    def data2pil(cls, data):                       #Converts datauri to a PIL image       
        im_stream = io.BytesIO(data)    # convert image to file-like object 
        img = Image.open(im_stream)   # img is now PIL Image object
        return img
        
    @classmethod
    def get_background_xml(cls, background_arr):       #Creates xml code for the png images to be embedded into the svg image
        xml_lines = ""
        for back_img in background_arr:
            
            back_data = cls.pil2data(back_img.img)
            xml_lines = xml_lines + '<image xlink:href="'+u'data:img/png;base64,'+back_data+'" width="100%" height="100%" class="bg-image"/> \n'
        
        return xml_lines

    def to_svg(self, file_name):     #Pass an output file name, a background image array (PIL images), and an array of vect_img objects to be vectorized and combined
        back_arr = []
        vect_arr = []
        for img in self.image_array:
            if img.bool_trace == True:
                vect_arr.append(img)
            if img.bool_trace == False:
                back_arr.append(img)
        
        with open(file_name, "w") as fp:
            fp.write(
                '<svg version="1.1"' +
                ' xmlns="http://www.w3.org/2000/svg"' +
                ' xmlns:xling="http://www.w3.org/1999/xlink"' +
                ' viewBox="0 0 '+str(self.img_width)+' '+str(self.img_height)+'">' +
                '\n' +
                self.get_background_xml(back_arr)                                   #Get the background array data and put it in the xml
                
            )
            all_parts =  []
            for image in vect_arr:                                                  #Loop through the vector path of each image, creating the path defenition "d" for each of them
                parts = []
                parts.append(image.colour)
                for curve in image.path:
                    fs = curve.start_point
                    #print("Curve start: "+fs.x+" "+fs.y)
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
                all_parts.append(parts)
            
                                     
            for parts in all_parts:                     #Create the xml code for each individual vector path, colour included
                colour_value = parts[0]
                del parts[0]
                paths_to_write = []
                for curr_string in parts:
                    paths_to_write.append(curr_string)
                
                join_write = "".join(paths_to_write)
                #fp.write('<path stroke="none" fill="' + colour_value + '" fill-rule="evenodd" fill-opacity="1" d="%s"/> \n' % (join_write))
                fp.write(f'<path stroke="none" fill="{colour_value}" fill-rule="evenodd" fill-opacity="1" d="{join_write}"/> \n')
            fp.write("</svg>")    
            
        
    @classmethod
    def from_session(cls, session):  #Method that fetches the images from the session and stores them in an array of vect_img objects
        image_arr = []
        threads = []
        layers = Layers.from_carta(session)
        
        #x = 0                                                   #Saving images for testing
        for image in layers.rasterList:
            pil_format = cls.data2pil(image)
            
            width, height = pil_format.size
            new_width = width*5
            new_height = height*5
            #print("width: " + str(new_width) + "height: " + str(new_height))
            
            resized_image = cls.resize(pil_format, new_width, new_height)
            image_arr.append(raw_img(False, resized_image, None))
            #resized_image = resized_image.save("check_raster_image_"+str(x)+".png")
            #x = x+1
            
            
        #x = 0
        for image in layers.vectorList:
            #print(len(layers.vectorList))
            #print(image.color)
            pil_format = cls.data2pil(image.data)
            
            width, height = pil_format.size
            new_width = width*5
            new_height = height*5
            #print("width: " + str(new_width) + "height: " + str(new_height))
            
            resized_image = cls.resize(pil_format, new_width, new_height)
            #vectorizable = cls.remove_transparency(resized_image)
            image_arr.append(raw_img(True, resized_image, str(image.color)))
            #resized_image = resized_image.save("check_vector_image_"+str(x)+".png")
            #x = x+1
        
        start_time = perf_counter()
        for image in image_arr:
                if image.bool_trace == True:
                    t = Thread(target=image.get_path)
                    #print("Created new thread")
                    threads.append(t)
                    t.start()
            
        for t in threads:
            t.join()
            
        end_time = perf_counter()
        print(f'It took {end_time- start_time: 0.2f} seconds to complete.')

        inst = cls(image_arr, new_width, new_height)
        return inst