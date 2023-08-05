#!/usr/bin/env python3
"""
Basic caching module
"""
BasicCaching = __import__('BaseCaching').BaseCaching


class BasicCache(BasicCaching):
    "BasicCache class"
    def __init__(self):
        """initilizating the
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """assigning a key to an item
        """
        if key or item:
            self.cache_data[key] = item

    def get(self, key) -> str:
        """Getting the value of a key
        """
        if key is None:
            return None
        if self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
