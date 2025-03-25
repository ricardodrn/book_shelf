from typing import Any, Dict, List, Optional
from books.models.book import Book
from books.repositories.book_repository import BookRepository


class BoookService:
    def __init__(self, repository: BookRepository = None):
        self.repository = repository or BookRepository()

    def get_all_books(self) -> List[Book]:
        return self.repository.get_all()
    
    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        return self.repository.get_by_id(book_id)
    
    def create_book(self, book_data: Dict[str, Any]) -> Book:
        return self.repository.create(**book_data)
    
    def update_book(self, book_id: int, book_data: Dict[str, Any]) -> Optional[Book]:
        book = self.get_book_by_id(book_id)
        if not book:
            return None
        return self.repository.update(book, **book_data)
    
    def delete_book(self, book_id: int) -> None:
        book = self.get_book_by_id(book_id)
        if not book:
            return None
        return self.repository.delete(book)
    
    def get_books_by_status(self, status: str) -> List[Book]:
        return self.repository.filter_by(status=status)
    
    def get_books_by_genre(self, genre: str) -> List[Book]:
        return self.repository.filter_by(genre=genre)