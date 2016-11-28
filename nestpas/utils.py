# -*- coding: utf-8 -*-
import os
import sys
import web
from web import session

def is_test():
  if 'WEBPY_ENV' in os.environ:
    web.config.debug = True
    return os.environ['WEBPY_ENV'] == 'test'
