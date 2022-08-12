from carta.session import Session
from imageProcessor import processor

session = Session.interact("http://196.24.158.179:3002/?token=4D266FF6-0B0B-45A0-B990-8E4B9AD9F4EA", 1567928931)

img = session.open_image("/Users/tangwashihepo/Desktop/VecLib/WFPC2u5780205r_c0fx.fits.txt")

extracted_layers = processor(session)

print(extracted_layers)






