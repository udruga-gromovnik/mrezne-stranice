#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gromovnik'
SITENAME = u'Udruga "Gromovnik"'
SITESUBTITLE = u'Mrežne stranice udruge "Gromovnik" ("Gromovnik" association web site)'
SITEURL = 'https://www.gromovnik.hr'

PATH = 'content'

TIMEZONE = 'Europe/Zagreb'

DEFAULT_LANG = u'hr'

THEME = '../pelican-alchemy/alchemy'
THEME_CSS_OVERRIDES = ['theme/css/gromovnik.css']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Anno Domini na Facebooku', 'https://www.facebook.com/AnnoDominiProject/'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/UdrugaGromovnik/'),)

ICONS = (('facebook', 'https://www.facebook.com/UdrugaGromovnik/'),)

DEFAULT_PAGINATION = 10

# URL settings
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/index.html'

YEAR_ARCHIVE_URL = 'archive/{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/index.html'

MONTH_ARCHIVE_URL = 'archive/{date:%Y}/{date:%m}/'
MONTH_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/{date:%m}/index.html'

ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

CATEGORIES_URL = 'categories/'
CATEGORIES_SAVE_AS = 'categories/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

AUTHORS_URL = 'authors/'
AUTHORS_SAVE_AS = 'authors/index.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
