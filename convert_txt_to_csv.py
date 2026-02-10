import re
import os

def parse_transcript_to_csv(input_file, output_file):
    """Convert transcript txt file to CSV format"""

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    csv_lines = ["from;to;speaker;content"]

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Match timestamp line: HH:MM:SS,mmm --> HH:MM:SS,mmm [speaker_X]
        match = re.match(r'(\d{2}:\d{2}:\d{2},\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2},\d{3})\s*\[speaker_(\d+)\]', line)

        if match:
            time_from = match.group(1)
            time_to = match.group(2)
            speaker = match.group(3)

            # Collect content lines until next timestamp or end of file
            content_lines = []
            i += 1

            while i < len(lines):
                next_line = lines[i].strip()

                # Check if next line is a timestamp (start of next entry)
                if re.match(r'\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*\d{2}:\d{2}:\d{2},\d{3}\s*\[speaker_\d+\]', next_line):
                    break

                # Add non-empty lines to content
                if next_line:
                    content_lines.append(next_line)

                i += 1

            # Join content lines with space
            content = ' '.join(content_lines)

            # Create CSV line
            if content:  # Only add if there's actual content
                csv_line = f"{time_from};{time_to};{speaker};{content}"
                csv_lines.append(csv_line)
        else:
            i += 1

    # Write CSV file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(csv_lines))

    print(f"Converted {input_file} -> {output_file}")
    print(f"Total entries: {len(csv_lines) - 1}")

# Process all txt files in the current directory
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]

for txt in txt_files:
    # Create CSV filename by replacing .docx with .csv
    csv_file = txt.replace('.txt', '.csv')

    try:
        parse_transcript_to_csv(txt, csv_file)
    except Exception as e:
        print(f"Error processing {txt}: {e}")

print(f"\nProcessed {len(txt_files)} files")
