from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
from services.transcribe_audio import transcribe_audio_content

import os

router = APIRouter()

AUDIO_PATH = "uploaded_audio/"

@router.get("/")
def read_root():
    return {"Audio":"OK"}

@router.post("/upload/")
async def upload_audio(file: UploadFile = File(...)):
    try:
        data = await file.read()

        Path(AUDIO_PATH).mkdir(parents=True, exist_ok=True)
        path_to_audio = os.path.join(AUDIO_PATH, file.filename)

        with open(path_to_audio, 'wb') as f:
            f.write(data)

        audio_text = transcribe_audio_content(path_to_audio)

        return {"filename": file.filename, "message": "File uploaded successfully!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="File upload failed.")

