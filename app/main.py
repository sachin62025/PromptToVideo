from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.routes import video
from app.utils.helpers import setup_directories

app = FastAPI()

# Setup required directories
setup_directories()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(video.router)

@app.get("/", response_class=HTMLResponse)
async def serve_home():
    with open("templates/index.html") as f:
        return f.read()
