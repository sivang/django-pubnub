from django.conf.urls.defaults import patterns, include, url
from tastypie.api import api
from api import *

from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v'1)

v1_api.register(LoginResource())
v1_api.register(CurrentAccountResource())

urlpatterns = patterns('',
    url(r'^$', include('currentaccount.urls')),
    url(r'^current_account/', include('currentaccount.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)

