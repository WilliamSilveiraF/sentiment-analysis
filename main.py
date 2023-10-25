from fastapi import FastAPI
from api.routes import audio
from api.middlewares import cors_middleware

app = FastAPI()

cors_middleware.setup_cors(app)

app.include_router(audio.router)