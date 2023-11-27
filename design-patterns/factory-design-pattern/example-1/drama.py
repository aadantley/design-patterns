"""
Concrete Book class: Dra,a
"""
from book_interface import IBook


class DramaBook(IBook):
    def __init__(self):
        self._genre = "drama"
        self._title = "My Sister's Keeper"
        self._page_count = 423
        self._author = "Jodi Picoult"

    def page_count(self):
        return self._page_count

    def title(self):
        return self._title

    def author(self):
        return self._author

    def genre(self):
        return self._genre