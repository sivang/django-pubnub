from django.conf.urls.defaults import patterns, url

from currentaccount import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<curaccount_id>\d+)/$', views.detail, name='detail'),
)
