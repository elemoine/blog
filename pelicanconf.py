#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Éric Lemoine'
SITENAME = 'Éric Lemoine'
SITEURL = 'https://erilem.net'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('Twitter', 'httsp://twitter.com/erilem'),
          ('GitHub', 'https://github.com/elemoine'),
          ('Google+', 'https://plus.google.com/u/1/101823398102994275785'),
          ('Linkedin', 'https://www.linkedin.com/in/erilem'))

DEFAULT_PAGINATION = 10

ARTICLE_EXCLUDES = ['cv']
STATIC_PATHS = ['cv/cv.en.html',
                'cv/cv.en.pdf',
                'cv/cv.css',
                'keybase.txt',
                'eric-lemoine-openpgp4fpr.png']
DEFAULT_CATEGORY = 'Blog'
MENUITEMS = [('Resume', '/cv/cv.en.html')]

RELATIVE_URLS = True
