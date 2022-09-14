#!/usr/bin/env python3

from carta.constants import Overlay
from carta.constants import PaletteColor
from toVector import ToVector
import sys


class Layers:
    """"This object encasulates all the bitmap layers from a CARTA session.
    
    This class provides a classmethod which extracts bitmap layers from a CARTA user session.

    The Layers object is create when the class method is executed

    Parameters
    ----------
    rasterList : list 
        The list is returned with decoded PNG images in byte format
    vectorList : list
        The list is returned with ToVector objects.

    Attributes
    ----------
    OVER_CCOMPONENTS : list
        This is a class list accessible to all instances of this class
        Contains a list of obj:`carta.stores.OverlayStore to keep record of possible overlays
    """
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
        """Obtains bitmap layers from a CARTA session and sets them all to black.

        Bitmap layers which are not to be vectoriesed are kept in rasterList

        Bitmap layers which need to be vectorised are stored in obj; `ToVector` and added to vectorList

        Original color of each layer to be vectorised is stored 

        Parameters
        ----------
        sesssion : :obj:`carta.session`
            An active session from a user
        
        Returns
        -------
            obj:`Layers` which contains rasterList and vectorList
        """
        #Initialisation of empty lists and variables which will store data obtained 
        # from the invocation of the from_carta method
        rasterList = [] #List to store raster elements data
        vectorList = [] #List to store objects of data for vectorization
        visibleLayers = []  #List to keep track of all the visible elements within the active session
        ticksVisible = False    #Variable used to check is ticks are visible
        contours_visible = False    #Variable used to keep track of contours visibility
        backgroundColor = session.palette_to_rgb(PaletteColor.WHITE)

        #Store variable in current image view
        img = session.active_frame()

        #Loops through the component list to check which of the components are visible
        visibleLayers = [component for component in Layers.OVERLAY_COMPONENTS if session.visible(component)]  #Loop eliniataed, functional 

        #Checks if there are any ticks visible, then makes them less visible
        ticks_width = session.get_overlay_value(Overlay.TICKS, "width")

        #Loop hides all of the overlay components, except ticks
        for component in Layers.OVERLAY_COMPONENTS:
            session.hide(component)

        #Reduces the visibility of ticks in the session
        if ticks_width > 0.00001:
            ticksVisible = True
            session.call_overlay_action(Overlay.TICKS,"setWidth", 0.00001)


        #Checks whether the contours are visible in given image
        if (img.get_value("contourConfig.visible") == True) and (img.get_value("contourConfig.levels") != None):
            contours_visible = True
            img.hide_contours()
            
        #Append background image to raster list
        rasterList.append(session.rendered_view_data())
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
            img.hide_contours()
        

        #Loop through the visible overlay components
        #The colorbar is added to the raster list
        #The remaining visible layers are saved by invoking the saveLayer function
        for component in visibleLayers:
            if component != Overlay.COLORBAR:
                session.show(component)
            componentColor = session.color(component)
            if componentColor == None:
                originalColor = session.palette_to_rgb(session.color(Overlay.GLOBAL))
            else:
                originalColor = session.palette_to_rgb(componentColor)
            session.set_color(PaletteColor.BLACK, component)
            vectorList.append(ToVector(session.rendered_view_data(backgroundColor), originalColor))
            if componentColor == None:
                session.set_color(session.color(Overlay.GLOBAL), component)
            else:
                session.set_color(componentColor, component)
            session.hide(component)

        
        #Ticks width is adjusted to improve visibility
        #The ticks color is set to black before saving
        #Ticks color is set back to the original color
        if ticksVisible:
            session.call_overlay_action(Overlay.TICKS,"setWidth", ticks_width)
            ticksColor = session.color(Overlay.TICKS)
            if ticksColor != None:
                ticksRGB = session.palette_to_rgb(ticksColor)
            else:
                ticksRGB = session.palette_to_rgb(session.color(Overlay.GLOBAL))
            session.set_color(PaletteColor.BLACK, Overlay.TICKS)
            vectorList.append(ToVector(session.rendered_view_data(backgroundColor), ticksRGB))
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

        #returns an instance of the Layers class containing two lists
        return cls(rasterList, vectorList)
        
       
 