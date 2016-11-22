# -*- coding: utf-8 -*-

class Router(object):
    def __init__(self):
        self.urls = (
            '/', 'Index'
        )
  
    def get_routes(self):
        return self.urls
