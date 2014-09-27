from pygments.lexers.web import PhpLexer
from sphinx.highlighting import lexers

project = u'Vermillion'
copyright = u'2014 Kilte Leichnam'

master_doc = 'index'
highlight_language = 'php'

version = '1'
release = '1.0.0'

lexers['php'] = PhpLexer(startinline=True)
