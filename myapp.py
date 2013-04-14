import web
import logging

from nestpas import models
from nestpas.config import Config
from nestpas.router import Router
from nestpas.handlers import *

app = web.application(Router().get_routes(), globals())

def is_test():
  if 'WEBPY_ENV' in os.environ:
    return os.environ['WEBPY_ENV'] == 'test'

if (not is_test() and __name__ == "__main__"):
  app.run()
