#!/usr/bin/env python3
"""
LIFO Caching module
"""

BasicCaching = __import__('BaseCaching').BaseCaching


class LIFOCache(BasicCaching):
    """LIFOCache"""
    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """assigning a key to an item
        """
        if key is None and item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BasicCaching.MAX_ITEMS:
                key1 = self.cache_data.popitem()
                print('DISCARD: ', key1[0])
        self.cache_data[key] = item

    def get(self, key) -> str:
        """Getting the value of a key
        """
        if key is None:
            return None
        if self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
