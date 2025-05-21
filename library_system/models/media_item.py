"""
This module contains the base MediaItem class that represents a generic media item in the library system.
It serves as the parent class for all specific media types (Book, EBook, Audiobook).
"""

import re
from datetime import datetime

class MediaItem:
    def __init__(self, title: str, author: str, publication_date: str, isbn: str):
        self._title = title
        self._author = author
        self._publication_date = publication_date
        self._isbn = isbn
        self._is_available = True
        self._validate_isbn()

    def _validate_isbn(self):
        """Validate ISBN format using regular expression"""
        isbn_pattern = r'^\d{3}-\d{10}$'
        if not re.match(isbn_pattern, self._isbn):
            raise ValueError("Invalid ISBN format. Expected format: XXX-XXXXXXXXXX")

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        if not value.strip():
            raise ValueError("Title cannot be empty")
        self._title = value

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str):
        if not value.strip():
            raise ValueError("Author cannot be empty")
        self._author = value

    @property
    def publication_date(self) -> str:
        return self._publication_date

    @publication_date.setter
    def publication_date(self, value: str):
        try:
            datetime.strptime(value, '%Y-%m-%d')
            self._publication_date = value
        except ValueError:
            raise ValueError("Invalid date format. Expected format: YYYY-MM-DD")

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def is_available(self) -> bool:
        return self._is_available

    def check_out(self):
        if not self._is_available:
            raise ValueError("Item is already checked out")
        self._is_available = False

    def check_in(self):
        if self._is_available:
            raise ValueError("Item is already checked in")
        self._is_available = True

    def __str__(self) -> str:
        return f"{self._title} by {self._author} (ISBN: {self._isbn})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, MediaItem):
            return False
        return self._isbn == other._isbn 