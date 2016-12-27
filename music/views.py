from django.shortcuts import render, get_object_or_404
from .models import Album

# Create your views here.
def index(request):
	album_list = Album.objects.all()
	context = {
	    'album_list': album_list
	}
	return render(request, 'music/index.html', context)

def detail(request, album_id):
	album = get_object_or_404(Album, pk=album_id)

	return render(request, 'music/detail.html', { 'album': album })

def favorite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except (KeyError, Album.DoesNotExist):
		return render(request, 'music/detail.html', {
			'album': album,
			'error_message': 'Song does not exist',
			})
	else:
		selected_song.is_favorite = True
		selected_song.save()
		return render(request, 'music/detail.html', { 'album': album })