# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import pathlib
# import sys
# path_ext = pathlib.Path("./source/_ext").resolve()
# sys.path.insert(0, str(path_ext))


# -- Project information -----------------------------------------------------

project = "Berk's Robotic Notes"
copyright = '2021, Berk Tosun'
author = 'Berk Tosun'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
    # "sphinx.ext.mathjax",
    "sphinx.ext.imgmath",
    "sphinx.ext.todo",
]
autosectionlabel_prefix_document = True
todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
# mathjax3_config = {
#     "tex": {
#         "packages": ["base", "ams", "physics"]
#     }
# }

latex_engine = 'lualatex'
imgmath_image_format = 'svg'
imgmath_font_size = 12
imgmath_latex_preamble = r"\usepackage{physics} \usepackage{mathptmx}" \
    r"\usepackage{amsmath} \usepackage{tensor}"

# \newcommand{\vertbar}{\rule[-1ex]{0.5pt}{2.5ex}}
# \newcommand{\horzbar}{\rule[.5ex]{2.5ex}{0.5pt}}

# def setup(app):
#     app.add_css_file(str(pathlib.Path("./source/_static/custom.css").resolve()))

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [] # type: ignore


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']