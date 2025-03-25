from typing import List, Optional
from books.models.book import Book

class BookRepository:

    @staticmethod
    def get_all() -> List[Book]:
        return Book.objects.all()
    
    @staticmethod
    def get_by_id(book_id: int) -> Optional[Book]:
        try:
            return Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return None
    
    @staticmethod
    def create(**kwargs) -> Book:
        return Book.objects.create(**kwargs)
    
    @staticmethod
    def update(book: Book, **kwargs) -> Book:
        for key, value in kwargs.items():
            setattr(book, key, value)
        book.save()
        return book
    
    @staticmethod
    def delete(book: Book) -> None:
        book.delete()

    @staticmethod
    def filter_by(**kwargs) -> List[Book]:
        return Book.objects.filter(**kwargs)
        