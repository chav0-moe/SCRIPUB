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
        
        cls.img_width = width            #Original size of image is 1138 by 511 on Dell
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
                ' viewBox="0 0 %d %d">' % (self.img_width, self.img_height) +
                '\n' +
                self.get_background_xml(back_arr)                                   #Get the background array data and put it in the xml
                
            )
            parts = []
            
            for image in vect_arr:
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
                parts.append("--endOfPath--")
                parts.append(image.colour)
                #parts.append(hex_value)
            
            x = 0
            paths_to_write = ""
            while x < len(parts):
                if parts[x] == "--endOfPath--":
                    x += 1
                    #print(parts[x])
                    #print(paths_to_write)
                    fp.write('<path stroke="none" fill="' + parts[x] + '" fill-rule="evenodd" fill-opacity="1" d="%s"/> \n' % (paths_to_write))
                    paths_to_write = ""
                    x += 1
                else:
                    paths_to_write = paths_to_write + parts[x]
                    x += 1
                
            fp.write("</svg>")
            
        
    @classmethod
    def from_session(cls, session):  #Method that fetches the images from the session and stores them in an array of vect_img objects
        image_arr = []
        threads = []
        layers = Layers.from_carta(session)

        for image in layers.rasterList:
            pil_format = cls.data2pil(image)
            
            width, height = pil_format.size
            new_width = width*5
            new_height = height*5
            #print("width: " + str(new_width) + "height: " + str(new_height))
            
            resized_image = cls.resize(pil_format, new_width, new_height)
            image_arr.append(raw_img(False, resized_image, None))
        
        for image in layers.vectorList:
            #print(len(layers.vectorList))
            #print(image.color)
            pil_format = cls.data2pil(image.data)
            
            width, height = pil_format.size
            new_width = width*5
            new_height = height*5
            #print("width: " + str(new_width) + "height: " + str(new_height))
            
            resized_image = cls.resize(pil_format, new_width, new_height)
            vectorizable = cls.remove_transparency(resized_image)
            image_arr.append(raw_img(True, vectorizable, str(image.color)))
        
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
   
    @classmethod    
    #This method is just to test some code
    def from_2(cls):    
        
        ########################################## --Reading in of textfiles containing image data
        raster_file = open("rasterLayers.txt", "r")
        raster_data = raster_file.read().split(', ')
        raster_file.close()
        
        vector_file = open("vectorLayers.txt", "r")
        vector_data = vector_file.read().split(', ')
        vector_file.close()
        
        colour_file = open("color.txt", "r")
        colour_data = colour_file.read().split(', ')
        colour_file.close()
        
        #image1 = Image.open('Complex_Contour.png')
        #image1_data = cls.pil2data(image1)
        #print(image1_data)
        
        ########################################## --Test to split different colours in an image into its own image
        imc = cv2.imread('testing.png')
        imcv = cv2.bitwise_not(imc)
        blue, green, red = cv2.split(imcv)
           
        blue_zeros = np.zeros(blue.shape, np.uint8)
        green_zeros = np.zeros(green.shape, np.uint8)
        red_zeros = np.zeros(red.shape, np.uint8)
 
        blueBGR = cv2.merge((blue,blue_zeros,blue_zeros))
        greenBGR = cv2.merge((green_zeros,green,green_zeros))
        redBGR = cv2.merge((red_zeros,red_zeros,red))
           
        im_blue = Image.fromarray(blueBGR)
        im_blue.save('blue.png')
        im_green = Image.fromarray(greenBGR)
        im_green.save('green.png')
        im_red = Image.fromarray(redBGR)
        im_red.save('red.png')
            
            
            
        #redBGR.save("red.png")
        #greenBGR.save("green.png")
        #blueBGR.save("blue.png")
            
            

        #new_image = r.convert('RGB')
            
        #new_image = Image.merge("RGB", (r_none, g, b_none))
        #new_image.save("What_is_this.png")
        #r.save("red_band.png")
        #g.save("blue_band.png")
        #.save("green_band.png")
        #alpha.save("This_is.png")
            
        ###########################################
        
        image_arr = []
        #print(len(vector_data))
        for img_data in vector_data:
            #print(img_data)
            #this_image = Image.open(img_data)
            img = cls.data2pil(img_data)
            image_arr.append(raw_img(False, img, None))
        
        
    