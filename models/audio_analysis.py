from sqlalchemy import Column, String, Text, Integer, Float
from db.session import Base

class AudioAnalysis(Base):
    __tablename__ = 'audio_analysis'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255))
    summary = Column(Text)
    transcription = Column(Text)
    negative_score = Column(Float)
    neutral_score = Column(Float)
    positive_score = Column(Float)

