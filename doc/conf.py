# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html  wokeignore:rule=master

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Netplan'
copyright = '2022, Netplan team'
author = 'Netplan team'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx_design', 'myst_parser', 'sphinx_copybutton', 'sphinxcontrib.spelling', 'breathe']
myst_enable_extensions = ["colon_fence"]
smartquotes_action = 'qe'

# Doxygen
# https://breathe.readthedocs.io/en/latest/directives.html
# breathe_projects = {"Netplan": "../doxyxml/"}
breathe_projects_source = {"auto-apidoc": ("../", [
    "include/netplan.h",
    "include/parse-nm.h",
    "include/parse.h",
    "include/types.h",
    "include/util.h",
    "src/error.c",
    "src/names.c",
    "src/netplan.c",
    "src/parse-nm.c",
    "src/parse.c",
    "src/types.c",
    "src/util.c",
    "src/validation.c",
    ])}
# breathe_doxygen_config_options =
# breathe_doxygen_aliases =
breathe_default_project = "auto-apidoc"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'env']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The logo
html_logo = 'netplan.svg'

# -- Options for MyST --------------------------------------------------------
myst_title_to_header = True
suppress_warnings = ['myst.xref_missing']

# Spelling
spelling_lang = 'en_US'
tokenizer_lang = 'en_US'
spelling_show_suggestions = True
