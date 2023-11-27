"""
Chair Factory class
"""

from scifi import SciFiBook
from drama import DramaBook
from comedy import ComedyBook


class BookFactory:
    @staticmethod
    def page_count(book):
        if book == "scifi":
            return SciFiBook()
        if book == "drama":
            return DramaBook()
        if book == "comedy":
            return ComedyBook()
        else:
            return "invalid genre, please update Book Factory."