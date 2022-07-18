#!/usr/bin/env python3

from extractedLayers import ExtractedLayers
from .constants import Overlay

class ImageProcessor:

    def processor(self, sessionObj):
        #Dictionary to store the layers
        dic = {'Title': sessionObj.get_value("overlayStore.title.visible"), 'Grid': sessionObj.get_value("overlayStore.grid.visible"), 'Border': sessionObj.get_value("overlayStore.border.visible"), 'Axes': sessionObj.get_value("overlayStore.axes.visible"), 'Numbers': sessionObj.get_value("overlayStore.numbers.visible"), 'Labels': sessionObj.get_value("overlayStore.labels.visible"), 'Beam': sessionObj.get_value("overlayStore.beam.visible"), 'Ticks': sessionObj.get_value("overlayStore.ticks.visible")}

        #Store variable for image in current session
        img = sessionObj.active_frame()
        #Save edited image in session
        def save_raster():
            sessionObj.save_rendered_view("rendered_raster.png")

        def remove_colorbar():
            sessionObj.call_action("overlayStore.colorbar.setVisible", False)

        #TODO use if statements to check if the added elements are visible

        def hide_layers():
            img.hide_contours()
        
            if dic['Title']:
                sessionObj.hide(Overlay.TITLE)

            if dic['Grid']:
                sessionObj.hide(Overlay.GRID)

            if dic['Border']:
                sessionObj.hide(Overlay.BORDER)

            if dic['Axes']:
                sessionObj.hide(Overlay.AXES)

            if dic['Numbers']:
                sessionObj.hide(Overlay.NUMBERS)

            if dic['Beam']:
                sessionObj.hide(Overlay.BEAM)

            if dic['Labels']:
                sessionObj.hide(Overlay.LABELS)

            sessionObj.call_action("overlayStore.ticks.setWidth", 0.0001)

        save_raster()
        remove_colorbar()
        hide_layers()
        #Store variable for the background raster image
        backgroundImg = sessionObj.active_frame()
        #sessionObj.save_rendered_view("background_raster.png")
        img.hide_raster()

        #Contours
        img.show_contours()
        contours = sessionObj.active_frame()
        #sessionObj.save_rendered_view("contours.png")
        img.hide_contours()
        
        #Title
        if dic['Title'] != 0:
            sessionObj.show(Overlay.TITLE)
            title = sessionObj.active_frame()
            #sessionObj.save_rendered_view("title.png")
            sessionObj.hide(Overlay.TITLE)

        #Grid
        if dic['Grid'] != 0:
            sessionObj.show(Overlay.GRID)
            grid = sessionObj.active_frame()
            #sessionObj.save_rendered_view("grid.png")
            sessionObj.hide(Overlay.GRID)

        #Border
        if dic['Border'] != 0:
            sessionObj.show(Overlay.BORDER)
            border = sessionObj.active_frame()
            #sessionObj.save_rendered_view("border.png")
            sessionObj.hide(Overlay.BORDER)

        #Axes
        if dic['Axes'] != 0:
            sessionObj.show(Overlay.AXES)
            axes = sessionObj.active_frame()
            #sessionObj.save_rendered_view("axes.png")
            sessionObj.hide(Overlay.AXES)

        #Numbers
        if dic['Numbers'] != 0:
            sessionObj.show(Overlay.NUMBERS)
            numbers = sessionObj.active_frame()
            #sessionObj.save_rendered_view("numbers.png")
            sessionObj.hide(Overlay.NUMBERS)

        #Beam
        if dic['Beam'] != 0:
            sessionObj.show(Overlay.BEAM)
            beam = sessionObj.active_frame()
            #sessionObj.save_rendered_view("beam.png")
            sessionObj.hide(Overlay.BEAM)

        #Labels
        if dic['Labels'] != 0:
            sessionObj.show(Overlay.LABELS)
            labels = sessionObj.active_frame()
            #sessionObj.save_rendered_view("labels.png")
            sessionObj.hide(Overlay.LABELS)

        #Ticks
        ticks = sessionObj.call_action("overlayStore.ticks.setWidth", dic['Ticks'])

        layers = ExtractedLayers(backgroundImg, contours, title, grid, border, axes, numbers, beam, labels, ticks)

        return layers
        
