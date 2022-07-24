#!/usr/bin/env python3

from carta.constants import Overlay

class ImageProcessor:

    def __init__(self, byteList):
        self.byteList = byteList

    def processor(self, sessionObj):
        #Dictionary to store the layers
        #TODO create a list of overlay elements to help with iteration
        visible = {'Title': sessionObj.get_overlay_value(Overlay.TITLE), 'Grid': sessionObj.get_overlay_value(Overlay.GRID), 'Border': sessionObj.get_overlay_value(Overlay.BORDER), 'Axes': sessionObj.get_overlay_value(Overlay.AXES), 'Numbers': sessionObj.get_overlay_value(Overlay.NUMBERS), 'Labels': sessionObj.get_overlay_value(Overlay.LABELS), 'Beam': sessionObj.get_overlay_value(Overlay.BEAMS), 'Ticks': sessionObj.get_overlay_value(Overlay.TICKS), 'ColorBar': sessionObj.get_overlay_value(Overlay.COLORBAR)}

        #Store variable for image in current session
        img = sessionObj.rendered_view_data()
        

        #TODO use if statements to check if the added elements are visible

        img.hide_contours()

        
        if visible['Title']:
            sessionObj.hide(Overlay.TITLE)

        if visible['Grid']:
            sessionObj.hide(Overlay.GRID)

        if visible['Border']:
            sessionObj.hide(Overlay.BORDER)

        if visible['Axes']:
            sessionObj.hide(Overlay.AXES)

        if visible['Numbers']:
            sessionObj.hide(Overlay.NUMBERS)

        if visible['Beam']:
            sessionObj.hide(Overlay.BEAM)

        if visible['Labels']:
            sessionObj.hide(Overlay.LABELS)

        if visible['ColorBar']:
            sessionObj.hide(Overlay.COLORBAR)

        sessionObj.call_overlay_action("overlayStore.ticks.setWidth", 0.0001)

        #TODO create a list to add elements into
        layers = []
        #TODO create a list where the visible elements can be mapped to the exsisting ones

        #Store variable for the background raster image
        backgroundImg = sessionObj.rendered_view_data()
        layers.append(backgroundImg)
        #sessionObj.save_rendered_view("background_raster.png")
        img.hide_raster()

        #Contours
        img.show_contours()
        contours = sessionObj.rendered_view_data()
        layers.append(contours)
        #sessionObj.save_rendered_view("contours.png")
        img.hide_contours()
        
        #Title
        if visible['Title']:
            sessionObj.show(Overlay.TITLE)
            title = sessionObj.rendered_view_data()
            layers.append(title)
            #sessionObj.save_rendered_view("title.png")
            sessionObj.hide(Overlay.TITLE)

        #Grid
        if visible['Grid']:
            sessionObj.show(Overlay.GRID)
            grid = sessionObj.rendered_view_data()
            layers.append(grid)
            #sessionObj.save_rendered_view("grid.png")
            sessionObj.hide(Overlay.GRID)

        #Border
        if visible['Border']:
            sessionObj.show(Overlay.BORDER)
            border = sessionObj.rendered_view_data()
            layers.append(border)
            #sessionObj.save_rendered_view("border.png")
            sessionObj.hide(Overlay.BORDER)

        #Axes
        if visible['Axes']:
            sessionObj.show(Overlay.AXES)
            axes = sessionObj.rendered_view_data()
            layers.append(axes)
            #sessionObj.save_rendered_view("axes.png")
            sessionObj.hide(Overlay.AXES)

        #Numbers
        if visible['Numbers']:
            sessionObj.show(Overlay.NUMBERS)
            numbers = sessionObj.rendered_view_data()
            layers.append(numbers)
            #sessionObj.save_rendered_view("numbers.png")
            sessionObj.hide(Overlay.NUMBERS)

        #Beam
        if visible['Beam']:
            sessionObj.show(Overlay.BEAM)
            beam = sessionObj.rendered_view_data()
            layers.append(beam)
            #sessionObj.save_rendered_view("beam.png")
            sessionObj.hide(Overlay.BEAM)

        #Labels
        if visible['Labels']:
            sessionObj.show(Overlay.LABELS)
            labels = sessionObj.rendered_view_data()
            layers.append(labels)
            #sessionObj.save_rendered_view("labels.png")
            sessionObj.hide(Overlay.LABELS)

        #Ticks
        ticks = sessionObj.call_action("overlayStore.ticks.setWidth", visible['Ticks'])
        layers.append(ticks)

        layersObj = ImageProcessor(layers)

        return layersObj