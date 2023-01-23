#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """
        The goal here is that if between two queries,
        certain rows are removed from the dataset, the user
        does not miss items from dataset when changing page.
        """
        assert type(index) is int and type(page_size)\
            is int and index >= 0 and page_size > 0
        assert index <= list(self.__indexed_dataset.keys())[-1]
        i = index
        data = []
        while not self.__indexed_dataset.get(i):
            if i > list(
                    self.__indexed_dataset.keys()
                    )[-1]:
                break
            i += 1
        while True:
            if len(data) == page_size or i > list(
                                            self.__indexed_dataset.keys()
                                            )[-1]:
                break
            if self.__indexed_dataset.get(i):
                data.append(self.__indexed_dataset[i])
            i += 1

        data_page = {
            'index': index,
            'next_index': index + page_size,
            'page_size': page_size,
            'data': data
        }
        return data_page
