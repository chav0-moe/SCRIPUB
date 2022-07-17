from carta.session import Session
from carta.token import BackendToken

session = Session.interact("http://192.168.0.191:3002/?token=C98642A9-1D93-43F3-8887-8CF562A073FD", 568728538)


img1 = session.open_image("/Users/tangwashihepo/Desktop/VecLib/WFPC2u5780205r_c0fx.fits.txt")
img2 = session.append_image("/Users/tangwashihepo/Desktop/VecLib/WFPC2ASSNu5780205bx.fits.txt")