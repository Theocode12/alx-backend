#!/usr/bin/env python3
""" mod's doc string """
# import csv
# import math
# from typing import List, Tuple


# def index_range(page: int, page_size: int) -> Tuple[int, int]:
#     """return the starts and end index of a page"""
#     stop = page * page_size
#     start = stop - page_size
#     return (start, stop)


# class Server:
#     """Server class to paginate a database of popular baby names.
#     """
#     DATA_FILE = "Popular_Baby_Names.csv"

#     def __init__(self):
#         self.__dataset = None

#     def dataset(self) -> List[List]:
#         """Cached dataset
#         """
#         if self.__dataset is None:
#             with open(self.DATA_FILE) as f:
#                 reader = csv.reader(f)
#                 dataset = [row for row in reader]
#             self.__dataset = dataset[1:]

#         return self.__dataset

#     # def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
#     #     """gets page"""
#     #     assert (
#     #         isinstance(page, int) and isinstance(page_size, int)
#     #         and page > 0 and page_size > 0
#     #     )
#     #     # assert type(page) is int and type(page_size)\
#     #     #     is int and page > 0 and page_size > 0
#     #     start, stop = index_range(page, page_size)
#     #     data = self.dataset()
#     #     if start > len(data) - 2 or stop > len(data) - 1:
#     #         return []
#     #     return data[start:stop]

#     def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
#         """ get page returns paginated dataset based on page and page
#         size"""
#         assert (
#             isinstance(page, int) and isinstance(page_size, int)
#             and page > 0 and page_size > 0
#         )
#         start, end = index_range(page, page_size)
#         data = self.dataset()
#         # max_page = math.ceil(len(data) / page_size)
#         if start > len(data) - 2 or end > len(data) - 1:
#             return []
#         return data[start:end]




import csv
import math
from typing import List, Set, Dict, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ computes and returns the range of indexes
    to return in a list for which page and page_size
    was determined """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)


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
        """ get page returns paginated dataset based on page and page
        size"""
        assert (
            isinstance(page, int) and isinstance(page_size, int)
            and page > 0 and page_size > 0
        )
        start, end = index_range(page, page_size)
        data = self.dataset()
        # max_page = math.ceil(len(data) / page_size)
        if start > len(data) - 2 or end > len(data) - 1:
            return []
        return data[start:end]