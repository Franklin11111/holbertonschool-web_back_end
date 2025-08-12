#!/usr/bin/python3
""" LFUCache module that inherits from BaseCache class
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Inherits from BaseCaching:
              - it is an LFU caching system
              - discard the least frequently used item
              - references the data are stored (in a
                dictionary of a parent class)
    """

    def __init__(self):
        """ Initialize the class
         """
        super().__init__()
        self.cache_data_obj = {}
        self.cache_data_obj_sorted = {}

    def put(self, key, item):
        """ Add an item in the cache. If key or item is None,
            this method should not do anything
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data_obj_sorted))
            self.cache_data_obj[first_key] -= 1
            self.cache_data_obj_sorted = dict(sorted(self.cache_data_obj.items(), key=lambda _item: _item[1]))
            if self.cache_data_obj[first_key] == 0:
                self.cache_data_obj_sorted.pop(first_key)
                self.cache_data_obj.pop(first_key)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}\n")

        if key in self.cache_data_obj:
            self.cache_data_obj[key] += 1
            self.cache_data_obj_sorted = dict(sorted(self.cache_data_obj.items(), key=lambda _item: _item[1]))
        else:
            self.cache_data_obj[key] = 1
            self.cache_data_obj_sorted[key] = 1
            self.cache_data_obj_sorted = dict(sorted(self.cache_data_obj.items(), key=lambda _item: _item[1]))

    def get(self, key):
        """ Get an item by key. If key is None or if the key doesn’t
            exist in self.cache_data, return None
        """
        if key in self.cache_data:
            if key in self.cache_data_obj:
                self.cache_data_obj[key] += 1
                self.cache_data_obj_sorted = dict(sorted(self.cache_data_obj.items(), key=lambda _item: _item[1]))
            return self.cache_data[key]
        else:
            return None


my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
my_cache.put("L", "L")
my_cache.print_cache()
my_cache.put("M", "M")
my_cache.print_cache()