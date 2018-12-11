from django.db import models
from django.urls import reverse

# Create your models here.
# Django will create table with Album name
# Django will also create a primary key automatically 
class Album(models.Model):
	# each of these variable is column name in table
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=500)
	genre = models.CharField(max_length=100)
	album_logo = models.FileField()

	# Where to redirect after insertion
	def get_absolute_url(self):
		return reverse('music:detail',kwargs={'pk':self.pk})

	# To Display Some whenever the album object is printed 
	def __str__(self):
		return self.album_title + '-' + self.artist

class Song(models.Model):
	# set the album primary key as a foreignkey for song
	# CASCADE means if album is deleted, also deletd the 
	# song associated with that album
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	file_type = models.CharField(max_length=10)
	song_title = models.CharField(max_length=250)
	is_favorite = models.BooleanField(default=False)

	# To Display Some whenever the song object is printed 
	def __str__(self):
		return self.song_title