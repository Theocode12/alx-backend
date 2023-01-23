#!/usr/bin/env python3
"""Implentation of cache with FIFO"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Cache replacement for FIFO"""
    def __init__(self):
        self.fifo = []
        super().__init__()

    def put(self, key, item):
        """Input data into the cache"""
        if self.cache_data.get(key):
            self.fifo.remove(key)
            self.fifo.append(key)
        elif (len(self.fifo) < self.MAX_ITEMS) and key:
            self.fifo.append(key)
        elif key:
            r_key = self.fifo.pop(0)
            print("DISCARD: {}".format(r_key))
            del self.cache_data[r_key]
            self.fifo.append(key)
        else:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Gets value for key if exist"""
        return self.cache_data.get(key)
