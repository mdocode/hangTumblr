from django.conf.urls.defaults import *
from game.views import hello, game, start,found, grabRandomPostAsJson
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', start),
                       (r'^search/$', found),
                       (r'^hello/$', hello),
                       (r'^game/([a-z\-]+)/$', game),
                       (r'^game/([a-z\-]+)/next/$', grabRandomPostAsJson),
#                       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
 #                       {'document_root': '/home/mdobbs/Tumblr/hangtumblr/media/'}),
    # Example:
    # (r'^hangtumblr/', include('hangtumblr.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
