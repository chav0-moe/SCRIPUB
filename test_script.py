from carta.session import Session
from combined_img import combined_img
from carta.constants import Overlay
import sys

                                #Test script that takes in the session's frontend URL and ID as command line arguments
session_loc = sys.argv[1]
session_id = sys.argv[2]

session = Session.interact(session_loc, session_id)

com = combined_img.from_session(session)
com.to_svg('created_vector.svg')