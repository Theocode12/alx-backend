#!/usr/bin/env python3
"""Implentation of cache with LRU"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Cache replacement for LRU"""
    def __init__(self):
        self.lru = []
        super().__init__()

    def put(self, key, item):
        """Input data into the cache"""
        if self.cache_data.get(key) and item:
            self.lru.remove(key)
            self.lru.append(key)
        elif (len(self.lru) < self.MAX_ITEMS) and key and item:
            self.lru.append(key)
        elif key and item:
            r_key = self.lru.pop(0)
            print("DISCARD: {}".format(r_key))
            del self.cache_data[r_key]
            self.lru.append(key)
        else:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Gets value for key if exist"""
        if self.cache_data.get(key):
            self.lru.remove(key)
            self.lru.append(key)
        return self.cache_data.get(key)
