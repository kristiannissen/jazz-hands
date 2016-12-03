import web

from nestpas.views import *
from nestpas.urls import *
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# web.config.debug = False

app = web.application(urls, globals(), autoreload = True)

if not web.config.get('session'):
    init = {'auth': ''}
    store = web.session.DiskStore('./sessions')
    session = web.session.Session(app, store, initializer = init)
    web.config.session = session
else:
    session = web.config.session

if __name__ == '__main__':
    app.run()

