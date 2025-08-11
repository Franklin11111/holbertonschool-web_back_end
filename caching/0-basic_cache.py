#!/usr/bin/python3
""" BasicCache module that inherits from BaseCache class
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")


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
