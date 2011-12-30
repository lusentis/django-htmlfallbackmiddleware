# Django HTML Fallback Middleware

For each HTTP request, if no url can handle it, searches for a suitable template (based on request uri) and renders it (similar to flatpage.middleware.FlatpageFallbackMiddleware). 

## Install

Manual install

	git clone https://github.com/lusentis/django-htmlfallbackmiddleware
	python setup.py install

easy_install

	easdy_install django-htmlfallbackmiddleware

## Setup

Put `htmlfallbackmiddleware.middleware.HTMLFallbackMiddleware` at the end of your `settings.MIDDLEWARE_CLASSES` list

    MIDDLEWARE_CLASSES = (
      ...
      'htmlfallbackmiddleware.middleware.HTMLFallbackMiddleware',
    ) 


## Template name resolution

If no `urlpattern` matches the current request url (e.g. `/myapp/list`), then:

1. if the template `myapp/list.html` exists then render it and stop
2. if the template `list.html` exists then render it and stop
3. else raise Http404

