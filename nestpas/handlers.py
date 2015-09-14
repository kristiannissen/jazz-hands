import logging
import datetime
import os
import web
from web import form

from nestpas.config import Config
from nestpas.models import *

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
    # TODO: Make the content type depend on file extension
    web.header("Content-Type", "text/html")
    
    output = web.template.frender(template_file)
    return output(values)

class HomeHandler(BaseHandler):
  def GET(self):
    """ Show Home page """
    doc = Document.select().get()
    return self.render_view("Hello Kitty")

class DocumentHandler(BaseHandler):
  def GET(self, id=None):
    """ Get document """
    return self.render_view("Kitty says muuh", 'home.html')

class LoginHandler(BaseHandler):
  def GET(self):
    """ Show login form """
    loginform = self.get_form()
    
    return self.render_view(loginform)
  
  def POST(self):
    """ Process form submit """
    web.header("Content-Type", "text/html")
    return "Hello"
    
  def get_form(self):
    return form.Form(
      form.Textbox('mail'),
      form.Password('password'),
      form.Button('Login')
    )

class UserHandler(BaseHandler):
  def GET(self, id=None):
    """ User page """
    return self.render_view("Kitty")
