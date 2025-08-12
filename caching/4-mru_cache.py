#!/usr/bin/python3
""" MRUCache module that inherits from BaseCache class
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Inherits from BaseCaching:
              - it is an MRU caching system
              - discard the most recently used item
              - references the data that are stored (in a
                dictionary of a parent class)
    """

    def __init__(self):
        """ Initialize the class
         """
        super().__init__()
        self.cache_data_keys = []

    def put(self, key, item):
        """ Add an item in the cache. If key or item is None,
            this method should not do anything
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            if key in self.cache_data_keys:
                self.cache_data_keys.remove(key)
                self.cache_data_keys.append(key)
            else:
                self.cache_data_keys.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            removed_key = self.cache_data_keys.pop(-2)
            del self.cache_data[removed_key]
            print(f"DISCARD: {removed_key}")

    def get(self, key):
        """ Get an item by key. If key is None or if the key doesn’t
            exist in self.cache_data, return None
        """
        if key in self.cache_data:
            if key in self.cache_data_keys:
                self.cache_data_keys.remove(key)
                self.cache_data_keys.append(key)
            return self.cache_data[key]
        else:
            return None
