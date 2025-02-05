def validate_music_prompt(prompt):
    if not prompt or len(prompt.strip()) == 0:
        raise ValueError("Music prompt cannot be empty.")
    return prompt