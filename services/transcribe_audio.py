from google.cloud import speech
from pydub.utils import mediainfo

def map_audio_properties_to_encoding(audio_properties):
    encoding_map = {
        ('pcm_s16le', None): 'LINEAR16',
        ('flac', None): 'FLAC',
        ('mulaw', None): 'MULAW',
        ('amr-nb', None): 'AMR',
        ('amr-wb', None): 'AMR_WB',
        ('opus', 'ogg'): 'OGG_OPUS',
        ('speex', None): 'SPEEX_WITH_HEADER_BYTE',
        ('opus', 'webm'): 'WEBM_OPUS',
    }
    
    codec_container_tuple = (
        audio_properties.get('codec_name', '').lower(),
        audio_properties.get('format_name', '').lower()
    )

    encoding_str = encoding_map.get(codec_container_tuple, 'ENCODING_UNSPECIFIED')
    return getattr(speech.RecognitionConfig.AudioEncoding, encoding_str)


def transcribe_audio_content(speech_file: str, model: str) -> str:

    client = speech.SpeechClient()
    
    audio_properties = mediainfo(speech_file)
    encoding = map_audio_properties_to_encoding(audio_properties)

    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=encoding,
        sample_rate_hertz=int(audio_properties['sample_rate']),
        language_code="en-US",
        model=model
    )

    response = client.recognize(config=config, audio=audio)
    
    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        
        return alternative.transcript