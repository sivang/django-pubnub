from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('currentaccount.urls')),
    url(r'^current_account/', include('currentaccount.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
