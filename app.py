import web

from nestpas.views import *
from nestpas.urls import *
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# web.config.debug = False
web.ctx.debug = True

app = web.application(urls, globals(), autoreload=True)

if not web.config.get('_session'):
    init = {'auth': ''}
    store = web.session.DiskStore('./sessions')
    session = web.session.Session(app, store, initializer=init)
    web.config._session = session
else:
    session = web.config._session

if __name__ == '__main__':
    app.run()
