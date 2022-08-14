#!/usr/bin/env python3

from carta.constants import Overlay
from carta.constants import PaletteColor

class Layers:
    #List of overlay components derived from overlaysores class
    OVERLAY_COMPONENTS = [Overlay.TITLE, Overlay.GRID, Overlay.BORDER, Overlay.AXES, Overlay.NUMBERS, Overlay.BEAM, Overlay.LABELS, Overlay.COLORBAR, Overlay.TICKS]
    rasterList = []
    vectorList = []
    originalColor = []

    def __init__(self, *args):
        pass

    @classmethod
    def from_carta(cls, session):

        #List to keep track of all the visible elements within the active session
        visibleLayers = []
        ticksVisible = False
        #Loops through the component list to check which of the components are visible
        for overlayCom in Layers.OVERLAY_COMPONENTS:
            if session.visible(overlayCom):
                visibleLayers.append(overlayCom)

      
        if Overlay.TICKS in visibleLayers:
            ticksVisible = True
            ticksLayer = session.get_overlay_value(Overlay.TICKS, "overlaystore.ticks")

        #TODO explore other components contained within the colorbar

        #Store variable for image in current session
        img = session.active_frame()
        

        
        #TODO check if the contours are visible before hiding them
        contours_visible = False
        if img.set_contours_visible(True):
            contours_visible = True
            img.hide_contours()
        

        #Loop hides all of the overlay components
        for component in Layers.OVERLAY_COMPONENTS:
            session.hide(component)


        #TODO get the width of the ticks before setting them to null
        session.call_overlay_action(Overlay.TICKS,"setWidth", 0.0001)

        #Store variable for the background raster image
        #TODO have some form of flag to distingush between the elements which need to be vectorised and the raster layers, ideally with the latter first
        #List which is used to store the individual layers

        #List for original colors of each component
        #Appending background image
        cls.rasterList.append(session.rendered_view_data())
        #sessionObj.save_rendered_view("background_raster.png")
        img.hide_raster()

        #Contours
        if contours_visible:
            img.show_contours()
            img.set_contour_color(PaletteColor.BLACK)
            cls.vectorList.append(session.rendered_view_data())
            #sessionObj.save_rendered_view("contours.png")
            img.hide_contours()

        #Function saves the overlay components
        #TODO add a check to see if the are any none colours which need to adopt the global color set
        #TODO saving the colorbar as an actusl layer
        def saveLayer(overlayComponent, sessionObj, layerList):
            sessionObj.show(overlayComponent)
            cls.originalColor.append(sessionObj.color(overlayComponent))
            sessionObj.set_color(PaletteColor.BLACK, overlayComponent)
            layerList.append(sessionObj.rendered_view_data())
            #sessionObj.save_rendered_view("labels.png")
            sessionObj.hide(overlayComponent)

        #Loop used to show the overlay components individually and then hide them once they have been added to the list in byte format
        for component in visibleLayers:
            saveLayer(component, session, cls.vectorList)

        #Ticks
        if ticksVisible:
            session.call_overlay_action(Overlay.TICKS,"setWidth", ticksLayer)
            session.set_color("black", Overlay.TICKS)
            cls.vectorList.append(session.render_view_data())

        return cls(session, cls.rasterList, cls.vectorList, cls.originalColor)

    
 