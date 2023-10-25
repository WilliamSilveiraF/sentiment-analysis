from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import shutil
from pathlib import Path
import os

router = APIRouter()

AUDIO_PATH = "uploaded_audio/"

@router.get("/")
def read_root():
    return {"Audio":"OK"}

@router.post("/upload/")
async def upload_audio(file: UploadFile = File(...)):
    try:
        Path(AUDIO_PATH).mkdir(parents=True, exist_ok=True)

        with open(os.path(AUDIO_PATH, file.filename), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        return {"filename": file.filename, "message": "File uploaded successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="File upload failed.")

