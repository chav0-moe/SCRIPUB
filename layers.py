#!/usr/bin/env python3

from carta.constants import Overlay
from carta.constants import PaletteColor
import time



class Layers:
    #List of overlay components derived from overlaysores class
    OVERLAY_COMPONENTS = [Overlay.TITLE, Overlay.GRID, Overlay.BORDER, Overlay.AXES, Overlay.NUMBERS, Overlay.BEAM, Overlay.LABELS, Overlay.COLORBAR, Overlay.TICKS]
    

    def __init__(self, rasterList,vectorList,originalColor):
        self.rasterList = rasterList
        self.vectorList = vectorList
        self.originalColor = originalColor

    @classmethod
    def from_carta(cls, session):
        #Initialisation of empty lists and variables which will store data obtained from the invocation of the from_carta method
        layers = []
        rasterList = []
        vectorList = []
        originalColor = []  #List for original colors of each component
        visibleLayers = []  #List to keep track of all the visible elements within the active session
        overlayColor = session.palette_to_rgb(PaletteColor.BLACK)   #Variable which stores the color black
        ticksVisible = False    #Initialised boolean variable which stores the state of the ticks with in the session object 


        #TODO obtain the list of images in order to extract layers from each image
        def chooseImage(self):
            return


        #Loops through the component list to check which of the components are visible
        #TODO consider using recursion instead of loops
        for overlayCom in Layers.OVERLAY_COMPONENTS:
            if session.visible(overlayCom):
                visibleLayers.append(overlayCom)


        #Checks if there are any ticks visible
        if Overlay.TICKS in visibleLayers:
            ticksVisible = True
            ticksLayer = session.get_overlay_value(Overlay.TICKS, "overlaystore.ticks")


        #Loop hides all of the overlay components
        for component in Layers.OVERLAY_COMPONENTS:
            session.hide(component)

        #Ticks are set to be less visible in the frame
        session.call_overlay_action(Overlay.TICKS,"setWidth", 0.00001)

    
        #Store variable for image displayed in current session
        img = session.active_frame()


        #TODO check if the contours are visible before hiding them
        contours_visible = False
        if img.get_value("contourConfig.levels") != None:
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
            img.set_contour_color(overlayColor)
            vectorList.append(session.rendered_view_data())
            session.save_rendered_view("contours.png")
            img.hide_contours()
        
        #Function saves the overlay components
        #TODO add a check to see if the are any none colours which need to adopt the global color set
        def saveLayer(overlayComponent, sessionObj, layerList, x):
            sessionObj.show(overlayComponent)
            originalColor.append(sessionObj.color(overlayComponent))
            sessionObj.set_color(PaletteColor.BLACK, overlayComponent)
            layerList.append(sessionObj.rendered_view_data())
            session.save_rendered_view("image"+str(x)+".png")
            sessionObj.hide(overlayComponent)

        #Loop used to show the overlay components individually and then hide them once they have been added to the list in byte format
        x = 0
        for component in visibleLayers:
            if component == Overlay.COLORBAR:
                saveLayer(component, session, rasterList, x)
                x = x+1
            else:
                saveLayer(component, session, vectorList, x)
                x = x+1

        #Ticks
        if ticksVisible:
            session.call_overlay_action(Overlay.TICKS,"setWidth", ticksLayer)
            session.set_color(PaletteColor.BLACK, Overlay.TICKS)
            vectorList.append(session.render_view_data())
            session.save_rendered_view("ticks.png")

        return cls(rasterList, vectorList, originalColor)
        
        #TODO return a list of layers objects
        #TODO consider animations
        #TODO think in terms of functions
        #TODO built-in methods to optimise the already exsisitng code
        #TODO use guppy to scale down on memory usage
        #TODO consider multi-processing
    
 