#from django.http import Http404
#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request):
 
    # all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')
    # context = {
    # 	'all_albums':all_albums
    # }
    # return HttpResponse(template.render(context,request))

    all_albums = Album.objects.all()
    context = {'all_albums':all_albums}
    return render(request, 'music/index.html',context)


def detail(request, album_id):
	# try:
	# 	album = Album.objects.get(pk=album_id)
	# 	return render(request, 'music/detail.html',{'album':album})
	# except Exception as e:
	# 	raise http404("Album does not exist")
    # Instead of try except block we can use the shortcuts
    album = get_object_or_404(Album,pk=album_id)
    return render(request, 'music/detail.html',{'album':album})

def favorite(request, album_id):
    album = get_object_or_404(Album,pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, song.DoesNotExist):
          return render(request, 'music/detail.html',{
            'album':album,
            'error_message':"You did not select a valid song",
            })
    else:
        if selected_song.is_favorite != True:
            selected_song.is_favorite = True
        else:
            selected_song.is_favorite = False

        selected_song.save()
        return render(request, 'music/detail.html',{'album':album})
