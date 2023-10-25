from fastapi import FastAPI
from api.routes import audio

app = FastAPI()

app.include_router(audio.router)