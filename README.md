# 11labs Audio Transcriber
A script I wrote to help me transcribe audio from 11labs, since API free use is longer than UI use.

## Requirements
- Python 3 with modules:
  - venv
  - ElevenLabs
  - python-dotenv

## How to use
- Install the requirements with `./install`.
- Put an input MP3 audio file, named `input.mp3`.
- Create `.env`. Add ELEVENLABS_API_KEY=<Your ElevenLabs API key here>
- Run `./run`. It will output to `result.docx`.

## Note
How to use additional_formats option:

```
from elevenlabs import ElevenLabs, ExportOptions_Docx

transcription = client.speech_to_text.convert(
    model_id="scribe_v1",
    file=audio_data,
    additional_formats=[ExportOptions_Docx()]
)
```
