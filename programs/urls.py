from django.conf.urls import patterns, url

from programs import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='programs_home'),
    url(r'^song/$', views.songList, name='programs_song_list'),
    url(r'^artist/$', views.artistList, name='programs_artist_list'),
    url(r'^song/(?P<pk>\d+)$', views.song, name='programs_song'),
    url(r'^artist/(?P<pk>\d+)$', views.artist, name='programs_artist'),
)
