#!/usr/bin/python3
""" BasicCache module that inherits from BaseCache class
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Inherits from BaseCaching:
          - it is a caching system
          - references the data are stored (in a dictionary of a parent class)
    """

    def __init__(self):
        """ Initiliaze the class
        """
        super().__init__()
        """ Inherits properties from parent class
        """

    def put(self, key, item):
        """ Add an item in the cache. If key or item is None,
            this method should not do anything
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key. If key is None or if the key doesn’t
            exist in self.cache_data, return None
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
