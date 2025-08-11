#!/usr/bin/python3
""" LIFOCache module that inherits from BaseCache class
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Inherits from BaseCaching:
              - it is a LIFO caching system
              - references the data are stored (in a
                dictionary of a parent class)
    """

    def __init__(self):
        """ Initiliaze the class
         """
        super().__init__()
        self.last_added_key = ''

    def put(self, key, item):
        """ Add an item in the cache. If key or item is None,
            this method should not do anything
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keys = list(self.cache_data.keys())
            key_to_remove = keys[len(keys) - 2]
            if self.last_added_key:
                del self.cache_data[self.last_added_key]
                print(f"DISCARD: {self.last_added_key}")
            else:
                del self.cache_data[key_to_remove]
                print(f"DISCARD: {key_to_remove}")
            self.cache_data[key] = item
        self.last_added_key = key

    def get(self, key):
        """ Get an item by key. If key is None or if the key doesn’t
            exist in self.cache_data, return None
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
