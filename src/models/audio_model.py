from dataclasses import dataclass

@dataclass
class AudioData:
    """
    Data class representing audio data from the API response.
    
    Attributes:
        data (str): Base64 encoded audio data
        audio_container (str): Format of the audio container (e.g., "MP3")
    """
    data: str 
    audio_container: str