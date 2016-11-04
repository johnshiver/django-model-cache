from django.db.models.signals import post_save


class BaseCache(object):
    # check that model vars
    # and attributes were set correctly

    model_serializer = None
    model = None
    version = None
    queryset = None

    required_attrs = {
        'model_serializer',
        'model',
        'version',
    }

    def __init__(self, *args, **kwargs):
        """
        """

        # validate BaseCache
       # if not all(self.required_attrs):
       #     raise ValueError("Must define cache with {}".format(self.required_attrs))
       # if self.queryset is None:
       #     self.queryset = self.model.objects.all()


    def get(self):
        """
        """

    @staticmethod
    def model_post_save_signal(sender, instance, **kwargs):
        # look at sender and determine if any
        # of the model attributes we care about
        # were changed on newly saved model

        # if so: store in redis sorted
        import ipdb;ipdb.set_trace()


    def refresh(self):
        """
        """


    # method that will put model in cache
    def _store_in_cache(self, instance):
        """
        invoked when post_save signal determines
        cache needs to be invalidated
        """

        cache_key =self._gen_cache_key()
        serialized_model = self.model_serializer(instance)

        if not serialized_model.valid():
            print "There was an error serializing model"
            return

        conn = self._get_redis_connection()
        conn.zadd(cache_key, instanc.id, serialized_model.data)

    def _gen_cache_key(self):
        # important, used for key in redis
        return "mc:{}_{}_v{}".format(self.__name__,
                                     self.model.__name__,
                                     self.version)

    def _get_cache_fields(self):
        return self.model_serializer.Meta.fields

# after model is created connect signal
#post_save.connect(BaseCache.model_post_save_signal, BaseCache.model)


from example_app.models import Album
from example_app.serializers import AlbumSerializer


class AlbumCache(BaseCache):
    model_serializer = AlbumSerializer
    model = Album
    queryset = Album.objects.all()
    version = '1.0'

post_save.connect(AlbumCache.model_post_save_signal, sender=AlbumCache.model)
