
from .constants import Overlay

class ImageProcessor:

    def processor(self, sessionObj):
        #Dictionary to store the layers
        dick = {'Title': sessionObj.get_value("overlayStore.title.visible"), 'Grid': sessionObj.get_value("overlayStore.grid.visible"), 'Border': sessionObj.get_value("overlayStore.border.visible"), 'Axes': sessionObj.get_value("overlayStore.axes.visible"), 'Numbers': sessionObj.get_value("overlayStore.numbers.visible"), 'Labels': sessionObj.get_value("overlayStore.labels.visible"), 'Beam': sessionObj.get_value("overlayStore.beam.visible")}

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
        
            if dick['Title']:
                sessionObj.hide(Overlay.TITLE)

            elif dick['Grid']:
                sessionObj.hide(Overlay.GRID)

            elif dick['Border']:
                sessionObj.hide(Overlay.BORDER)

            elif dick['Axes']:
                sessionObj.hide(Overlay.AXES)

            elif dick['Numbers']:
                sessionObj.hide(Overlay.NUMBERS)

            elif dick['Beam']:
                sessionObj.hide(Overlay.BEAM)

            elif dick['Labels']:
                sessionObj.hide(Overlay.LABELS)

            sessionObj.call_action("overlayStore.ticks.setWidth", 0.0001)

        #Store variable for the background raster image
        backgroundImg = sessionObj.active_frame()
        sessionObj.save_rendered_view("background_raster.png")
        img.hide_raster()

        #Contours
        img.show_contours()
        contours = sessionObj.active_frame()
        sessionObj.save_rendered_view("contours.png")
        img.hide_contours()
        
        #Title
        if dick['Title'] != 0:
            sessionObj.show(Overlay.TITLE)
            title = sessionObj.active_frame()
            sessionObj.save_rendered_view("title.png")
            sessionObj.hide(Overlay.TITLE)

        #Grid
        elif dick['Grid'] != 0:
            sessionObj.show(Overlay.GRID)
            grid = sessionObj.active_frame()
            sessionObj.save_rendered_view("grid.png")
            sessionObj.hide(Overlay.GRID)

        #Border
        elif dick['Border'] != 0:
            sessionObj.show(Overlay.BORDER)
            border = sessionObj.active_frame()
            sessionObj.save_rendered_view("border.png")
            sessionObj.hide(Overlay.BORDER)

        #Axes
        elif dick['Axes'] != 0:
            sessionObj.show(Overlay.AXES)
            axes = sessionObj.active_frame()
            sessionObj.save_rendered_view("axes.png")
            sessionObj.hide(Overlay.AXES)

        #Numbers
        elif dick['Numbers'] != 0:
            sessionObj.show(Overlay.NUMBERS)
            numbers = sessionObj.active_frame()
            sessionObj.save_rendered_view("numbers.png")
            sessionObj.hide(Overlay.NUMBERS)

        #Beam
        elif dick['Beam'] != 0:
            sessionObj.show(Overlay.BEAM)
            beam = sessionObj.active_frame()
            sessionObj.save_rendered_view("beam.png")
            sessionObj.hide(Overlay.BEAM)

        #Labels
        elif dick['Labels'] != 0:
            sessionObj.show(Overlay.LABELS)
            labels = sessionObj.active_frame()
            sessionObj.save_rendered_view("labels.png")
            sessionObj.hide(Overlay.LABELS)

        