# programs/views.py
from django.shortcuts import render, get_object_or_404#, redirect_render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from programs.models import Song, Artist

def home(request):
    context = {
        'artist_count': Artist.objects.count(),
        'song_count': Song.objects.count(),
    }
    return render(request, 'programs/home.html', context)

def song(request, pk):
    song = get_object_or_404(Song, id=pk)
    return render(request, 'programs/song.html', {'song': song})

def artist(request, pk):
    artist = get_object_or_404(Artist, id=pk)
    return render(request, 'programs/artist.html', {'artist': artist})
    
def songList(request):
    song_list = Song.objects.all()
    return render(request, 'programs/song_list.html', {'songs': song_list})

def artistList(request):
    artist_list = Artist.objects.all()
    return render(request, 'programs/artist_list.html', {'artists': artist_list})