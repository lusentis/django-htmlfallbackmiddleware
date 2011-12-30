# Django HTML Fallback Middleware

For each HTTP request, if no url can handle it, searches for a suitable template (based on request uri) and renders it (similar to flatpage.middleware.FlatpageFallbackMiddleware). 

## Install

Manual install

	git clone https://github.com/lusentis/django-stylus/
	python setup.py install

Pypi

	pypi install 'https://github.com/lusentis/django-htmlfallbackmiddleware/zipball/master'

## Setup

Add `htmlfallbackmiddleware.middleware.HTMLFallbackMiddleware` to your `settings.MIDDLEWARE_CLASSES`

    MIDDLEWARE_CLASSES = (
      ...
      'htmlfallbackmiddleware.middleware.HTMLFallbackMiddleware',
      ...      
    ) 


## Template name resolution

If no `urlpattern` matches the current request url (e.g. /myapp/list), then:

1. If the template /myapp/list.html exists then render it and stop
2. If the template /list.html exists then render it and stop
3. Else raise Http404

