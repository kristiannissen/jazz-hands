import logging
import datetime
import os
import web
from nestpas.config import Config

class BaseHandler:
  template_file = None
  file_extension = "html"
  
  def __init__(self, templates_folder=None):
    self.template_file = str(self.__class__).split(".").pop().lower().replace('handler', '')
    self.settings = Config().get_settings_for('templates')
  
  def render_view(self, values=None, file_name=None):
    if file_name:
      self.file_extension = file_name.split(".").pop()
      self.template_file = file_name.split(".").pop(0)
    
    template_folder = self.settings['path']
    template_file = "%s/%s.%s" % (template_folder, self.template_file, self.file_extension)
    
    output = web.template.frender(template_file)
    return output(values)

class HomeHandler:
  def GET(self):
    """ Show Home page """
    return "hello kitty"

class DocumentHandler(BaseHandler):
  def GET(self, id=None):
    """ Get document """
    return self.render_view("Kitty says muuh", 'home.html')
