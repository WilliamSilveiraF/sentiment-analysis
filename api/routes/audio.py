from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from pathlib import Path
from services import summary, sentiment_calculator, transcribe_audio
from models.audio_analysis import AudioAnalysis
from sqlalchemy.orm import Session
from db.utils import get_db
import os

router = APIRouter()

AUDIO_PATH = "uploaded_audio/"

@router.get("/")
def read_root():
    return {"Audio":"OK"}

@router.post("/upload/")
async def upload_audio(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    try:
        data = await file.read()

        Path(AUDIO_PATH).mkdir(parents=True, exist_ok=True)
        path_to_audio = os.path.join(AUDIO_PATH, file.filename)

        with open(path_to_audio, 'wb') as f:
            f.write(data)

        transcription = transcribe_audio.transcribe_audio_content(path_to_audio)
        summary_text = summary.generate_summary(transcription)
        sentiment_scores = sentiment_calculator.sentiment_score(transcription)

        audio_analysis = AudioAnalysis(
            filename=file.filename,
            summary=summary_text,
            transcription=transcription,
            negative_score=sentiment_scores['negative_score'],
            neutral_score=sentiment_scores['neutral_score'],
            positive_score=sentiment_scores['positive_score']
        )

        db.add(audio_analysis)
        db.commit()
        
        return {"audio_id": audio_analysis.id, "message": "File uploaded successfully!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="File upload failed.")

@router.get("/audio/{audio_id}")
def get_audio_by_id(
    audio_id: int,
    db: Session = Depends(get_db)
):
    audio_analysis = db.query(AudioAnalysis).filter(AudioAnalysis.id == audio_id).first()
    if audio_analysis:
        return audio_analysis
    else:
        raise HTTPException(status_code=404, detail="Audio not found.")