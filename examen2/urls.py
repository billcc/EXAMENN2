#encoding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.userprofile.views import UserProfileList,UserProfileCreate 

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'examen2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', UserProfileList.as_view(), name='userprofile'),
    url(r'^registro/', UserProfileCreate.as_view(), name='registro'),
  

)

