"""
Book Interface 
"""

from abc import ABCMeta, abstractmethod


class IBook(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def page_count():
        """abstract method to retrieve page count"""

    @staticmethod
    @abstractmethod
    def title():
        """abstract method to retrieve the book title"""

    @staticmethod
    @abstractmethod
    def author():
        """abstract method to retrieve the author of a book"""

    @staticmethod
    @abstractmethod
    def genre():
        """abstract method to retrieve the genre of a book"""
