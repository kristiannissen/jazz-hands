from livereload import Server

import web

from nestpas.views import *
from nestpas.urls import *
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# web.config.debug = False
web.ctx.debug = False

app = web.application(urls, globals(), autoreload=False)
webapp = app.wsgifunc()

# Setup session storage
db = web.database(dbn='sqlite', db='dev.db')
store = web.session.DBStore(db, 'sessions')
session = web.session.Session(app, store,
    initializer={'login': 0}
)

if __name__ == '__main__':
    ## app.run()
    server = Server(webapp)
    server.watch('static/', 'templates/', 'nestpas/')
    server.serve(port=8080, host='localhost')
