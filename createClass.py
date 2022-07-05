#!/usr/bin/env python3

from carta.session import Session
from carta.token import BackendToken
from carta.browser import Chrome


class Create:


    def __init__(self, fitsImage):
        self.fitsImage = fitsImage


# New session, start local backend
    def startSession(self):
        session = Session.start_and_create(Chrome())


# Opening image in CARTA
    def openImage(self):
        img = session.open_image(fitsImage)

#Saving rendered image
    def saveRaster(self):
        session.save_rendered_view("rendered_raster.png")

#Adding contours
    def addContours(self):
        session.configure_contours([-3.22,23.28,49.78,76.28,102.78])
        session.apply_contours()
        session.show_contours()
        session.hide_raster()

#Save image contours
    def saveContours(self):
        session.save_rendered_view("rendered_contours.png")

def main():
    startSession()
    openImage()
    saveRaster()
    addContours()
    saveContours()


if __name__ == "__main__":
    ImagePath = input("Please enter image path:")
    image = Create(ImagePath)
    main()