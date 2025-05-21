"""
This module contains the Book class that represents a physical book in the library system.
It inherits from MediaItem and adds book-specific properties like page count and condition.
"""

from library_system.models.media_item import MediaItem

class Book(MediaItem):
    def __init__(self, title: str, author: str, publication_date: str, isbn: str, 
                 page_count: int, condition: str):
        super().__init__(title, author, publication_date, isbn)
        self._page_count = page_count
        self._condition = condition
        self._validate_condition()

    def _validate_condition(self):
        """Validate the book's condition"""
        valid_conditions = ['new', 'good', 'fair', 'poor']
        if self._condition.lower() not in valid_conditions:
            raise ValueError(f"Invalid condition. Must be one of: {', '.join(valid_conditions)}")

    @property
    def page_count(self) -> int:
        return self._page_count

    @page_count.setter
    def page_count(self, value: int):
        if value <= 0:
            raise ValueError("Page count must be positive")
        self._page_count = value

    @property
    def condition(self) -> str:
        return self._condition

    @condition.setter
    def condition(self, value: str):
        self._condition = value
        self._validate_condition()

    def __str__(self) -> str:
        return f"{super().__str__()} - {self._page_count} pages, Condition: {self._condition}" 