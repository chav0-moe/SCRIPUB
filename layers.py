#!/usr/bin/env python3

from carta.constants import Overlay
from carta.constants import PaletteColor
from carta.constants import ContourDashMode, Colormap
from toVector import ToVector



class Layers:
    #List of overlay components derived from overlaysores class
    OVERLAY_COMPONENTS = [Overlay.TITLE, Overlay.GRID, Overlay.BORDER, Overlay.AXES, Overlay.NUMBERS, Overlay.BEAM, Overlay.LABELS, Overlay.COLORBAR]
    
    #Class constructor
    def __init__(self, rasterList, vectorList):
        self.rasterList = rasterList
        self.vectorList = vectorList

    @classmethod
    def from_carta(cls, session):
        #TODO look up pre-processing algorithm
        #Initialisation of empty lists and variables which will store data obtained from the invocation of the from_carta method
        rasterList = []
        vectorList = []
        visibleLayers = []  #List to keep track of all the visible elements within the active session
        overlayColor = session.palette_to_rgb(PaletteColor.BLACK)   #Variable which stores the color black
        ticksVisible = False    #Initialised boolean variable which stores the state of the ticks with in the session object 
        contours_visible = False
        #TODO look if there are better data structure to use instead of simple lists

        #Save the session befor rendering it

        #TODO obtain the list of images in order to extract layers from each image
        def chooseImage(self):
            return


        #Loops through the component list to check which of the components are visible
        #TODO consider using recursion instead of loops
        for overlayCom in Layers.OVERLAY_COMPONENTS:
            if session.visible(overlayCom):
                visibleLayers.append(overlayCom)


        #Checks if there are any ticks visible, then makes them less visible
        if Overlay.TICKS in visibleLayers:
            ticksVisible = True
            ticksLayer = session.get_overlay_value(Overlay.TICKS, "overlaystore.ticks")
            print(ticksLayer)
        
        session.call_overlay_action(Overlay.TICKS,"setWidth", 0.00001)

        #Loop hides all of the overlay components
        for component in Layers.OVERLAY_COMPONENTS:
            if component !=  Overlay.TICKS:
                session.hide(component)

        #Store variable for image displayed in current session
        img = session.active_frame()


        #TODO check if the contours are visible before hiding them
        
        if img.get_value("contourConfig.visible") == True:
            contours_visible = True
            img.hide_contours()
            

        #Appending background image
        rasterList.append(session.rendered_view_data())
        session.save_rendered_view("background_raster.png")
        img.hide_raster()

        #TODO obtain the original color of the contours and add it to the color list
        #Saving the contours contained within the image if there are any
        if contours_visible:
            img.show_contours()
            contour_color = img.get_value("contourConfig.color")
            color_string = "rgb("+str(contour_color.get('b'))+", "+str(contour_color.get('g'))+", "+str(contour_color.get('r'))+")"
            print(color_string)
            img.set_contour_color(overlayColor)
            vectorList.append(ToVector(session.rendered_view_data(), color_string))
            session.save_rendered_view("contours.png")
            img.hide_contours()
        
        #Function saves the overlay components
        #TODO add a check to see if the are any none colours which need to adopt the global color set
        def saveLayer(overlayComponent, sessionObj, x):
            sessionObj.show(overlayComponent)
            componentColor = sessionObj.color(overlayComponent)
            if componentColor == None:
                originalColor = sessionObj.palette_to_rgb(sessionObj.color(Overlay.GLOBAL))
            else:
                originalColor = sessionObj.palette_to_rgb(componentColor)
            sessionObj.set_color(PaletteColor.BLACK, overlayComponent)
            vectorList.append(ToVector(sessionObj.rendered_view_data(), originalColor))
            session.save_rendered_view("image"+str(x)+".png")
            sessionObj.hide(overlayComponent)

        #Loop used to show the overlay components individually and then hide them once they have been added to the list in byte format
        x = 0
        for component in visibleLayers:
            if component == Overlay.COLORBAR:
                session.show(Overlay.COLORBAR)
                rasterList.append(session.rendered_view_data())
                session.hide(Overlay.COLORBAR)
            else:
                saveLayer(component, session, x)
                x = x+1

        #Ticks
        if ticksVisible:
            session.call_overlay_action(Overlay.TICKS,"setWidth", ticksLayer)
            ticksColor = session.color(Overlay.TICKS)
            ticksRGB = session.palette_to_rgb(ticksColor)
            session.set_color(PaletteColor.BLACK, Overlay.TICKS)
            vectorList.append(ToVector(session.render_view_data(), ticksRGB))
            session.save_rendered_view("ticks.png")

        #To restore the session once it has been rendered
        for component in visibleLayers:
            session.show(component)

        return cls(rasterList, vectorList)
        
        #TODO return a list of layers objects
        #TODO consider animations
        #TODO think in terms of functions
        #TODO built-in methods to optimise the already exsisitng code
        #TODO use guppy to scale down on memory usage
        #TODO consider multi-processing
    
 