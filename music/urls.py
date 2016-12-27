from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),                                     #/models/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),              #/models/1/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),   #/models/2/favorite
]