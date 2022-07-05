#!/usr/bin/env python3

from carta.session import Session
from carta.browser import Chrome
import sys


imagePath = sys.argv[1]

session = Session.start_and_create(Chrome())

img = session.open_image(imagePath)

session.save_rendered_view("rendered_raster.png")

img.configure_contours([-3.22,23.28,49.78,76.28,102.78])
img.apply_contours()
img.show_contours()
img.hide_raster()

session.save_rendered_view("rendered_contours.png","white")
