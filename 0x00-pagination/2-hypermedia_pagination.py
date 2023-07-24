#!/usr/bin/env python3
"""A python script"""
import math
import csv
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieving the page size"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
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
        """
        Ckeck for instance and return the data
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        my_page, my_Page_size = index_range(page, page_size)
        dataset = self.dataset()
        if my_page > len(dataset):
            return []
        return dataset[my_page:my_Page_size]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Getting some info from the file"""
        start, end = index_range(page, page_size)
        my_data = self.get_page(page, page_size)
        len_page_size = len(my_data)
        page = page
        data = my_data
        next_page = page + 1 if end < len(self.__dataset) else None
        prev_page = page - 1 if start > 0 else None
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_list = {
            'page_size': len_page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        return page_list
