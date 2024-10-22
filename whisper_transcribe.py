# Contact: tomas-salvador (https://github.com/tomas-salvador)

import whisper

# Load the Whisper model
model = whisper.load_model("base")  # Options: "tiny", "base", "small", "medium", "large"

# Load the audio file
audio_file = "your_audio.mp3"  # Change this to your audio file name

# Transcribe the audio
result = model.transcribe(audio_file)

# Print the transcription
print("Transcription:")
print(result['text'])
