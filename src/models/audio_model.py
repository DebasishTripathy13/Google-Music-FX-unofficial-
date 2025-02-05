from dataclasses import dataclass

@dataclass
class AudioData:
    data: str  # Base64-encoded audio data
    audio_container: str  # Format (e.g., mp3, wav)