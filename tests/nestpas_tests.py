from nose.tools import *

from nestpas.config import Config
from nestpas.models.entities import *
from nestpas.router import Router
from nestpas.handlers import *

import logging
import re

def test_config_get_settings():
  conf = Config()
  assert_equal(type(conf.get_settings()), dict)

def test_config_get_settings_for():
  conf = Config()
  assert_equal(type(conf.get_settings_for('database')), dict)

def test_config_get_settings_for_none():
  conf = Config()
  setting = conf.get_settings_for('weird_stuff')
  assert_equal(setting, None)

def test_user_mail():
  test_mail = "chunkylover53@aol.com"
  user = User(mail=test_mail)
  user.save()
  
  assert_equal(user.mail, test_mail)

def test_document_title():
  test_user = User(mail="chunkylover53@aol.com")
  test_user.save()
  
  test_title = "Hello Kitty"
  doc = Document(title=test_title, user=test_user, slug=re.sub(r'[^a-z0-9]', '-', test_title.lower()))
  doc.save()
  
  assert_equal(doc.title, test_title)

def test_user_documents():
  test_user = User(mail="chunkylover53@aol.com")
  test_user.save()
  
  for i in [1,2,3,4,5]:
    test_title = "Hello Kitty no %d" % i
    doc = Document(title=test_title, user=test_user)
    doc.slug = re.sub(r'[^a-z0-9]', '-', test_title.lower())
    doc.save()
  
  assert_equal(test_user.documents.count(), 5)

def test_router():
  routes = Router().get_routes()
  
  assert_equal(type(routes), tuple)

def test_handlers_render():
  home = HomeHandler()
  
  assert_equal(hasattr(home, "render"), True)

def test_hanlders_render_template():
  home = HomeHandler()
  
  assert_not_equal(home.render().__class__, object)