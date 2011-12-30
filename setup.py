#!/usr/bin/env python

from distutils.core import setup

setup(name='django-htmlfallbackmiddleware',
      version='0.1',
      description='For each HTTP request, if no url can handle it, searches for a suitable template (based on request uri) and renders it (similar to flatpage.middleware.FlatpageFallbackMiddleware).',
      author='Simone Lusenti',
      author_email='simone@slusenti.me',
      url='https://github.com/lusentis/django-htmlfallbackmiddleware',
      packages=['htmlfallbackmiddleware'],
)
