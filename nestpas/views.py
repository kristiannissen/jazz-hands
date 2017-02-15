# -*- coding: utf-8 -*-
import sys
import hashlib
import web
import json
import markdown
import logging
from nestpas.models import *
from nestpas.utils import *

# View contacts
TEMPLATE_ADMIN = "admin"
TEMPTATE_FRONT = "layout"
HASH_SALT = "supersecrethashsalt"


t_globals = {
    'markdown': markdown.markdown
}
render = web.template.render(globals=t_globals, base="layout")


class Index:
    def GET(self):
        """ Index view """
        posts = BlogPost.select().where(BlogPost.online == 1).order_by(
                BlogPost.when_created.desc()
            ).paginate(0, 10)

        return render.index({
                "posts": posts
            })


class Blog:
    def GET(self, post_slug):
        """ Render single post """
        try:
            post = BlogPost.get(BlogPost.slug == post_slug)
        except DoesNotExist:
            raise web.seeother("/go-away")

        return render.post({
                "blogpost_title": post.title,
                "blogpost_content": post.content,
                "blogpost_teaser": post.teaser
            })


def authenticate(func):
    """ If auth isn't in session or auth isn't 1
        redirect to login
    """
    def func_wrapper(*args, **kwargs):
        if "auth" in web.ctx.session == False or web.ctx.session.get("auth", 0) == 0:
            raise web.seeother("/login/")

        return func(*args, **kwargs)

    return func_wrapper


class Admin:

    @authenticate
    def GET(self):
        """ Admin """
        posts = BlogPost.select().order_by(
                BlogPost.when_created.desc()
            ).paginate(0, 10)

        render = web.template.render(base="admin")
        return render.latest({
            "user_mail": "Kitty {}".format(web.ctx.session),
            "blog_posts": posts
        })


class Entry:

    @authenticate
    def GET(self, blog_id=None):
        """ Blog """
        if blog_id is None:
            """ Create a new BlogPost """
            post = BlogPost(title="", content="")
        else:
            """ Exit existing BlogPost """
            post = BlogPost.get(BlogPost.id == blog_id)

        mediafiles = MediaFile.select().order_by(MediaFile.id).limit(10)

        render = web.template.render(base="admin")
        return render.blog({
            "blog_id": post.id,
            "blog_title": post.title,
            "blog_theme": post.theme_image,
            "blog_content": post.content,
            "blog_online": post.online,
            "media_files": mediafiles,
            "send_as_newsletter": post.send_as_newsletter
        })

    @authenticate
    def POST(self, blog_id=None):
        """ Handle creating and editing blog posts """
        inp = web.input()
        logging.debug(inp)
        logging.debug(blog_id)

        if blog_id:
            blogpost = BlogPost.get(BlogPost.id == blog_id)
        else:
            blogpost = BlogPost()

        blogpost.title = inp.blog_title
        blogpost.content = inp.blog_content
        blogpost.slug = slugify(blogpost.title)

        if 'blog_online' in inp:
            blogpost.online = 1
        else:
            blogpost.online = 0

        if 'send_as_newsletter' in inp:
            blogpost.send_as_newsletter = True
        else:
            blogpost.send_as_newsletter = False

        blogpost.save()

        web.header("Content_Type", "application/json; charset=utf=8")
        return json.dumps(
            {"blog_id": blogpost.id, "blog_slug": blogpost.slug},
            sort_keys=True, indent=4, separators=(",", ": "))


class Media:

    @authenticate
    def GET(self):
        """ Media """
        render = web.template.render(base="admin")
        return render.media({})

    @authenticate
    def POST(self):
        inp = web.input(media_file={})
        # FIXME: get real path
        filedir = '/Users/kristiannissen/Documents/python/jazz-hands/static'
        if 'media_file' in inp:
            filepath = inp.media_file.filename.replace('\\', '/')
            filename = filepath.split('/')[-1]

            fout = open("{0}/{1}".format(filedir, filename), 'w')
            fout.write(inp.media_file.file.read())
            fout.close()

            MediaFile.create(filepath=filename)

        raise web.seeother('/media/')


class Login:
    def GET(self):
        """ Login """
        cookies = web.cookies()

        render = web.template.render(base="admin")
        return render.login({})

    def POST(self):
        """ Handle login """
        inp = web.input()
        # FIXME: Use const for cookie lifetime and hash secret
        if 'user_mail' in inp and 'user_pwd' in inp:
            try:
                user = User.get(
                    User.mail == inp.user_mail,
                    User.password == inp.user_pwd
                )
                logging.info("Login by user {}".format(user.id))
                web.setcookie(
                    '_k',
                    hashlib.md5(
                        "{0}-{1}".format(HASH_SALT, inp.user_mail)
                    ).hexdigest(),
                    360000
                )
                web.ctx.session.auth = 1

                raise web.seeother("/admin/")
            except DoesNotExist:
                # User not found in DB
                logging.warning("Login attempt")
                raise web.seeother("/login/")   
        else:
            # Form params not present
            raise web.seeother("/login/")


class Logout:

    @authenticate
    def GET(self):
        """ Logout """
        web.ctx.session.kill()
        web.setcookie(
            '_k',
            '',
            -1
        )
        web.ctx.session.auth = 0
        raise web.seeother("/login/")
