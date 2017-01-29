# -*- coding: utf-8 -*-
from peewee import *
import datetime
import re
import logging

from nestpas.config import Config
from nestpas.utils import *

config = Config()


def get_db():
    return SqliteDatabase('dev.db', threadlocals=True)


class MyBaseModel(Model):
    class Meta:
        database = get_db()


class User(MyBaseModel):
    mail = CharField(null=True)
    password = CharField()
    hashed_key = CharField()


class BlogPost(MyBaseModel):
    title = CharField(max_length=255)
    theme_image = CharField(max_length=255, null=True)
    when_created = TimeField(default=datetime.datetime.now)
    when_changed = TimeField(null=True)
    content = TextField(null=True)
    online = IntegerField(default=0)
    slug = CharField()
    send_as_newsletter = BooleanField(default=False)

    @property
    def teaser(self):
        words = self.content.split()
        return " ".join(words[:20])

    @property
    def when_published(self):
        return self.when_created.strftime('%d %m %Y')


class MediaFile(MyBaseModel):
    filepath = CharField(max_length=255)
    mimetype = CharField(max_length=255, null=True)


class Newsletter(MyBaseModel):
    user = ForeignKeyField(User, related_name='subscriber')
    blogpost = ForeignKeyField(BlogPost, related_name='message')


def migrate():
    User.drop_table(True)
    User.create_table(True)

    BlogPost.drop_table(True)
    BlogPost.create_table(True)

    MediaFile.drop_table(True)
    MediaFile.create_table(True)

    Newsletter.drop_table(True)
    Newsletter.create_table(True)
