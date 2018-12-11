from django.urls import path
from . import views

#namespace 
app_name = 'music'

urlpatterns = [
	# ex: /music/
    path('', views.index, name='index'),
   	# ex: /music/5/
   	# NOTE: `name` in the url refer to the path e.g '/music/5/'
    path('<int:album_id>/', views.detail, name='detail'),
    # ex: /music/3/favorite
    #path('favorite/<int:album_id>/', views.favorite, name='favorite'), or 
    path('<int:album_id>/favorite', views.favorite, name='favorite'),
]
