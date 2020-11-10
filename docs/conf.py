import sphinx_rtd_theme
import os
import sys
import os.path
import subprocess
import shutil
import sphinx_rtd_theme
from recommonmark.transform import AutoStructify
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

master_doc="index"

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'drkrm'
copyright = '2020, Ursula Ott'
author = 'Ursula Ott'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['recommonmark', 'autoapi.extension']
autoapi_dirs = ['../src']

source_suffix = ['.rst', '.md']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.


html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


from recommonmark.transform import AutoStructify

def setup(app):
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
    }, True)
    app.add_transform(AutoStructify)

# for auto api documentation


# -- Other -------------------------------------------------
# with reference to https://github.com/timkpaine/tributary/blob/main/docs/conf.py

texinfo_documents = [
    (master_doc, 'drkrm') ,
]


def run_copyreadme(_):
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), 'index.md'))
    readme = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'README.md'))
    api = os.path.abspath(os.path.join(os.path.dirname(__file__), 'api.md'))
    with open(out, 'w') as fp1:
        with open(readme, 'r') as fp2:
            # Skip img
            fp2.readline()
            fp1.write("# drkrm\n")
            for line in fp2:
                if 'src=' in line:
                    # <img>
                    fp1.write(line.replace("docs/", ""))
                elif "](docs/" in line:
                    # md
                    fp1.write(line.replace("](docs/", "]("))
                else:
                    fp1.write(line)

        with open(api, 'r') as fp2:
            fp1.write(fp2.read())


def run_apidoc(_):
    out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'api'))
    lib_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
    cmd_path = 'sphinx-apidoc'
    if hasattr(sys, 'real_prefix'):  # Check to see if we are in a virtualenv
        # If we are, assemble the path manually
        cmd_path = os.path.abspath(os.path.join(sys.prefix, 'bin', 'sphinx-apidoc'))
    subprocess.check_call([cmd_path,
                           '-E',
                           '-M',
                           '-o',
                           out_dir,
                           lib_dir,
                           '--force'])


def setup(app):
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
    }, True)
    app.add_transform(AutoStructify)
    app.connect('builder-inited', run_copyreadme)
    app.connect('builder-inited', run_apidoc)
