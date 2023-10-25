from fastapi import FastAPI, Depends
from api.routes import audio
from middlewares import cors_middleware
from typing import Annotated
from sqlalchemy.orm import Session
from db.init_db import init_db
from db.utils import get_db


app = FastAPI()

@app.on_event("startup")
async def startup_event():
    init_db()

cors_middleware.setup_cors(app)

db_dependency = Annotated[Session, Depends(get_db)]

app.include_router(audio.router)
