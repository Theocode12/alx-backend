#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple, Mapping


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """gets page"""
        assert type(page) is int and type(page_size)\
            is int and page > 0 and page_size > 0
        start, stop = self.index_range(page, page_size)
        data = self.__dataset
        if start > len(data) - 2 or stop > len(data) - 1:
            return []
        return self.dataset()[start:stop]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """return the starts and end index of a page"""
        stop = page * page_size
        start = stop - page_size
        return (start, stop)

    def get_hyper(self, page: int, page_size: int) -> Mapping:
        """returns a dictionary"""
        prev_page = page - 1 if page > 1 else None
        total_pages = math.floor(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        page_dict = {'page_size': page_size, 'page': page,
                     'data': self.get_page(page, page_size),
                     'next_page': next_page,
                     'prev_page': prev_page,
                     'total_pages': total_pages
                     }
        return page_dict
