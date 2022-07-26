from carta.session import Session
from imageProcessor import processor

session = Session.interact("http://192.168.0.191:3002/?token=CE0A7228-1830-4D01-AE7C-3053AA4DCDC5", 517237617)

img = session.open_image("/Users/tangwashihepo/Desktop/VecLib/WFPC2u5780205r_c0fx.fits.txt")

extracted_layers = processor(session)

print(extracted_layers)


