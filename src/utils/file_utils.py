import re
import base64

def generate_filename(text, sound_number):
    cleaned_name = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    cleaned_name = cleaned_name.replace(" ", "_")[:50]
    return f"{cleaned_name}_sound_{sound_number}.mp3"

def save_audio_file(audio_data, file_name, media_format):
    try:
        audio_bytes = base64.b64decode(audio_data)
        with open(file_name, "wb") as audio_file:
            audio_file.write(audio_bytes)
        print(f"Audio file saved as {file_name}")
    except Exception as e:
        print(f"Failed to save audio file: {e}")