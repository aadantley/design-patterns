"""
Book Interface 
"""

from abc import ABCMeta, abstractmethod


class IBook(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def page_count():
        """abstract method to retrieve page count"""

    def title():
        """abstract method to retrieve the book title"""

    def author():
        """abstract method to retrieve the author of a book"""
