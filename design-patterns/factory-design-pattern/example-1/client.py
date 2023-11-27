"""
Book Factory Implementation
"""

from book_factory import BookFactory 

book_genre = input("please describe your book genre: ")
BOOK = BookFactory().get_book(book_genre)
print(BOOK.page_count())