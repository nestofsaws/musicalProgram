from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^songs/$', views.song_listing, name='song_listing'),
    url(r'^artists/$', views.artist_listing, name='artist_listing'),
    url(r'^programs/$', views.program_listing, name='program_listing'),
    url(r'^songs/(?P<pk>\d+)$', views.song_detail, name='song_detail'),
    url(r'^artists/(?P<pk>\d+)$', views.artist_detail, name='artist_detail'),
    url(r'^programs/(?P<pk>\d+)$', views.program_detail, name='program_detail'),
)
