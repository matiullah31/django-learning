from django.urls import path
from . import views

#namespace 
app_name = 'music'

urlpatterns = [
	# ex: /music/
    path('', views.IndexView.as_view(), name='index'),
   	# ex: /music/5/
   	# NOTE: `name` in the url refer to the path e.g '/music/5/'
   	# When ever we use DetailView it expect primary key 'pk'
    #path('<int:album_id>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    # ex: /music/album/5/
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),

    # ex: /music/album/5/delete/
    path('album/<int:pk>/delete', views.AlbumDelete.as_view(), name='album-delete'),

]
