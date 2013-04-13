import web
import logging

from nestpas import models
from nestpas.config import Config
from nestpas.router import Router
from nestpas.handlers import *

app = web.application(Router().get_routes(), globals())

if __name__ == "__main__":
  app.run()
