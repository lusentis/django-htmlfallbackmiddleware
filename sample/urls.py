from django.conf.urls.defaults import patterns, include, url

from django.views.generic.simple import redirect_to

urlpatterns = patterns('',
    # Examples:
    url(r'^$', redirect_to, {'url': '/index.html'}), 
)
