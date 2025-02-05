import pytest
from src.utils.file_utils import generate_filename

def test_generate_filename():
    assert generate_filename("test song", 1) == "test_song_sound_1.mp3"
    assert generate_filename("a" * 100, 2) == "a" * 50 + "_sound_2.mp3"