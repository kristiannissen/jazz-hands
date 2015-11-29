import os

def is_test():
  if 'WEBPY_ENV' in os.environ:
    return os.environ['WEBPY_ENV'] == 'test'
