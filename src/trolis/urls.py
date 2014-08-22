from django.conf.urls import patterns, url
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import *

urlpatterns = patterns('',
    url(r'^$', index_view, name='index'),
    url(r'^vomax/$', vomax_view, name='vomax'),
    url(r'^login/$', login_view, name='login'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)
