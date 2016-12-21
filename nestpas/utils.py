# -*- coding: utf-8 -*-
import os
import sys
import web
import re
import unidecode


def is_test():
    if 'WEBPY_ENV' in os.environ:
        web.config.debug = True

    return os.environ['WEBPY_ENV'] == 'test'


def slugify(text):
    text = unidecode.unidecode(text).lower()
    return re.sub(r'\W+', '-', text)
