"""
This is the main program file for the library system.
It demonstrates the functionality of the library management system with a simple command-line interface.
"""

import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from library_system.utils.library_manager import LibraryManager
from library_system.models.book import Book
from library_system.models.ebook import EBook
from library_system.models.audiobook import Audiobook

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <data_file>")
        sys.exit(1)

    data_file = sys.argv[1]
    library = LibraryManager(data_file)
    library.load_data()

    # Example usage
    try:
        # Create some sample items
        book = Book(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
            publication_date="1925-04-10",
            isbn="978-0743273565",
            page_count=180,
            condition="good"
        )

        ebook = EBook(
            title="Python Crash Course",
            author="Eric Matthes",
            publication_date="2019-05-03",
            isbn="978-1593279288",
            file_size_mb=5.2,
            format_type="pdf",
            download_url="https://example.com/python-crash-course.pdf"
        )

        audiobook = Audiobook(
            title="The Hobbit",
            author="J.R.R. Tolkien",
            publication_date="1937-09-21",
            isbn="978-0547928227",
            duration_minutes=683,
            narrator="Rob Inglis",
            audio_format="mp3"
        )

        # Add items to library
        library.add_item(book)
        library.add_item(ebook)
        library.add_item(audiobook)

        # Demonstrate filtering and sorting
        print("\nAll items sorted by title:")
        for item in library.sort_by_title():
            print(item)

        print("\nItems by author 'J.R.R. Tolkien':")
        for item in library.get_items_by_author("J.R.R. Tolkien"):
            print(item)

        print("\nAuthor statistics:")
        for author, count in library.get_author_stats().items():
            print(f"{author}: {count} items")

        # Demonstrate search functionality
        print("\nSearch results for 'Python':")
        for item in library.search_by_title("Python"):
            print(item)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 