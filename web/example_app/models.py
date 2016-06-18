from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=250)


class Album(models.Model):
    title = models.CharField(max_length=250)
    artist = models.ForeignKey(Artist, related_name='albums')


class Song(models.Model):
    album = models.ForeignKey(Album, related_name='songs')
    title = models.CharField(max_length=250)
