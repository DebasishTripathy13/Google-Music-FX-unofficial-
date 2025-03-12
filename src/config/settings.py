import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """
    Configuration settings for the application.
    Loads environment variables and provides defaults.
    """
    AUTH_TOKEN = os.getenv("AUTH_TOKEN")
    SESSION_ID = os.getenv("SESSION_ID")
    
    # New config options allowing user customization via environment variables
    MAX_GENERATION_COUNT = int(os.getenv("MAX_GENERATION_COUNT", 3))
    ALLOWED_SOUND_LENGTHS = [int(x) for x in os.getenv("ALLOWED_SOUND_LENGTHS", "30,50,70").split(",")]

    @staticmethod
    def get_credentials():
        """
        Get authentication credentials from environment variables or user input.
        
        Returns:
            tuple: (auth_token, session_id)
            
        Raises:
            ValueError: If either credential is missing
        """
        auth_token = Settings.AUTH_TOKEN or input("Please enter your Authorization token: ")
        session_id = Settings.SESSION_ID or input("Please enter your session ID: ")
        
        if not auth_token or not session_id:
            raise ValueError("Both AUTH_TOKEN and SESSION_ID are required.")
        
        return auth_token, session_id