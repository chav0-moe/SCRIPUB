#!/usr/bin/env python3

import numpy as np
import os
from carta.session import Session

class ImageProcessor:

    def processor(self, sessionObj):

        #Save open raster image
        sessionObj.save_rendered_view("rendered_raster.png")

        sessionObj.call_action("overlayStore.colorbar.setVisible", False)

        #TODO use if statements to check if the added elements are visible
        Dict = {'Global': sessionObj.get_value("overlayStore.global.visible"), 'Title': sessionObj.get_value("overlayStore.title.visible"), 'Grid': sessionObj.get_value("overlayStore.grid.visible"), 'Border': sessionObj.get_value("overlayStore.border.visible"), 'Axes': sessionObj.get_value("overlayStore.axes.visible"), 'Numbers': sessionObj.get_value("overlayStore.numbers.visible"), 'Labels': sessionObj.get_value("overlayStore.labels.visible"), 'Beam': sessionObj.get_value("overlayStore.beam.visible")}

        img = sessionObj.active_frame()

        img.hide_contours()

        if Dict['Global'] != 0:
            sessionObj.hide(Overlay.GLOBAL)
        
        if Dict['Title'] != 0:
            sessionObj.hide(Overlay.TITLE)

        if Dict['Grid'] != 0:
            sessionObj.hide(Overlay.GRID)

        if Dict['Border'] != 0:
            sessionObj.hide(Overlay.BORDER)

        if Dict['Axes'] != 0:
            sessionObj.hide(Overlay.AXES)

        if Dict['Numbers'] != 0:
            sessionObj.hide(Overlay.NUMBERS)

        if Dict['Beam'] != 0:
            sessionObj.hide(Overlay.BEAM)

        if Dict['Labels'] != 0:
            sessionObj.hide(Overlay.LABELS)

        sessionObj.save_rendered_view("background_raster.png")

        img.hide_raster()

        img.show_contours()
        sessionObj.save_rendered_view("contours.png")
        img.hide_contours()

        if Dict['Global'] != 0:
            sessionObj.show(Overlay.GLOBAL)
            sessionObj.save_rendered_view("global.png")
            sessionObj.hide(Overlay.GLOBAL)
        
        if Dict['Title'] != 0:
            sessionObj.show(Overlay.TITLE)
            sessionObj.save_rendered_view("title.png")
            sessionObj.hide(Overlay.TITLE)

        if Dict['Grid'] != 0:
            sessionObj.show(Overlay.GRID)
            sessionObj.save_rendered_view("grid.png")
            sessionObj.hide(Overlay.GRID)

        if Dict['Border'] != 0:
            sessionObj.show(Overlay.BORDER)
            sessionObj.save_rendered_view("border.png")
            sessionObj.hide(Overlay.BORDER)

        if Dict['Axes'] != 0:
            sessionObj.show(Overlay.AXES)
            sessionObj.save_rendered_view("axes.png")
            sessionObj.hide(Overlay.AXES)

        if Dict['Numbers'] != 0:
            sessionObj.show(Overlay.NUMBERS)
            sessionObj.save_rendered_view("numbers.png")
            sessionObj.hide(Overlay.NUMBERS)

        if Dict['Beam'] != 0:
            sessionObj.show(Overlay.BEAM)
            sessionObj.save_rendered_view("beam.png")
            sessionObj.hide(Overlay.BEAM)

        if Dict['Labels'] != 0:
            sessionObj.show(Overlay.LABELS)
            sessionObj.save_rendered_view("labels.png")
            sessionObj.hide(Overlay.LABELS)

        #Configuring the contours
        levels = np.arange(5, 5 * 5, 4)
        img = sessionObj.img.configure_contours(levels)
        img.apply_contours()
