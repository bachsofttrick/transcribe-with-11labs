import os
import json
import base64
from dotenv import load_dotenv
from elevenlabs import ElevenLabs, ExportOptions_Docx

def main():
    os.system('clear')

    # Load env
    print("Loading key...")
    load_dotenv()
    client = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
    )

    # Load mp3 file and transcribe
    audio_file = "input.mp3"
    print("Loading audio " + audio_file + " ...")
    with open(audio_file, "rb") as audio_data:
        print("Transcirbing...")
        transcription = client.speech_to_text.convert(
            file=audio_data,
            model_id="scribe_v2",
            diarize=True,
            tag_audio_events=False,
            language_code="en",
            additional_formats=[ExportOptions_Docx()]
        )

    # Get the base64 content
    base64_content = transcription.additional_formats[0].content

    # Decode base64 and save to Docx file
    docx_decoded = base64.b64decode(base64_content)
    docx_file = "result.docx"
    print ("Saving " + docx_file + " ...")
    with open(docx_file, "wb") as docx_data:
        docx_data.write(docx_decoded)

if __name__ == "__main__":
    main()