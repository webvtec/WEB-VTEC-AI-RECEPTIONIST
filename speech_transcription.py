import assemblyai as aai

class SpeechTranscriber:
    def __init__(self, api_key):
        aai.settings.api_key = api_key
        self.transcriber = None

    def start_transcription(self, on_data_callback):
        self.transcriber = aai.RealtimeTranscriber(
            sample_rate=16000,
            on_data=on_data_callback,
            end_utterance_silence_threshold=1000
        )
        self.transcriber.connect()
        microphone_stream = aai.extras.MicrophoneStream(sample_rate=16000)
        self.transcriber.stream(microphone_stream)

    def stop_transcription(self):
        if self.transcriber:
            self.transcriber.close()
            self.transcriber = None
