from .models import Album
from ..model_cache_store import BaseCache

from example_app.serializers import AlbumSerializer


class AlbumCache(BaseCache):
    model_serializer = AlbumSerializer
    model = Album
    queryset = Album.objects.all()
    version = '1.0'

post_save.connect(AlbumCache.model_post_save_signal, sender=AlbumCache.model)
