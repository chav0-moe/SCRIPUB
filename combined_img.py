from carta.session import Session
from io import BytesIO
import io
import base64
from raw_img import raw_img
from PIL import Image
from threading import Thread
from layers import Layers

#Sort variable names

class combined_img():

    def __init__(self, raw_image_array, width, height):
        self.raw_image_array = raw_image_array              #Array of raw_img objects
        self.img_width = width            
        self.img_height = height
    
    def resize(im, w, h):                              #Expands the image, in order to improve the performace of the Potrace algorithm.
        new_dimensions = (w, h)
        new_img = im.resize(new_dimensions)
        return new_img

    def remove_transparency(im):                           #Removes transparency of image by placing a white background. CARTA now facilitates this.
        new_img = Image.new('RGBA', im.size, (255,255,255))
        new_img.paste(im, (0, 0), im)
        return new_img

    def pil2data(img):                          #Converts PIL image to datauri.
        data = BytesIO()
        img.save(data, "PNG")
        data64 = base64.b64encode(data.getvalue())
        return data64.decode('utf-8')

    def data2pil(data):                       #Converts datauri to a PIL image.
        im_stream = io.BytesIO(data)               
        img = Image.open(im_stream)                
        return img

    def get_background_xml(background_arr):       #Creates xml code for the png images to be embedded into the svg image.
        xml_back_lines = ""
        for back_img in background_arr:
            back_data = combined_img.pil2data(back_img.img)
            xml_back_lines = xml_back_lines + '<image xlink:href="'+u'data:img/png;base64,'+back_data+'" width="100%" height="100%" class="bg-image"/> \n'
        return xml_back_lines

    
    def to_svg(self, file_name):     #Pass an output file name. Uses img_array instance to create svg image from the vector and raster images in that array.
        back_arr = []
        vect_arr = []
        
        for img in self.raw_image_array:                                            #Separate the vector and the raster images
            if img.bool_trace == True:
                vect_arr.append(img)
            if img.bool_trace == False:
                back_arr.append(img)
        
        with open(file_name, "w") as fp:
            fp.write(
                '<svg version="1.1"' +                                                      #First line of xml to identify the file as an SVG image
                ' xmlns="http://www.w3.org/2000/svg"' +
                ' xmlns:xling="http://www.w3.org/1999/xlink"' +
                ' viewBox="0 0 '+str(self.img_width)+' '+str(self.img_height)+'">' +
                '\n' +
                combined_img.get_background_xml(back_arr)                                   #Get the background array data as xml and insert it into the xml file 
            )
            
            all_parts =  []
            for image in vect_arr:                                                  #Loop through the vector path of each image, creating the path defenition "d" for each of them
                parts = []
                parts.append(image.colour)                                          #Store the overlay compontents original colour as the first item
                for curve in image.path:
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
                    parts.append("z")                                                               #Identifies the end of a vector path
                all_parts.append(parts)
            
                                     
            for parts in all_parts:                                             #Create the xml code for each individual vector path and its respective colour
                colour_value = parts[0]
                del parts[0]

                paths_to_write = "".join(parts)
                fp.write(f'<path stroke="none" fill="{colour_value}" fill-rule="evenodd" fill-opacity="1" d="{paths_to_write}"/> \n')   #XML line for each vector image
            
            fp.write("</svg>")    
            
        
    @classmethod
    def from_session(cls, session):     #Method that fetches the images from the session and stores them in an array of vect_img objects
        print("Running...")
        
        expansion_factor = 5
        raw_image_arr = []
        potrace_threads = []
        
        layers = Layers.from_carta(session)                             #Exports the images as data from CARTA, storing them in the rasterList and vectorList attributes
                                                  
        for image in layers.rasterList:                                 
            pil_format = combined_img.data2pil(image)                   #Convert image data to PIL image
            
            width, height = pil_format.size                             
            new_width = width*expansion_factor
            new_height = height*expansion_factor
            resized_image = combined_img.resize(pil_format, new_width, new_height)  #Expand the image size
            
            raw_image_arr.append(raw_img(False, resized_image, None))   #Create raw_img object, with the trace flag = False and no original colour
            

        for image in layers.vectorList:
            pil_format = combined_img.data2pil(image.data)              #Convert image data to PIL image
            
            width, height = pil_format.size                             
            new_width = width*expansion_factor
            new_height = height*expansion_factor
            resized_image = combined_img.resize(pil_format, new_width, new_height)  #Expand the image size
            
            raw_image_arr.append(raw_img(True, resized_image, str(image.color)))    #Create raw_img object, with the trace flag = True and with an original colour that will be added back
        
        for image in raw_image_arr:                                     
                if image.bool_trace == True:                                #Create multiple threads to generate the path objects for each raw_img.
                    t = Thread(target=image.get_path)
                    potrace_threads.append(t)
                    t.start()
            
        for t in potrace_threads:                                           #Wait for all threads to finish
            t.join()
            
        inst = cls(raw_image_arr, new_width, new_height)                    #Create and return combined_img instance to user
        return inst