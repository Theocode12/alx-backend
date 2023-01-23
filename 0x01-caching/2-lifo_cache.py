#!/usr/bin/env python3
"""Implentation of cache with LIFO"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Cache replacement for LIFO"""
    def __init__(self):
        self.lifo = []
        super().__init__()

    def put(self, key, item):
        """Input data into the cache"""
        if self.cache_data.get(key) and item:
            self.lifo.remove(key)
            self.lifo.append(key)
        elif (len(self.lifo) < self.MAX_ITEMS) and key and item:
            self.lifo.append(key)
        elif key and item:
            r_key = self.lifo.pop(-1)
            print("DISCARD: {}".format(r_key))
            del self.cache_data[r_key]
            self.lifo.append(key)
        else:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Gets value for key if exist"""
        return self.cache_data.get(key)
