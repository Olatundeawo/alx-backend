#!/usr/bin/env python3
"""
LIFO Caching module
"""
from collections import OrderedDict, defaultdict
BasicCaching = __import__('BaseCaching').BaseCaching


class LFUCache(BasicCaching):
    """LIFOCache"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = defaultdict(int)

    def put(self, key, item):
        """assigning a key to an item
        """
        if key is None and item is None:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
        elif len(self.cache_data) >= BasicCaching.MAX_ITEMS:
            remove_key = min(self.frequency, key=self.frequency.get)
            self.cache_data.pop(remove_key)
            del self.frequency[remove_key]
            print('DISCARD: ', remove_key[0])
        self.cache_data[key] = item
        self.frequency[key] += 1

    def get(self, key) -> str:
        """Getting the value of a key
        """
        if key in self.cache_data:
            value = self.cache_data.get(key)
            self.frequency[key] += 1
            self.cache_data[key] = value
            return value
        else:
            return None
