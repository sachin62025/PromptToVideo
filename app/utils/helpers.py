import os

def setup_directories():
    """Create all required directories for the application."""
    directories = [
        "static",
        "media",
        "media/videos",
        "media/videos/generated_scene",
        "media/videos/generated_scene/480p15",
        "outputs",
        "logs",
        "manim_scenes"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
