from services.transcribe_audio import transcribe_audio_content

def test_transcribe_audio_content():
    audio_file_path = "static/test_transcribe.flac"
    transcript = transcribe_audio_content(speech_file=audio_file_path, model='default')
    assert "slushy" in transcript.lower()