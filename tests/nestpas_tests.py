from nose.tools import *
from paste.fixture import TestApp

from nestpas.config import Config
from nestpas.models import *
from nestpas.router import Router
from nestpas.handlers import *
from myapp import app

import logging
import re

def setup_func():
    migrate()
  
    test_user = User(mail="chunkylover53@aol.com", password="chunkylover53")
    test_user.save()

def teardown_func():
    pass

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

@with_setup(setup_func, teardown_func)
def test_user_mail():
    test_mail = "chunkylover53@aol.com"
    user = User.get(User.mail == test_mail)
  
    assert_equal(user.mail, test_mail)

@with_setup(setup_func, teardown_func)
def test_document_title():
    test_user = User.get(User.mail == "chunkylover53@aol.com")
  
    test_title = "Hello Kitty"
    # TODO: Better way of handling slugs
    doc = Document(title=test_title, user=test_user, slug=re.sub(r'[^a-z0-9]', '-', test_title.lower()))
    doc.save()
  
    assert_equal(doc.title, test_title)

@with_setup(setup_func, teardown_func)
def test_user_documents():
    test_user = User.get(User.mail == "chunkylover53@aol.com")
  
    for i in [1,2,3,4,5]:
        test_title = "Hello Kitty no %d" % i
        doc = Document(title=test_title, user=test_user)
        doc.slug = re.sub(r'[^a-z0-9]', '-', test_title.lower())
        doc.save()
  
    assert_equal(test_user.documents.count(), 5)

def test_handlers_index():
    mw = []
    testApp = TestApp(app.wsgifunc(*mw))
    req = testApp.get('/')

    assert_equal(req.status, 200)

    req.mustcontain('Hello Kitty')

def test_handlers_login_get_post():
    pass
    # GET
    # testApp = TestApp(app.wsgifunc(*[]))
    # req = testApp.get('/login/')
    # assert_equal(req.status, 200)
    # req.mustcontain("Login")
    # POST
    # req = testApp.post('/login/', params = {
    #    'mail': 'chunkylover53@aol.com',
    #    'password': 'chunkylover53'
    #})
    # assert_equal(req.status, 200)
    # req.mustcontain("Hello")

