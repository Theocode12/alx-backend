#!/usr/bin/env python3
"""Implentation of cache with LFU"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Cache replacement for MRU"""
    def __init__(self):
        self.lfu = []
        self.freq = []
        super().__init__()

    def put(self, key, item):
        """Input data into the cache"""
        if self.cache_data.get(key) and item:
            index = self.lfu.index(key)
            self.lfu.append(self.lfu.pop(index))
            self.freq.append(self.freq.pop(index) + 1)
        elif (len(self.lfu) < self.MAX_ITEMS) and key and item:
            self.lfu.append(key)
            self.freq.append(1)
        elif key and item:
            index = self.freq.index(min(self.freq))
            print("DISCARD: {}".format(self.lfu[index]))
            del self.cache_data[self.lfu.pop(index)]
            self.lfu.append(key)
            self.freq.pop(index)
            self.freq.append(1)
        else:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Gets value for key if exist"""
        if self.cache_data.get(key):
            index = self.lfu.index(key)
            self.lfu.append(self.lfu.pop(index))
            self.freq.append(self.freq.pop(index) + 1)
        return self.cache_data.get(key)
