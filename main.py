from src.services.api_client import APIClient
from src.utils.file_utils import generate_filename, save_audio_file
from src.utils.validation_utils import validate_music_prompt

def main():
    """
    Main function to run the Google Music FX application.
    Prompts the user for input, generates music, and saves the audio files.
    
    Handles exceptions and provides user feedback.
    """
    try:
        api_client = APIClient()
        music_prompt = input("Please enter a description for the music (e.g., 'anime background song for a sad plot twist'): ")
        validate_music_prompt(music_prompt)
        
        sounds = api_client.generate_music(music_prompt)
        
        for idx, sound in enumerate(sounds, start=1):
            file_name = generate_filename(music_prompt, idx)
            save_audio_file(sound["data"], file_name, sound["audioContainer"].lower())
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()