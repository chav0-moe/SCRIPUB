from carta.session import Session
from layers import Layers
from combined_img import combined_img
import sys

session = Session.interact(sys.argv[1], sys.argv[2])
#session = Session.interact("http://192.168.1.106:3002/?token=34fe6d76-b36a-4697-aa81-4e75e5421a1f", 2077054659)

img = session.open_image(r"test_image.fits")

#com = combined_img.original_from_session()

com = combined_img.from_session(session)

com.to_svg('created_vector.svg')