#!/usr/bin/env python3
"""Implentation of cache with MRU"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Cache replacement for MRU"""
    def __init__(self):
        self.mru = []
        super().__init__()

    def put(self, key, item):
        """Input data into the cache"""
        if self.cache_data.get(key) and item:
            self.mru.remove(key)
            self.mru.append(key)
        elif (len(self.mru) < self.MAX_ITEMS) and key and item:
            self.mru.append(key)
        elif key and item:
            r_key = self.mru.pop(-1)
            print("DISCARD: {}".format(r_key))
            del self.cache_data[r_key]
            self.mru.append(key)
        else:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Gets value for key if exist"""
        if self.cache_data.get(key):
            self.mru.remove(key)
            self.mru.append(key)
        return self.cache_data.get(key)
