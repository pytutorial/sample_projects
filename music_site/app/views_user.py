from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def index(request):
    songs = Song.objects.all()
    
    keyword = request.GET.get('keyword', '')
    if keyword:
        songs = songs.filter(title__contains=keyword)

    return render(request, 'user/index.html', {'songs' : songs, 'keyword': keyword})

def viewSong(request, id):
    song = get_object_or_404(Song, pk=id)
    return render(request, 'user/song_detail.html', {'song' : song})

def myPlaylist(request):
    return render(request, 'user/my_playlist.html', {'page' : 1})    
