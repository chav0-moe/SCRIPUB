#!/usr/bin/env python3

from carta.constants import Overlay
from carta.constants import PaletteColor
from toVector import ToVector
import sys


class Layers:
    #List of overlay components derived from overlaysores class, except ticks
    OVERLAY_COMPONENTS = [Overlay.TITLE, 
                            Overlay.GRID, 
                            Overlay.BORDER, 
                            Overlay.AXES, 
                            Overlay.NUMBERS, 
                            Overlay.BEAM, 
                            Overlay.LABELS, 
                            Overlay.COLORBAR]
    
    #Class constructor
    def __init__(self, rasterList, vectorList):
        self.rasterList = rasterList
        self.vectorList = vectorList

    @classmethod
    def from_carta(cls, session):
        #Initialisation of empty lists and variables which will store data obtained 
        # from the invocation of the from_carta method
        rasterList = [] #List to store raster elements data
        vectorList = [] #List to store objects of data for vectorization
        visibleLayers = []  #List to keep track of all the visible elements within the active session
        ticksVisible = False
        contours_visible = False    #Variable used to keep track of contours visibility
        backgroundColor = session.palette_to_rgb(PaletteColor.WHITE)

        img = session.active_frame()
        #Saves the session before showing and hiding elements
        session.save_rendered_view("Before_pre-processing.png")

        #Loops through the component list to check which of the components are visible
        visibleLayers = [component for component in Layers.OVERLAY_COMPONENTS if session.visible(component)]  #Loop eliniataed, functional 

        #Checks if there are any ticks visible, then makes them less visible
        ticksLayer = session.get_overlay_value(Overlay.TICKS, "width")

        #Loop hides all of the overlay components, except ticks
        for component in Layers.OVERLAY_COMPONENTS:
            session.hide(component)

        #Reduces the visibility of ticks in the session
        if ticksLayer > 0.00001:
            ticksVisible = True
            session.call_overlay_action(Overlay.TICKS,"setWidth", 0.00001)


        #Checks whether the contours are visible in given image
        if (img.get_value("contourConfig.visible") == True) and (img.get_value("contourConfig.levels") != None):
            contours_visible = True
            img.hide_contours()
            
        #Append background image to raster list
        rasterList.append(session.rendered_view_data())
        session.save_rendered_view("background_raster.png")
        img.hide_raster()

        session.show(Overlay.COLORBAR)
        rasterList.append(session.rendered_view_data())
        session.hide(Overlay.COLORBAR)

        #Saves contour data in a ToVector object, object is added to vector list
        if contours_visible:
            img.show_contours()
            contour_color = img.get_value("contourConfig.color")
            color_string = "rgb("+str(contour_color.get('b'))+", "+str(contour_color.get('g'))+", "+str(contour_color.get('r'))+")"
            img.set_contour_color(session.palette_to_rgb(PaletteColor.BLACK))
            vectorList.append(ToVector(session.rendered_view_data(backgroundColor), color_string))
            session.save_rendered_view("contours.png")
            img.hide_contours()
        
        #Function saves overlay components
        #Function changes overlay color to black before saving it
        #Function changes color back to the original color
        def saveLayer(overlayComponent, x):
            session.show(overlayComponent)
            componentColor = session.color(overlayComponent)
            if componentColor == None:
                originalColor = session.palette_to_rgb(session.color(Overlay.GLOBAL))
            else:
                originalColor = session.palette_to_rgb(componentColor)
            session.set_color(PaletteColor.BLACK, overlayComponent)
            vectorList.append(ToVector(session.rendered_view_data(backgroundColor), originalColor))
            session.save_rendered_view("image"+str(x)+".png")
            if componentColor == None:
                session.set_color(session.color(Overlay.GLOBAL), overlayComponent)
            else:
                session.set_color(componentColor, overlayComponent)
            session.hide(overlayComponent)

        #Loop through the visible overlay components
        #The colorbar is added to the raster list
        #The remaining visible layers are saved by invoking the saveLayer function
        x = 0
        for component in visibleLayers:
            if component != Overlay.COLORBAR:
                saveLayer(component, x)
                x = x+1

        
        #Ticks width is adjusted to improve visibility
        #The ticks color is set to black before saving
        #Ticks color is set back to the original color
        if ticksVisible:
            session.call_overlay_action(Overlay.TICKS,"setWidth", ticksLayer)
            ticksColor = session.color(Overlay.TICKS)
            if ticksColor != None:
                ticksRGB = session.palette_to_rgb(ticksColor)
            else:
                ticksRGB = session.palette_to_rgb(session.color(Overlay.GLOBAL))
            session.set_color(PaletteColor.BLACK, Overlay.TICKS)
            vectorList.append(ToVector(session.rendered_view_data(backgroundColor), ticksRGB))
            session.save_rendered_view("ticks.png")
            if ticksColor == None:
                session.set_color(session.color(Overlay.GLOBAL), Overlay.TICKS)
            else:
                session.set_color(ticksColor, Overlay.TICKS)

        #Shows the background raster image
        img.show_raster()

        #Contours are set to original visibility state
        if contours_visible:
            img.set_contour_color(color_string)
            img.show_contours()

        #Loop restores all overlay components that were visible at the start of the session
        for component in visibleLayers:
            session.show(component)

        session.save_rendered_view("After_pre-processing.png")

        #returns an instance of the Layers class containing two lists
        return cls(rasterList, vectorList)
        
        #TODO return a list of layers objects
        #TODO consider animations
        #TODO built-in methods to optimise the already exsisitng code
        #TODO use guppy to scale down on memory usage
        #TODO consider multi-processing
    
 