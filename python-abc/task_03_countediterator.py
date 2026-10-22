#!/usr/bin/python3
"""Module containing the CountedIterator class"""


class CountedIterator:
    """An iterator that counts the items fetched"""

    def __init__(self, data):
        self.iterator = iter(data)
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item

    def __iter__(self):
        return self
