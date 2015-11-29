# -*- coding: utf-8 -*-
from peewee import *
import datetime
import re
import logging

from nestpas.config import Config
from nestpas.utils import *
# db = SqliteDatabase('db_nestpas.sqlite')

config = Config()

def get_db():
  if is_test():
    db = SqliteDatabase(config.get_settings_for('database')['development']['path'])
  else:
    db = None

  return db

class BaseModel(Model):
  class Meta:
    database = get_db()

class User(BaseModel):
  mail = CharField(null=True)
  password = CharField()

class Document(BaseModel):
  title = CharField(max_length=255)
  when_created = TimeField(default=datetime.datetime.now)
  when_changed = TimeField(null=True)
  body_text = TextField(null=True)
  # SomeUser.documents returns list of a users documents
  user = ForeignKeyField(User, related_name="documents")
  published = BooleanField(default=False)
  slug = CharField()

# db.connect()

def migrate():
  User.drop_table(True)
  User.create_table(True)

  Document.drop_table(True)
  Document.create_table(True)
