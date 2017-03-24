from django.conf.urls import url
# Doctring
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/712/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #/music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    #/music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    #/music/album/2/delete/
    url(r'(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    #/music/album/2/rent/
    url(r'(?P<pk>[0-9]+)/rent/$', views.AlbumRent.as_view(), name='rent'),
    
    #/music/album/2/inventory/
    url(r'album/(?P<pk>[0-9]+)/inventory/$', views.AlbumInventory.as_view(), name='inventory'),
    
    #/music/album/2/confirm/
    url(r'album/(?P<pk>[0-9]+)/confirm/$', views.Confirm.as_view(), name='confirm')
]