#!/usr/bin/env python3
"""A module that computes the start
index and end index of a page"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return the starts and end index of a page"""
    stop = page * page_size
    start = stop - page_size
    return (start, stop)
