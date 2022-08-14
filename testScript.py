from carta.session import Session
from layers import Layers

session = Session.interact("http://192.168.0.191:3002/?token=B84B9C09-660E-4708-9CF0-08AFB6D121DE", 3056068301)

img = session.open_image("/Users/tangwashihepo/Desktop/VecLib/WFPC2u5780205r_c0fx.fits.txt")

layerLists = Layers()

layers = layerLists.from_carta(session)

print(layers.rasterList)
print(layers.vectorList)
print(layers.originalColor)






