# PythonProject

# Library Management System

A Python-based library management system that handles different types of media items (books, ebooks, and audiobooks) with proper inheritance, encapsulation, and data manipulation capabilities.

## Project Structure

```
library_system/
├── models/
│   ├── media_item.py      # Base class for all media items
│   ├── book.py            # Physical book implementation
│   ├── ebook.py           # Ebook implementation
│   └── audiobook.py       # Audiobook implementation
├── utils/
│   └── library_manager.py # Handles file operations and data manipulation
└── main.py                # Main program entry point
```

## Features

- Three-level class hierarchy with proper inheritance
- Encapsulation with private members and getters/setters
- Data validation using regular expressions
- File operations (JSON read/write)
- Data manipulation (filtering, sorting, aggregation)
- Polymorphic methods
- Operator overloading

## Requirements

- Python 3.6 or higher

## Usage

1. Run the program with a data file path as an argument:
   ```bash
   python library_system/main.py data/library.json
   ```

2. The program will:
   - Load existing data from the specified JSON file
   - Add sample media items
   - Demonstrate various operations (filtering, sorting, searching)
   - Save the updated data back to the file

## Class Hierarchy

- `MediaItem` (Base class)
  - `Book` (Physical book)
  - `EBook` (Electronic book)
  - `Audiobook` (Audio book)

## Data Validation

The system includes several validation features:
- ISBN format validation using regex
- URL format validation for ebooks
- Date format validation
- Format type validation for ebooks and audiobooks
- Condition validation for physical books

## Data Manipulation

The `LibraryManager` class provides various data manipulation methods:
- Filtering by author
- Sorting by title or author
- Searching by title
- Getting author statistics
- Managing item availability 
