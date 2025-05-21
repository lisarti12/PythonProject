"""
This module contains the Audiobook class that represents an audiobook in the library system.
It inherits from MediaItem and adds audiobook-specific properties like duration and narrator.
"""

import re
from library_system.models.media_item import MediaItem

class Audiobook(MediaItem):
    def __init__(self, title: str, author: str, publication_date: str, isbn: str,
                 duration_minutes: int, narrator: str, audio_format: str):
        super().__init__(title, author, publication_date, isbn)
        self._duration_minutes = duration_minutes
        self._narrator = narrator
        self._audio_format = audio_format
        self._validate_audio_format()

    def _validate_audio_format(self):
        """Validate the audio format"""
        valid_formats = ['mp3', 'aac', 'wav', 'm4b']
        if self._audio_format.lower() not in valid_formats:
            raise ValueError(f"Invalid audio format. Must be one of: {', '.join(valid_formats)}")

    @property
    def duration_minutes(self) -> int:
        return self._duration_minutes

    @duration_minutes.setter
    def duration_minutes(self, value: int):
        if value <= 0:
            raise ValueError("Duration must be positive")
        self._duration_minutes = value

    @property
    def narrator(self) -> str:
        return self._narrator

    @narrator.setter
    def narrator(self, value: str):
        if not value.strip():
            raise ValueError("Narrator cannot be empty")
        self._narrator = value

    @property
    def audio_format(self) -> str:
        return self._audio_format

    @audio_format.setter
    def audio_format(self, value: str):
        self._audio_format = value
        self._validate_audio_format()

    def __str__(self) -> str:
        hours = self._duration_minutes // 60
        minutes = self._duration_minutes % 60
        return f"{super().__str__()} - Narrated by {self._narrator}, {hours}h {minutes}m ({self._audio_format.upper()})" 