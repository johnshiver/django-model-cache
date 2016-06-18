from .models import Album

from ..model_cache_store import ModelCache


class AlbumCache(ModelCache):
    model = Album
    queryset = Album.objects.all()
    cache_key = 'albums_v1'
