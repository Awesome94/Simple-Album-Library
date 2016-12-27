from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Album(models.Model):
	artist = models.CharField(max_length=30)
	album_title = models.CharField(max_length=30)
	genre = models.CharField(max_length=15)
	#album_logo = models.CharField(max_length=50)        #A link to the logo online for now will suffice

	def __str__(self):
		return self.album_title + ' - ' + self.artist

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	song_title = models.CharField(max_length=30)
	file_type = models.CharField(max_length=10)
	is_favorite = models.BooleanField(default=False)

	def __str__(self):
		return self.song_title