# -*- coding: utf-8 -*-

class Router(object):
    def __init__(self):
        self.urls = (
            '/', 'Index',
            '/adgang', 'Login',
            '/admin/latest', 'Latest'
        )
  
    def get_routes(self):
        return self.urls
