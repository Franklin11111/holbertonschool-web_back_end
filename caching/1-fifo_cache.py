#!/usr/bin/python3
""" FIFOCache module that inherits from BaseCache class
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Inherits from BaseCaching:
              - it is a FIFO caching system
              - references the data are stored (in a
                dictionary of a parent class)
    """

    def __init__(self):
        """ Initiliaze the class
         """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache. If key or item is None,
            this method should not do anything
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key_deleted = next(iter(self.cache_data.keys()))
            self.cache_data.pop(key_deleted)
            print(f"DISCARD: {key_deleted}")
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key. If key is None or if the key doesn’t
            exist in self.cache_data, return None
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
