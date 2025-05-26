import subprocess
import os
import shutil
from pathlib import Path

def test_manim():
    """Test if Manim is working correctly by rendering a test scene."""
    print("Starting Manim test...")
    
    # Ensure directories exist
    os.makedirs("media", exist_ok=True)
    os.makedirs("static", exist_ok=True)
    
    # Run manim command
    cmd = [
        "python",
        "-m",
        "manim",
        "-pql",  # Preview, quality low
        "manim_scenes/test_scene.py",
        "TestScene"
    ]
    
    try:
        print(f"Running Manim command: {' '.join(cmd)}")
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("Manim command completed successfully")
        print(f"Manim output: {result.stdout}")
        
        # Find the generated video file
        media_dir = "media/videos/test_scene/480p15"
        video_file = os.path.join(media_dir, "TestScene.mp4")
        
        if not os.path.exists(video_file):
            raise Exception(f"Generated video file not found at {video_file}")
            
        # Copy to static directory
        static_path = "static/test_video.mp4"
        shutil.copy2(video_file, static_path)
        print(f"Copied video to {static_path}")
        
        print("Test completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Manim error: {str(e)}")
        print(f"Manim stderr: {e.stderr}")
        return False
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return False

if __name__ == "__main__":
    test_manim() 