from django.db import models
from model_utils import FieldTracker
from .model_caches import AlbumCache


class Artist(models.Model):
    name = models.CharField(max_length=250)


class Album(models.Model):
    title = models.CharField(max_length=250)
    artist = models.ForeignKey(Artist, related_name='albums')

    # need to add this in order to get cache to work
    tracker = FieldTracker()

post_save.connect(AlbumCache.model_post_save_signal, sender=AlbumCache.model)

class Song(models.Model):
    album = models.ForeignKey(Album, related_name='songs')
    title = models.CharField(max_length=250)
