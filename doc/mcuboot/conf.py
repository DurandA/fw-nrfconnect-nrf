#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# mcuboot documentation build configuration file, created by
# sphinx-quickstart on Mon Jun 11 11:28:40 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sys
import os
import pkg_resources
from packaging import version

if "NRF_BASE" not in os.environ:
    sys.exit("$NRF_BASE environment variable undefined.")
NRF_BASE = os.path.abspath(os.environ["NRF_BASE"])

if "ZEPHYR_OUTPUT" not in os.environ:
    sys.exit("$ZEPHYR_OUTPUT environment variable undefined.")
ZEPHYR_OUTPUT = os.path.abspath(os.environ["ZEPHYR_OUTPUT"])

if "NRF_OUTPUT" not in os.environ:
    sys.exit("$NRF_OUTPUT environment variable undefined.")
NRF_OUTPUT = os.path.abspath(os.environ["NRF_OUTPUT"])

if "NRF_RST_SRC" not in os.environ:
    sys.exit("$NRF_RST_SRC environment variable undefined.")
NRF_RST_SRC = os.path.abspath(os.environ["NRF_RST_SRC"])

if "MCUBOOT_OUTPUT" not in os.environ:
    sys.exit("$MCUBOOT_OUTPUT environment variable undefined.")
MCUBOOT_OUTPUT = os.path.abspath(os.environ["MCUBOOT_OUTPUT"])

if "MCUBOOT_RST_SRC" not in os.environ:
    sys.exit("$MCUBOOT_RST_SRC environment variable undefined.")
MCUBOOT_RST_SRC = os.path.abspath(os.environ["MCUBOOT_RST_SRC"])

if "KCONFIG_OUTPUT" not in os.environ:
    sys.exit("$KCONFIG_OUTPUT environment variable undefined.")
KCONFIG_OUTPUT = os.path.abspath(os.environ["KCONFIG_OUTPUT"])

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# recommonmark didn't have a setup function before 0.5.0, so source_parsers
# must be added manually
recommonmark_version = pkg_resources.get_distribution("recommonmark").version
if version.parse(recommonmark_version) < version.parse('0.5.0'):
    extensions = ['sphinx.ext.intersphinx',
                  'breathe',
                  'sphinx.ext.ifconfig']
else:
    extensions = ['sphinx.ext.intersphinx',
                  'breathe',
                  'sphinx.ext.ifconfig',
                  'recommonmark']

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['../_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

if version.parse(recommonmark_version) < version.parse('0.5.0'):
    source_parsers = {
       '.md': 'recommonmark.parser.CommonMarkParser',
    }

# The master toctree document.
master_doc = 'wrapper'

# General information about the project.
project = 'MCUboot'
copyright = '2019-2020'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.6.99'
# The full version, including alpha/beta/rc tags.
release = '1.6.99'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'mcuboot'
html_theme_path = ['{}/doc/themes'.format(NRF_BASE)]
html_favicon = '{}/doc/static/images/favicon.ico'.format(NRF_BASE)

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['{}/doc/static'.format(NRF_BASE)]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = True

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink =

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, license is shown in the HTML footer. Default is True.
html_show_license = True

intersphinx_mapping = {
    # Link the Kconfig docs with Intersphinx so that references to Kconfig
    # symbols (via :option:`CONFIG_FOO`) turn into links
    'kconfig': (os.path.relpath(KCONFIG_OUTPUT, MCUBOOT_OUTPUT),
                os.path.join(os.path.relpath(KCONFIG_OUTPUT, MCUBOOT_RST_SRC),
                             'objects.inv')),
    'zephyr': (os.path.relpath(ZEPHYR_OUTPUT, NRF_OUTPUT),
               os.path.join(os.path.relpath(ZEPHYR_OUTPUT, NRF_RST_SRC),
                            'objects.inv'))
}

def setup(app):
    app.add_stylesheet("css/common.css")
    app.add_stylesheet("css/mcuboot.css")
    app.add_js_file("js/ncs.js")
