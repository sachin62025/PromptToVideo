import subprocess
import os
import shutil
from app.utils.logger import get_logger
import sys

logger = get_logger(__name__)

def render_video(code: str) -> str:
    """Generate and render a Manim scene from the provided code."""
    logger.info("Starting Manim video rendering")
    
    # Ensure all required directories exist
    os.makedirs("manim_scenes", exist_ok=True)
    os.makedirs("static", exist_ok=True)
    os.makedirs("media/videos/generated_scene/480p15", exist_ok=True)
    
    # Write the scene code to file
    scene_path = os.path.abspath("manim_scenes/generated_scene.py")
    try:
        with open(scene_path, "w") as f:
            f.write(code)
        logger.info(f"Successfully wrote scene code to {scene_path}")
    except Exception as e:
        logger.error(f"Error writing scene code: {str(e)}")
        raise Exception(f"Failed to write scene code: {str(e)}")

    # Get the Python executable path
    python_path = sys.executable
    
    # Run manim command with full paths
    cmd = [
        python_path,
        "-m",
        "manim",
        "-pql",  # Preview, quality low
        scene_path,
        "GeneratedScene"
    ]
    
    try:
        logger.info(f"Running Manim command: {' '.join(cmd)}")
        # Set environment variables
        env = os.environ.copy()
        env["PYTHONPATH"] = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        env["PYTHONIOENCODING"] = "utf-8"
        env["PYTHONUNBUFFERED"] = "1"
        
        # Create a new process group for Windows
        creation_flags = 0x08000000  # CREATE_NO_WINDOW
        
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True,
            env=env,
            creationflags=creation_flags if os.name == 'nt' else 0
        )
        logger.info("Manim command completed successfully")
        logger.debug(f"Manim output: {result.stdout}")
        
        # Find the generated video file
        media_dir = os.path.abspath("media/videos/generated_scene/480p15")
        video_file = os.path.join(media_dir, "GeneratedScene.mp4")
        
        if not os.path.exists(video_file):
            raise Exception(f"Generated video file not found at {video_file}")
            
        # Copy to static directory
        static_path = os.path.abspath("static/rendered.mp4")
        shutil.copy2(video_file, static_path)
        logger.info(f"Copied video to {static_path}")
        
        return static_path
    except subprocess.CalledProcessError as e:
        error_msg = f"Manim error: {str(e)}\nStderr: {e.stderr}"
        logger.error(error_msg)
        raise Exception(error_msg)
    except Exception as e:
        error_msg = f"Unexpected error in Manim rendering: {str(e)}"
        logger.error(error_msg)
        raise Exception(error_msg)
