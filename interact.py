from carta.session import Session
from carta.token import BackendToken
from fits2image.fits2image import Fits2image

session = Session.interact("http://192.168.0.191:3002/?token=A2A6BB1B-85E1-49B8-A17C-27F12324A9CE", 3273084350)

print("Forth line executed")

img1 = session.open_image("/Users/tangwashihepo/Desktop/Scripting/WFPC2u5780205r_c0fx.fits.txt")
img2 = session.append_image("/Users/tangwashihepo/Desktop/Scripting/WFPC2ASSNu5780205bx.fits.txt")

