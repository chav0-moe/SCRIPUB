#!/usr/bin/env python3

from carta.constants import Overlay

class Layers:
    
    def processor(session):
        
        #List of overlay components derived from overlaysores class
        overlay_components = [Overlay.TITLE, Overlay.GRID, Overlay.BORDER, Overlay.AXES, Overlay.NUMBERS, Overlay.BEAM, Overlay.LABELS, Overlay.COLORBAR, Overlay.TICKS]

        #List to keep track of all the visible elements within the active session
        visibleLayers = []

        #Loops through the component list to check which of the components are visible
        for overlayCom in overlay_components:
            if session.visible(overlayCom):
                visibleLayers.append(overlayCom)

        #Obtain the value of ticks if it is visible in the current session
        ticksLayer = Overlay.TICKS
        
        ticksVisible = False
        if ticksLayer in visibleLayers:
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
        for component in overlay_components:
            session.hide(component)


        #TODO get the width of the ticks before setting them to null
        session.call_overlay_action(Overlay.TICKS,"setWidth", 0.0001)

        #List which is used to store the individual layers
        rasterLayers = []
        vectorLayers = []

        #Store variable for the background raster image
        #TODO have some form of flag to distingush between the elements which need to be vectorised and the raster layers, ideally with the latter first
        backgroundImg = session.rendered_view_data()
        rasterLayers.append(backgroundImg)
        #sessionObj.save_rendered_view("background_raster.png")
        img.hide_raster()

        #Contours
        if contours_visible:
            img.show_contours()
            contours = session.rendered_view_data()
            vectorLayers.append(contours)
            #sessionObj.save_rendered_view("contours.png")
            img.hide_contours()

        #Function saves the overlay components
        def saveLayer(overlayComponent, sessionObj, layerList):
            sessionObj.show(overlayComponent)
            sessionObj.set_color("black", overlayComponent)
            layerList.append(sessionObj.rendered_view_data())
            #sessionObj.save_rendered_view("labels.png")
            sessionObj.hide(overlayComponent)

        #Loop used to show the overlay components individually and then hide them once they have been added to the list in byte format
        for component in overlay_components:
            saveLayer(component, session, vectorLayers)

        #Ticks
        if ticksVisible:
            vectorLayers.append(session.call_overlay_action(Overlay.TICKS,"setWidth", ticksLayer))

        return rasterLayers, vectorLayers

    
