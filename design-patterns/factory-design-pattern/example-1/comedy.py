"""
Concrete Book class: Scifi
"""
from book_interface import IBook


class ComedyBook(IBook):
    def __init__(self):
        self._genre = "comedy"
        self._title = "Dial A For Aunties"
        self._page_count = 34
        self._author = "Jesse Q Sutanto"

    def page_count(self):
        return self._page_count

    def title(self):
        return self._title

    def author(self):
        return self._author

    def genre(self):
        return self._genre
