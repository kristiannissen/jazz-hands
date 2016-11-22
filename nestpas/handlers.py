# -*- coding: utf-8 -*-
import logging
import datetime
import os
import web

from nestpas.config import Config
from nestpas.models import *

class RenderHelper(object):
    def __init__(self):
        # TODO: Add try catch
        self.settings = Config().get_settings_for('templates')

    def render_with_layout(self):
        # TODO: Add try catch
        render = web.template.render(self.settings['path'],
                                base=self.settings['layout'])
        return render

class Index(RenderHelper):
    def GET(self):
        """ Index page """
        render = self.render_with_layout()
        return render.home('Kitty')

