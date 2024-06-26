#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Juan Manuel Varela"
SITENAME = "Tratamiento de imágenes 2023 - Proyecto final"

PATH = "content"

TIMEZONE = "America/Montevideo"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Facultad de Ingeniería", "https://www.fing.edu.uy/"),
    ("Instituto de Ingeniería Eléctrica", "https://iie.fing.edu.uy/"),
)

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# PLUGINS--------------------------------
# Where to look for plugins
PLUGIN_PATHS = ["pelican-plugins"]  # ['../pelican-plugins']
# Which plugins to enable
# PLUGIN PARA PONER NUMERO A LAS FIGURAS ->  figure-ref
# https://github.com/cmacmackin/figure-ref/tree/40e04d32bff468a6b3e63c373c5d95fca39783fe
# PLUGIN PARA CITAS ->  pelican-cite
# https://github.com/VorpalBlade/pelican-cite
PLUGINS = ["figure-ref", "pelican-cite","render_math"]



# ORDENAR LAS PAGINAS EN EL MENU POR EL ATRUBUTO "Ordinal" -------
# si no, te quedan ordenadas alfabéticamente
PAGE_ORDER_BY = "ordinal"

# UBICACION DE bibtex que usa el plugin pelican-cite
PUBLICATIONS_SRC = "content/biblio.bib"


# CAMBIAR EL ASPECTO
# Usar uno de los 'themes' de :  https://github.com/getpelican/pelican-themes
#THEME = "<sustituir por la ubicacion>/pelican-themes/tuxlite_zf"
#THEME = "<sustituir por la ubicacion>/pelican-themes/tuxlite_tbs"
#THEME = "<sustituir por la ubicacion>/pelican-themes/mnmlist"
#THEME = "<sustituir por la ubicacion>/pelican-themes/gum"
THEME = "content/theme/elegant"

# Landing Page
PROJECTS_TITLE = "Secciones"
PROJECTS = [
    {
        "name": "Introducción",
        "url": "https://juan.manuel.varela.pages.fing.edu.uy/proyecto-timag/pages/introduccion.html",
        "description": "",
    },
    {
        "name": "Dataset",
        "url": "https://juan.manuel.varela.pages.fing.edu.uy/proyecto-timag/pages/dataset.html",
        "description": "",
    },
    {
        "name": "Procedimiento",
        "url": "https://juan.manuel.varela.pages.fing.edu.uy/proyecto-timag/pages/procedimiento.html",
        "description": "",
    },
    {
        "name": "Experimentos",
        "url": "https://juan.manuel.varela.pages.fing.edu.uy/proyecto-timag/pages/experimentos.html",
        "description": "",
    },
    {
        "name": "Conclusiones",
        "url": "https://juan.manuel.varela.pages.fing.edu.uy/proyecto-timag/pages/conclusiones.html",
        "description": "",
    },
    {
        "name": "Acerca de...",
        "url": "https://juan.manuel.varela.pages.fing.edu.uy/proyecto-timag/pages/acerca-de.html",
        "description": "",
    },
]


LANDING_PAGE_TITLE = "ANALISIS DE CULTIVOS MEDIANTE IMAGENES INFRARROJAS"

