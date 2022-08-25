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
        layers = []
        rasterList = []
        vectorList = []
        originalColor = []
        visibleLayers = []

        overlayColor = session.palette_to_rgb(PaletteColor.BLACK)

        #TODO obtain the list of images in order to extract layers from each image
        def chooseImage(self):
            return


        #List to keep track of all the visible elements within the active session
        
        ticksVisible = False
        #Loops through the component list to check which of the components are visible
        #TODO consider using recursion instead of loops
        for overlayCom in Layers.OVERLAY_COMPONENTS:
            if session.visible(overlayCom):
                visibleLayers.append(overlayCom)

      
        if Overlay.TICKS in visibleLayers:
            ticksVisible = True
            ticksLayer = session.get_overlay_value(Overlay.TICKS, "overlaystore.ticks")


        #Loop hides all of the overlay components
        for component in Layers.OVERLAY_COMPONENTS:
            session.hide(component)
        
        #TODO explore other components contained within the colorbar
    

        #Store variable for image in current session
        img = session.active_frame()
        print("Contours if executed")
        img.hide_contours()
        time.sleep(10)
        print("Contours hidden")
        session.save_rendered_view("BackNew.png")

        
        
        #TODO check if the contours are visible before hiding them
        contours_visible = False
        if img.get_value("contourConfig.levels") != None:
            print("Contours if executed")
            contours_visible = True
            print(img.get_value())
            img.hide_contours()
            print()
            print("Contours hidden")

        print("Saving raster image")
        rasterList.append(session.rendered_view_data())
        session.save_rendered_view("background_raster.png")
        print("Raster image saved")
        
        #Appending background image
        img = session.active_frame()
        rasterList.append(session.rendered_view_data())
        session.save_rendered_view("background_raster.png")
        img.hide_raster()
       
        #TODO get the width of the ticks before setting them to null
        session.call_overlay_action(Overlay.TICKS,"setWidth", 0.00001)

        #Store variable for the background raster image
        #TODO have some form of flag to distingush between the elements which need to be vectorised and the raster layers, ideally with the latter first
        #List which is used to store the individual layers

        #List for original colors of each component
        #Appending background image
        rasterList.append(session.rendered_view_data())
        
        session.save_rendered_view("background_raster.png")
        img = session.active_frame()
        img.hide_raster()

    
        #Contours
        if contours_visible:
            img = session.active_frame()
            img.show_contours()
            img.hide_raster()
            img.set_contour_color(overlayColor)
            vectorList.append(session.rendered_view_data())
            session.save_rendered_view("contours.png")
            img.hide_contours()
        
        #Function saves the overlay components
        #TODO add a check to see if the are any none colours which need to adopt the global color set
        #TODO saving the colorbar as an actusl layer
        def saveLayer(overlayComponent, sessionObj, layerList, x):
            sessionObj.show(overlayComponent)
            originalColor.append(sessionObj.color(overlayComponent))
            #TODO change to rgb
            sessionObj.set_color(PaletteColor.BLACK, overlayComponent)
            layerList.append(sessionObj.rendered_view_data())
            session.save_rendered_view("image"+str(x)+".png")
            sessionObj.hide(overlayComponent)

        #Loop used to show the overlay components individually and then hide them once they have been added to the list in byte format
        x = 0
        for component in visibleLayers:
            if component == Overlay.COLORBAR:
                saveLayer(component, session, vectorList, x)
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
    
 