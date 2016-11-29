# -*- coding: utf-8 -*-
import logging
import datetime
import os
import web
import hashlib
from web import session

from nestpas.config import Config
from nestpas.models import *

def logged_in():
    if session.logged_in:
        return True
    else:
        return False

class RenderHelper(object):
    def __init__(self):
        # TODO: Add try catch
        self.settings = Config().get_settings_for('templates')

    def render_with_layout(self):
        # TODO: Add try catch
        render = web.template.render(self.settings['path'],
                                base=self.settings['layout'])
        return render

    def render_with_admin(self):
        render = web.template.render(self.settings['path'],
                                base="admin")
        return render

class Index(RenderHelper):
    def GET(self):
        """ Index page """
        render = self.render_with_layout()
        return render.home('Hello, Pussy')

class Login(RenderHelper):
    def GET(self):
        """ Serves login form """
        remember = web.cookies()
        if remember['remember-me']:
            user = User.get(User.hashed_key == remember['hashed_key'])
            if user:
                session.logged_in = True
                session.user_mail = user.mail
                raise web.seeother('/admin/latest')

        render = self.render_with_layout()
        return render.login({})

    def POST(self):
        """ Handles form post """
        inp = web.input()
        user = User.get((User.mail == inp.user_mail) & (User.password == inp.user_pwd))
        # FIXME: Hash remember and store in DB
        if inp.user_remember == '1':
            web.setcookie('remember-me', hashlib.md5(user.mail).hexdigest(), 3600)
            user.hashed_key = hashlib.md5(user.mail).hexdigest()
            user.save()

        if user:
            session.logged_in = True
            session.user_mail = user.mail
            raise web.seeother("/admin/latest")
        else:
            render = self.render_with_layout()
            return render.login({})

class Latest(RenderHelper):
    def GET(self):
        if logged_in():
            render = self.render_with_admin()
            return render.latest({'user_mail': session.user_mail})
        else:
            raise web.seeother("/adgang")

class Document(RenderHelper):
    def GET(self):
        render = self.render_with_admin()
        return render.document_form({})


