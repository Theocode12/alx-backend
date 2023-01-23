#!/usr/bin/env python3
"""implementation of a basic cache with dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Base class for basic caching"""
    def put(self, key, item):
        """Put a key/value pair"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get a key/value pair"""
        return self.cache_data.get(key)
