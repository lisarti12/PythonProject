"""
This module contains the EBook class that represents an electronic book in the library system.
It inherits from MediaItem and adds ebook-specific properties like file size and format.
"""

import re
from library_system.models.media_item import MediaItem

class EBook(MediaItem):
    def __init__(self, title: str, author: str, publication_date: str, isbn: str,
                 file_size_mb: float, format_type: str, download_url: str):
        super().__init__(title, author, publication_date, isbn)
        self._file_size_mb = file_size_mb
        self._format_type = format_type
        self._download_url = download_url
        self._validate_format()
        self._validate_url()

    def _validate_format(self):
        """Validate the ebook format"""
        valid_formats = ['pdf', 'epub', 'mobi', 'azw3']
        if self._format_type.lower() not in valid_formats:
            raise ValueError(f"Invalid format. Must be one of: {', '.join(valid_formats)}")

    def _validate_url(self):
        """Validate the download URL using regular expression"""
        url_pattern = r'^https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)$'
        if not re.match(url_pattern, self._download_url):
            raise ValueError("Invalid download URL format")

    @property
    def file_size_mb(self) -> float:
        return self._file_size_mb

    @file_size_mb.setter
    def file_size_mb(self, value: float):
        if value <= 0:
            raise ValueError("File size must be positive")
        self._file_size_mb = value

    @property
    def format_type(self) -> str:
        return self._format_type

    @format_type.setter
    def format_type(self, value: str):
        self._format_type = value
        self._validate_format()

    @property
    def download_url(self) -> str:
        return self._download_url

    @download_url.setter
    def download_url(self, value: str):
        self._download_url = value
        self._validate_url()

    def __str__(self) -> str:
        return f"{super().__str__()} - {self._format_type.upper()}, {self._file_size_mb}MB" 