from carta.session import Session
from carta.token import BackendToken
from carta.browser import Chrome

# New session, connect to an existing backend
#session = Session.create(Chrome(), "FRONTEND URL", BackendToken("SECURITY TOKEN"))

# New session, start local backend
session = Session.start_and_create(Chrome())

# New session, start remote backend
#session = Session.start_and_create(Chrome(), remote_host="REMOTE HOSTNAME OR IP")