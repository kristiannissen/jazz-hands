# -*- coding: utf-8 -*-
import web
import logging

from nestpas import models
from nestpas.config import Config
from nestpas.router import Router
from nestpas.handlers import *
from nestpas.utils import *

app = web.application(Router().get_routes(), globals())

def connection_processor(handler):
    db = models.get_db()
    try:
        return handler()
    finally:
        if not db.is_closed():
            db.close()

app.add_processor(connection_processor)

if (__name__ == "__main__"):
    app.run()
