import os
import json
import base64
from dotenv import load_dotenv
from elevenlabs import ElevenLabs, ExportOptions_Txt
from convert_txt_to_csv import parse_transcript_to_csv

def main():
    os.system('clear')

    # Load env
    print("Loading key...")
    load_dotenv()
    client = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
    )

    # Load mp3 file and transcribe
    audio_file = "Participant 3.m4a"
    print("Loading audio " + audio_file + " ...")
    with open(audio_file, "rb") as audio_data:
        print("Transcribing...")
        transcription = client.speech_to_text.convert(
            file=audio_data,
            model_id="scribe_v2",
            diarize=True,
            tag_audio_events=False,
            language_code="en",
            additional_formats=[ExportOptions_Txt()]
        )

    # Get the base64 content
    content = transcription.additional_formats[0].content

    txt_file = "result.txt"
    print ("Saving " + txt_file + " ...")
    with open(txt_file, "w") as txt:
        txt.write(content)
    
    # Convert to csv
    csv_file = txt_file.replace('.txt', '.csv')
    parse_transcript_to_csv(txt_file, csv_file)


if __name__ == "__main__":
    main()