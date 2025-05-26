from fastapi import APIRouter, Request
from app.services import llm_service, manim_service, tts_service, merge_service

router = APIRouter(prefix="/api")

@router.post("/generate")
async def generate_video(request: Request):
    data = await request.json()
    prompt = data.get("prompt")

    # Step 1: Call LLM
    manim_code = llm_service.generate_code(prompt)

    # Step 2: Save and run Manim
    video_path = manim_service.render_video(manim_code)

    # Skip audio and merge steps for now
    return {"video_url": f"/{video_path}"}
