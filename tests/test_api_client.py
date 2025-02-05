import pytest
from src.services.api_client import APIClient

def test_generate_music():
    api_client = APIClient()
    with pytest.raises(Exception):
        api_client.generate_music("")  # Invalid prompt