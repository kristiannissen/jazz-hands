# -*- coding: utf-8 -*-

import hashlib
import web
import json
import logging
from nestpas.models import *
from nestpas.utils import *

# View contacts
TEMPLATE_ADMIN = "admin"
TEMPTATE_FRONT = "layout"
HASH_SALT = "supersecrethashsalt"

class Index:
    def GET(self):
        """ Index view """
        return "Hello Kitty"


class Contact:
    def GET(self):
        """ Contact view """
        return "Contact"


class Newsletter:
    def GET(self):
        """ Newsletter """
        return "Newsletter"


class About:
    def GET(self):
        """ About """
        return "About"


class Admin:
    def GET(self):
        """ Admin """
        render = web.template.render(base="admin")
        return render.latest({
            "user_mail": "hello@kitty.com"
        })


class Blog:
    def GET(self, blog_id=None):
        """ Blog """
        logging.debug(blog_id)
        render = web.template.render(base="admin")
        return render.blog({})

    def POST(self, blog_id=None):
        """ Handle creating and editing blog posts """
        inp = web.input()
        logging.debug(inp)
        logging.debug(blog_id)

        blogpost = BlogPost(title = inp.blog_title, content = inp.blog_content,
            slug = slugify(inp.blog_title))
        blogpost.save()

        web.header("Content_Type", "application/json; charset=utf=8")
        return json.dumps({"blog_id": blogpost.id}, sort_keys=True, indent=4,
            separators=(",", ": "))


class Media:
    def GET(self):
        """ Media """
        render = web.template.render(base="admin")
        return render.media({})


class User:
    def GET(self):
        """ User """
        render = web.template.render(base="admin")
        return render.user({})


class Login:
    def GET(self):
        """ Login """
        cookies = web.cookies()
        logging.debug(cookies)

        render = web.template.render(base='layout')
        return render.login({})

    def POST(self):
        """ Handle login """
        inp = web.input()
        if inp.user_remember == '1':
            logging.debug("Remember me feature")
            # FIXME: Use const for cookie lifetime and hash secret
            web.setcookie('_k', hashlib.md5("{0}-{1}".format(HASH_SALT, inp.user_mail)).hexdigest(), 360000)

        return "Hello ADMIN"


class Logout:
    def GET(self):
        """ Logout """
        return "Logout"

