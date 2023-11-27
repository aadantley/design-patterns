"""
Chair Factory class
"""

from scifi import ScifiBook
from drama import DramaBook
from comedy import ComedyBook


class BookFactory:
    @staticmethod
    def genre(book):
        if book == "scifi":
            return ScifiBook()
        if book == "drama":
            return DramaBook()
        if book == "comedy":
            return ComedyBook()
        else:
            return None