"""
1. make it so that on postsave, serialized version of model is cached to its id
2. cache list of all ids you want (define queryset)
3.

"""


class BaseCache(object):
    pass


class ModelCache(BaseCache):
    pass

