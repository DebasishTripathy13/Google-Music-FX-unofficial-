import requests
from src.config.settings import Settings

class APIClient:
    def __init__(self):
        self.url = "https://aisandbox-pa.googleapis.com/v1:soundDemo"
        self.auth_token, self.session_id = Settings.get_credentials()

    def generate_music(self, music_prompt, generation_count=2, loop=False, sound_length_seconds=70, model="DEFAULT"):
        headers = {
            "Authorization": f"Bearer {self.auth_token}",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "*/*"
        }
        
        payload = {
            "generationCount": generation_count,
            "input": {"textInput": music_prompt},
            "loop": loop,
            "soundLengthSeconds": sound_length_seconds,
            "model": model,
            "clientContext": {
                "tool": "MUSICLM_V2",
                "sessionId": self.session_id
            }
        }
        
        response = requests.post(self.url, headers=headers, json=payload)
        
        if response.status_code == 200:
            response_data = response.json()
            if "sounds" in response_data and response_data["sounds"]:
                return response_data["sounds"]
            else:
                raise ValueError("No audio data found in the response.")
        else:
            raise Exception(f"Request failed with status code {response.status_code}: {response.text}")