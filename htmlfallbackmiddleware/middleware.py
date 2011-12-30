"""

HTMLFallbackMiddleware
======================

For each HTTP request, if no url can handle it, searches for a
suitable template (based on request uri) and renders it (similar
to flatpage.middleware.FlatpageFallbackMiddleware).

"""

from django.http import Http404
from django.shortcuts import render_to_response
from django.template import TemplateDoesNotExist
from django.conf import settings 

class HTMLFallbackMiddleware(object):
    def process_response(self, request, response):
        if response.status_code != 404:
            return response
        else:
            path = request.path_info.lstrip('/') # remove leading /

            try:
                try:
                    # search for 'myapp/list.html'
                    if path.endswith('.html'):
                        return render_to_response(path)
                    else:
                        return render_to_response(''.join([path, '.html']))
                except:
                    # search for 'list.html'
                    (_, _, path_ending) = path.rpartition('/')
                    if path_ending.endswith('.html'):
                        return render_to_response(path_ending)
                    else:
                        return render_to_response(''.join([path_ending, '.html']))

            except TemplateDoesNotExist:
                raise Http404('No HTML template matches the given path: `{0}` (See HTMLFallbackMiddleware README for more info: https://github.com/lusentis/django-htmlfallbackmiddleware/blob/master/README.markdown).'.format(path))

            except:
                if settings.DEBUG:
                    raise
                return response
