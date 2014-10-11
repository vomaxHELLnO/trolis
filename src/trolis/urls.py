from django.conf.urls import patterns, url
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import *

urlpatterns = patterns('',
    url(r'^$', trolis_view, name='index'),
    url(r'^vomax/$', vomax_view, name='vomax'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^checkers/$', checkers_view, name='checkers'),
    url(r'^play_checkers/$', play_checkers_view, name='checkers'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)
