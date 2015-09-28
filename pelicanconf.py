#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Santiago Buczak'
SITENAME = u'Santiago Buczak - Sysadmin / DevOps'
SITEURL = 'http://cv.buczak.com.ar'

PATH = 'content'

TIMEZONE = 'America/Argentina/Buenos_Aires'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "/opt/webapps/cv/theme"
USER_LOGO_URL = SITEURL + "/images/profile_400x400.jpg"

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/santiago.buczak'),
          ('Twitter', 'http://twitter.com/the_elven'),
	  ('Github', 'https://github.com/the-elven-archer/'))

MARKUP = ['rst', 'md']
DEFAULT_PAGINATION = False

PDF_GENERATOR = True
PLUGIN_PATHS = ["/opt/webapps/pelican_commons/pelican-plugins"]
PLUGINS = ['pdf']

PDF_STYLE_PATH = "/usr/local/lib/python2.7/site-packages/rst2pdf/styles/"
PDF_STYLE = "kerning"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
