from django.conf.urls import patterns, url
from .views import UserProfileLista
 
urlpatterns = patterns('',

url(r'^$', UserProfileLista.as_view(), name='userprofile'),

)
