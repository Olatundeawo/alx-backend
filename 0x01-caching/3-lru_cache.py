#!/usr/bin/env python3
"""
LIFO Caching module
"""
from collections import OrderedDict
BasicCaching = __import__('base_caching').BaseCaching


class LRUCache(BasicCaching):
    """LIFOCache"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assigning a key to an item
        """
        if key is None and item is None:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
        elif len(self.cache_data) >= BasicCaching.MAX_ITEMS:
            remove_key = self.cache_data.popitem(last=False)
            print('DISCARD: ', remove_key[0])
        self.cache_data[key] = item
        self.cache_data[key] = item

    def get(self, key) -> str:
        """Getting the value of a key
        """
        if key is None:
            return None
        if self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
