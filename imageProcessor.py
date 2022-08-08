#!/usr/bin/env python3

from carta.constants import Overlay

class Layers:
    
    def processor(session):
        
        #List of overlay components derived from overlaysores class
        overlay_components = [Overlay.TITLE, Overlay.GRID, Overlay.BORDER, Overlay.AXES, Overlay.NUMBERS, Overlay.BEAM, Overlay.LABELS, Overlay.COLORBAR, Overlay.TICKS]

        #List to keep track of all the visible elements within the active session
        visible = []

        #Loops through the component list to check which of the components are visible
        for overlayCom in overlay_components:
            if visible(overlayCom):
                visible.append(overlayCom)

            
        #TODO explore other components contained within the colorbar

        #Store variable for image in current session
        img = session.active_frame()
        

        
        #TODO check if the contours are visible before hiding them
        img.hide_contours()

        #Loop hides all of the overlay components
        for component in overlay_components:
            session.hide(component)

        #TODO get the width of the ticks before setting them to null
        session.call_overlay_action(Overlay.TICKS,"setWidth", 0.0001)

        #List which is used to store the individual layers
        layers = []


        #Store variable for the background raster image
        #TODO have some form of flag to distingush between the elements which need to be vectorised and the raster layers, ideally with the latter first
        backgroundImg = session.rendered_view_data()
        layers.append(backgroundImg)
        #sessionObj.save_rendered_view("background_raster.png")
        img.hide_raster()

        #Contours
        img.show_contours()
        contours = session.rendered_view_data()
        layers.append(contours)
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
            saveLayer(component, session, layers)

        #Ticks
        if visible['Ticks']:
            ticksWidth = visible['Ticks']
            ticks = session.call_overlay_action(Overlay.TICKS,"setWidth", ticksWidth)
            layers.append(ticks)

        return layers

    
