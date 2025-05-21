"""
This module contains the LibraryManager class that handles file operations and data manipulation
for the library system. It provides functionality to read/write media items from/to files,
filter, sort, and aggregate data.
"""

import json
import os
from typing import List, Dict, Any
from library_system.models.media_item import MediaItem
from library_system.models.book import Book
from library_system.models.ebook import EBook
from library_system.models.audiobook import Audiobook

class LibraryManager:
    def __init__(self, data_file: str):
        self._data_file = data_file
        self._media_items: List[MediaItem] = []
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(data_file), exist_ok=True)
        # Initialize the file if it doesn't exist
        if not os.path.exists(data_file):
            self._initialize_file()

    def _initialize_file(self) -> None:
        """Initialize the data file with an empty list"""
        with open(self._data_file, 'w') as file:
            json.dump([], file)

    def load_data(self) -> None:
        """Load media items from JSON file"""
        try:
            with open(self._data_file, 'r') as file:
                content = file.read()
                if not content.strip():  # If file is empty
                    self._media_items = []
                else:
                    data = json.loads(content)
                    self._media_items = self._deserialize_items(data)
        except (FileNotFoundError, json.JSONDecodeError):
            self._media_items = []
            self._initialize_file()

    def save_data(self) -> None:
        """Save media items to JSON file"""
        with open(self._data_file, 'w') as file:
            json.dump(self._serialize_items(), file, indent=4)

    def _deserialize_items(self, data: List[Dict[str, Any]]) -> List[MediaItem]:
        """Convert JSON data to MediaItem objects"""
        items = []
        for item_data in data:
            item_type = item_data.pop('type')
            if item_type == 'book':
                items.append(Book(**item_data))
            elif item_type == 'ebook':
                items.append(EBook(**item_data))
            elif item_type == 'audiobook':
                items.append(Audiobook(**item_data))
        return items

    def _serialize_items(self) -> List[Dict[str, Any]]:
        """Convert MediaItem objects to JSON-serializable data"""
        serialized_items = []
        for item in self._media_items:
            item_dict = item.__dict__.copy()
            # Add type information for deserialization
            if isinstance(item, Book):
                item_dict['type'] = 'book'
            elif isinstance(item, EBook):
                item_dict['type'] = 'ebook'
            elif isinstance(item, Audiobook):
                item_dict['type'] = 'audiobook'
            serialized_items.append(item_dict)
        return serialized_items

    def add_item(self, item: MediaItem) -> None:
        """Add a new media item to the library"""
        self._media_items.append(item)
        self.save_data()

    def remove_item(self, isbn: str) -> None:
        """Remove a media item by ISBN"""
        self._media_items = [item for item in self._media_items if item.isbn != isbn]
        self.save_data()

    def get_items_by_author(self, author: str) -> List[MediaItem]:
        """Filter items by author"""
        return [item for item in self._media_items if item.author.lower() == author.lower()]

    def get_available_items(self) -> List[MediaItem]:
        """Get all available items"""
        return [item for item in self._media_items if item.is_available]

    def sort_by_title(self) -> List[MediaItem]:
        """Sort items by title"""
        return sorted(self._media_items, key=lambda x: x.title)

    def sort_by_author(self) -> List[MediaItem]:
        """Sort items by author"""
        return sorted(self._media_items, key=lambda x: x.author)

    def get_author_stats(self) -> Dict[str, int]:
        """Get statistics about items per author"""
        stats = {}
        for item in self._media_items:
            stats[item.author] = stats.get(item.author, 0) + 1
        return stats

    def search_by_title(self, query: str) -> List[MediaItem]:
        """Search items by title using case-insensitive partial matching"""
        return [item for item in self._media_items if query.lower() in item.title.lower()] 