from fastapi import FastAPI
from api.routes import audio
from middlewares import cors_middleware
import db

db.services.create_tables()

app = FastAPI()

cors_middleware.setup_cors(app)

app.include_router(audio.router)
