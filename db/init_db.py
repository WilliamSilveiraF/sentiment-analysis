from db.session import engine
from models import audio_analysis

def init_db():
    audio_analysis.Base.metadata.create_all(bind=engine)