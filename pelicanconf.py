#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Grupo 51'
SITENAME = 'Tratamiento de imágenes 2023 - Proyecto final'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Montevideo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Facultad de Ingeniería', 'https://www.fing.edu.uy/'),
         ('Instituto de Ingeniería Eléctrica', 'https://iie.fing.edu.uy/'),
         ('Se pueden poner otros links en el pelicanconf', '#'),)

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# PLUGINS--------------------------------
# Where to look for plugins
PLUGIN_PATHS = ['pelican-plugins']  #['../pelican-plugins']
# Which plugins to enable
# PLUGIN PARA PONER NUMERO A LAS FIGURAS ->  figure-ref
#https://github.com/cmacmackin/figure-ref/tree/40e04d32bff468a6b3e63c373c5d95fca39783fe
PLUGINS = ['figure-ref']



# ORDENAR LAS PAGINAS EN EL MENU POR EL ATRUBUTO "Ordinal" -------
# si no, te quedan ordenadas alfabéticamente
PAGE_ORDER_BY = 'ordinal'