from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^planet/', include('planet.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': 'media/favicon.ico'}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += patterns('',
    ('$', "planet.views.posts_list"),
)
