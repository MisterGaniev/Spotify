from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=30)
    direction = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True)


class Album(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateField()
    cover = models.URLField(blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
    title = models.CharField(max_length=30)
    cover = models.URLField(blank=True)
    lyrics = models.TextField(blank=True)
    duration = models.DurationField()
    source = models.URLField(blank=True)
    eshitildi = models.PositiveIntegerField(default=0)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_songs')
