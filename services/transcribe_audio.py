from google.cloud import speech

def transcribe_audio_content(speech_file: str) -> speech.RecognizeResponse:

    client = speech.SpeechClient()

    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig( # TODO SUPPORT DIFFERENT TYPES OF AUDIO
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)
    
    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        
        return alternative.transcript