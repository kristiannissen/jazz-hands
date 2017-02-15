from livereload import Server

import web

from nestpas.views import *
from nestpas.urls import *
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


app = web.application(urls, globals())
webapp = app.wsgifunc()

# Setup session storage
db = web.database(dbn='sqlite', db='dev.db')
store = web.session.DBStore(db, 'sessions')
session = web.session.Session(app, store,
    initializer={'auth': 0}
)

def session_hook():
    web.ctx.session = session
    web.template.Template.globals['session'] = session

app.add_processor(web.loadhook(session_hook))

if __name__ == '__main__':
    # app.run()

    static_app = web.httpserver.StaticMiddleware(webapp)
    server = Server(static_app)
    server.watch('static/', 'templates/', 'nestpas/')
    server.serve(port=8080, host='localhost')
