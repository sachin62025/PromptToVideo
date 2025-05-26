from fastapi import APIRouter, Request, HTTPException
from app.services import llm_service, manim_service, tts_service, merge_service
from app.utils.logger import get_logger

logger = get_logger(__name__)
router = APIRouter(prefix="/api")

@router.post("/generate")
async def generate_video(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt")
        logger.info(f"Received video generation request for prompt: {prompt}")

        if not prompt:
            logger.error("No prompt provided in request")
            raise HTTPException(status_code=400, detail="Prompt is required")

        # Step 1: Call LLM
        logger.info("Generating Manim code using LLM")
        manim_code = llm_service.generate_code(prompt)

        # Step 2: Save and run Manim
        logger.info("Rendering video with Manim")
        video_path = manim_service.render_video(manim_code)

        # Step 3 (Optional): Generate voice
        logger.info("Generating audio")
        audio_path = tts_service.generate_audio(prompt)

        # Step 4: Merge
        logger.info("Merging video and audio")
        final_path = merge_service.merge(video_path, audio_path)

        logger.info(f"Video generation completed successfully: {final_path}")
        return {"video_url": "/static/final_video.mp4"}

    except Exception as e:
        logger.error(f"Error in video generation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
