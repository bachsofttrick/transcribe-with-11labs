import re
from docx import Document
import csv
import os

def parse_transcript_to_csv(docx_path, csv_path):
    """
    Read a docx file containing transcript data and convert to CSV format.
    Format: from;to;speaker;content
    """
    # Read the docx file
    doc = Document(docx_path)

    # Extract all text from paragraphs
    full_text = '\n'.join([para.text for para in doc.paragraphs if para.text.strip()])

    # Pattern to match: timestamp --> timestamp [speaker_X]
    # Followed by content on the next line(s)
    pattern = r'(\d{2}:\d{2}:\d{2},\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2},\d{3})\s*\[speaker_(\d+)\]\s*\n(.*?)(?=\n\d{2}:\d{2}:\d{2},\d{3}\s*-->|\Z)'

    matches = re.findall(pattern, full_text, re.DOTALL)

    # Write to CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['from', 'to', 'speaker', 'content'])

        for match in matches:
            from_time = match[0]
            to_time = match[1]
            speaker = match[2]
            content = match[3].strip().replace('\n', ' ')

            writer.writerow([from_time, to_time, speaker, content])

    print(f"Converted {docx_path} -> {csv_path}")
    print(f"Found {len(matches)} transcript entries")

# Process all docx files in the current directory
docx_files = [f for f in os.listdir('.') if f.endswith('.docx')]

for docx_file in docx_files:
    # Create CSV filename by replacing .docx with .csv
    csv_file = docx_file.replace('.docx', '.csv')

    try:
        parse_transcript_to_csv(docx_file, csv_file)
    except Exception as e:
        print(f"Error processing {docx_file}: {e}")

print(f"\nProcessed {len(docx_files)} files")
