from elevenlabs import generate, stream

class TextToSpeech:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_audio(self, text):
        audio_stream = generate(
            api_key=self.api_key,
            text=text,
            voice="Rachel",
            stream=True
        )
        stream(audio_stream)
