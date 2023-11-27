"""
Concrete Book class: Scifi
"""
from book_interface import IBook


class ScifiBook(IBook):
    def __init__(self):
        self._genre = "scifi"
        self._title = "A Scanner Darkly"
        self._page_count = 220
        self._author = "Phillip K. Dick"

    def page_count(self):
        return self._page_count

    def title(self):
        return self._title

    def author(self):
        return self._author

    def genre(self):
        return self._genre
