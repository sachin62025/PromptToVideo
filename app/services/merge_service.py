from moviepy import VideoFileClip, AudioFileClip
import os

from app.utils.logger import get_logger
logger = get_logger(__name__)

def merge(video_path: str, audio_path: str) -> str:
    """Merge video and audio files into a final video."""
    # output_path = "outputs/final_video.mp4"
    output_path = "static/final_video.mp4"
    # os.makedirs("outputs", exist_ok=True)
    # os.makedirs("static", exist_ok=True)
    
    try:
        logger.info(f"Merging video: {video_path} and audio: {audio_path}")
        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)
        
        # If audio is longer than video, trim it
        if audio.duration > video.duration:
            audio = audio.with_duration(video.duration)
        
        logger.info(f"Video duration: {video.duration}, Audio duration: {audio.duration}")
        final_video = video.with_audio(audio)
        final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')
        
        # Clean up
        video.close()
        audio.close()
        final_video.close()
        logger.info(f"Final video saved to: {output_path}")
        return output_path
    
    except Exception as e:
        logger.error(f"Error merging video and audio: {str(e)}")
        # If there's an error, return the original video
        return video_path
