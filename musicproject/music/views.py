

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Album

def album_list(request):
    query = request.GET.get('q', '')
    genre = request.GET.get('genre', '')
    artist = request.GET.get('artist', '')

    albums = Album.objects.all()

    if query:
        albums = albums.filter(title__icontains=query)
    if genre:
        albums = albums.filter(genre__icontains=genre)
    if artist:
        albums = albums.filter(artist__icontains=artist)

    context = {
        'albums': albums,
        'query': query,
        'genre': genre,
        'artist': artist,
    }
    return render(request, 'music/album_list.html', context)



def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    context = {
        'album': album,
    }
    return render(request, 'music/album_detail.html', context)

