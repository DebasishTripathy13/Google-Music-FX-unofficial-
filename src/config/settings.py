import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    AUTH_TOKEN = os.getenv("AUTH_TOKEN")
    SESSION_ID = os.getenv("SESSION_ID")

    @staticmethod
    def get_credentials():
        auth_token = Settings.AUTH_TOKEN or input("Please enter your Authorization token: ")
        session_id = Settings.SESSION_ID or input("Please enter your session ID: ")
        
        if not auth_token or not session_id:
            raise ValueError("Both AUTH_TOKEN and SESSION_ID are required.")
        
        return auth_token, session_id