"""
Book Factory Implementation
"""

from book_factory import BookFactory 


if __name__ == "__main__":
    book_genre = input("please describe your book genre: ")
    BOOK = BookFactory().genre(book_genre)
    if BOOK:
        print(BOOK.author(), BOOK.title(), BOOK.genre(), BOOK.page_count())
    else:
        print("error: book genre not implemented in factory. please update")