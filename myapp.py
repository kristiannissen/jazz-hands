# -*- coding: utf-8 -*-
import web
import logging

from livereload import Server

from nestpas import models
from nestpas.router import Router
from nestpas.handlers import *
from nestpas.utils import *

web.config.debug = True

app = web.application(Router().get_routes(), globals())

def connection_processor(handler):
    db = models.get_db()
    try:
        return handler()
    finally:
        if not db.is_closed():
            db.close()

app.add_processor(connection_processor)

if is_test():
    web.webapi.internalerror = web.debugerror

if (__name__ == "__main__"):
    app.run()

