from carta.session import Session
from carta.token import BackendToken
from carta.browser import Chrome

class Create:

    def _init_(self, fitsImage):
        self.fitsImage = fitsImage



# New session, connect to an existing backend
    #session = Session.create(Chrome(), "FRONTEND URL", BackendToken("SECURITY TOKEN"))

# New session, start local backend
    session = Session.start_and_create(Chrome())

# New session, start remote backend
    #session = Session.start_and_create(Chrome(), remote_host="REMOTE HOSTNAME OR IP")

# Opening image in CARTA
    img = session.open_image(fitsImage)

#Saving rendered image
    session.save_rendered_view("rendered.png")