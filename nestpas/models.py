# -*- coding: utf-8 -*-
from peewee import *
import datetime
import re
import logging

from nestpas.config import Config
from nestpas.utils import *

config = Config()

def get_db():
    return SqliteDatabase('dev.db', threadlocals = True)


class MyBaseModel(Model):
    class Meta:
        database = get_db()

class User(MyBaseModel):
    mail = CharField(null=True)
    password = CharField()
    hashed_key = CharField()

class BlogPost(MyBaseModel):
    title = CharField(max_length=255)
    when_created = TimeField(default=datetime.datetime.now)
    when_changed = TimeField(null=True)
    content = TextField(null=True)
    # SomeUser.documents returns list of a users documents
    # user = ForeignKeyField(User, related_name="blogposts")
    published = BooleanField(default=False)
    slug = CharField()

# get_db().connect()

def migrate():
    User.drop_table(True)
    User.create_table(True)
 
    BlogPost.drop_table(True)
    BlogPost.create_table(True)

