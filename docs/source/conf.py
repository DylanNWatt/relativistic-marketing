from sphinxawesome_theme import ThemeOptions
from dataclasses import asdict
from sphinxawesome_theme.postprocess import Icons

# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Relativistic'
copyright = '2024, Kadre LLC'
author = 'Dylan Watt'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

# intersphinx_mapping = {
#     'python': ('https://docs.python.org/3/', None),
#     'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
# }
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinxawesome_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'



# theme_options = ThemeOptions(
#    # Add your theme options. For example:
#    show_breadcrumbs=True,
#    main_nav_links={"About", "/about"},
# )

html_permalinks_icon = Icons.permalinks_icon
# html_theme_options = asdict(theme_options)