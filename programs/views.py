# programs/views.py
from django.shortcuts import render, get_object_or_404#, redirect_render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . import models

def home(request):
    context = {
        'artist_count': models.Artist.objects.count(),
        'song_count': models.Song.objects.count(),
    }
    return render(request, 'programs/home.html', context)

def song_detail(request, pk):
    song = get_object_or_404(models.Song, id=pk)
    return render(request, 'programs/song_detail.html', {'song': song})

def artist_detail(request, pk):
    artist = get_object_or_404(models.Artist, id=pk)
    return render(request, 'programs/artist_detail.html', {'artist': artist})
    
def song_listing(request):
    songs = models.Song.objects.all()
    return render(request, 'programs/song_listing.html', {'songs': songs})

def artist_listing(request):
    artists = models.Artist.objects.all()
    return render(request, 'programs/artist_listing.html', {'artists': artists})