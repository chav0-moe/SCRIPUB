#!/usr/bin/env python3

from carta.constants import Overlay


def processor(session):
    #TODO create a list of overlay elements to help with iteration

    #Dictionary to store the layers
    visible = {'Title': session.get_overlay_value(Overlay.TITLE,"overlaystore.title"), 'Grid': session.get_overlay_value(Overlay.GRID,"overlaystore.grid"), 'Border': session.get_overlay_value(Overlay.BORDER, "overlaystore.border"), 'Axes': session.get_overlay_value(Overlay.AXES, "overlaystore.axes"), 'Numbers': session.get_overlay_value(Overlay.NUMBERS, "overlaystore.numbers"), 'Labels': session.get_overlay_value(Overlay.LABELS, "overlaystore.labels"), 'Beam': session.get_overlay_value(Overlay.BEAM, "overlaystore.beam"), 'Ticks': session.get_overlay_value(Overlay.TICKS, "overlaystore.ticks"), 'ColorBar': session.get_overlay_value(Overlay.COLORBAR, "overlaystore.colorbar")}
    #TODO explore other components contained within the colorbar

    #Store variable for image in current session
    img = session.active_frame()
        

    #TODO use if statements to check if the added elements are visible

    img.hide_contours()

        
    if visible['Title']:
        session.hide(Overlay.TITLE)

    if visible['Grid']:
        session.hide(Overlay.GRID)

    if visible['Border']:
        session.hide(Overlay.BORDER)

    if visible['Axes']:
        session.hide(Overlay.AXES)

    if visible['Numbers']:
        session.hide(Overlay.NUMBERS)

    if visible['Beam']:
        session.hide(Overlay.BEAM)

    if visible['Labels']:
        session.hide(Overlay.LABELS)

    if visible['ColorBar']:
        session.hide(Overlay.COLORBAR)

    session.call_overlay_action(Overlay.TICKS,"setWidth", 0.0001)

    #TODO create a list to add elements into
    layers = []
    #TODO create a list where the visible elements can be mapped to the exsisting ones

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
        
    #Title
    if visible['Title']:
        session.show(Overlay.TITLE)
        title = session.rendered_view_data()
        layers.append(title)
        #sessionObj.save_rendered_view("title.png")
        session.hide(Overlay.TITLE)

    #Grid
    if visible['Grid']:
        session.show(Overlay.GRID)
        grid = session.rendered_view_data()
        layers.append(grid)
        #sessionObj.save_rendered_view("grid.png")
        session.hide(Overlay.GRID)

    #Border
    if visible['Border']:
        session.show(Overlay.BORDER)
        border = session.rendered_view_data()
        layers.append(border)
        #sessionObj.save_rendered_view("border.png")
        session.hide(Overlay.BORDER)

    #Axes
    if visible['Axes']:
        session.show(Overlay.AXES)
        axes = session.rendered_view_data()
        layers.append(axes)
        #sessionObj.save_rendered_view("axes.png")
        session.hide(Overlay.AXES)

    #Numbers
    if visible['Numbers']:
        session.show(Overlay.NUMBERS)
        numbers = session.rendered_view_data()
        layers.append(numbers)
        #sessionObj.save_rendered_view("numbers.png")
        session.hide(Overlay.NUMBERS)

    #Beam
    if visible['Beam']:
        session.show(Overlay.BEAM)
        beam = session.rendered_view_data()
        layers.append(beam)
        #sessionObj.save_rendered_view("beam.png")
        session.hide(Overlay.BEAM)

    #Labels
    if visible['Labels']:
        session.show(Overlay.LABELS)
        labels = session.rendered_view_data()
        layers.append(labels)
        #sessionObj.save_rendered_view("labels.png")
        session.hide(Overlay.LABELS)

    #Ticks
    if visible['Ticks']:
        ticksWidth = visible['Ticks']
        ticks = session.call_overlay_action(Overlay.TICKS,"setWidth", ticksWidth)
        layers.append(ticks)

    return layers