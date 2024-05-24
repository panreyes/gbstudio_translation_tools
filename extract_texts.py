import json
import csv

# Path to your JSON file
file_path = 'project.gbsproj'

def extract_text(data, collected_texts):
    if isinstance(data, dict):  # If the current item is a dictionary
        for key, value in data.items():
            # Check for specific text-containing keys
            if key in ['text', 'trueText', 'falseText', 'nameTag', 'option1', 'option2', 'option3', 'option4', 'option5', 'option6', 'option7', 'option8']:
                if isinstance(value, list):  # If the value is a list
                    # Process each line to exclude empty, whitespace-only, or numeric-only lines
                    processed_lines = [
                        line.replace('\n', '\\n').replace('\"', '\\"') 
                        for line in value 
                        if not (line.strip() == "" or line.isspace() or line.isdigit())
                    ]
                    collected_texts.extend(processed_lines)
                elif isinstance(value, str):  # If the value is a string
                    processed_line = value.replace('\n', '\\n').replace('\"', '\\"')
                    # Add the line if it is not empty, only whitespace, or only numbers
                    if not (value.strip() == "" or value.isspace() or value.isdigit()):
                        collected_texts.append(processed_line)
            else:
                extract_text(value, collected_texts)  # Recurse into the value
    elif isinstance(data, list):  # If the current item is a list
        for item in data:
            extract_text(item, collected_texts)  # Recurse into each item in the list

# Open the file with UTF-8 encoding
with open(file_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# List to store the collected text lines
all_text_lines = []
extract_text(json_data, all_text_lines)

# Set to track unique lines
unique_lines = set()

# CSV file path
csv_file_path = 'translation_labels.csv'

# Writing to CSV
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Line', 'Text'])
    # Write each line with a label, ensuring no duplicates and no undesired lines
    line_number = 1
    for line in all_text_lines:
        if line not in unique_lines:
            unique_lines.add(line)
            writer.writerow([f'LINE_{line_number}', line])
            line_number += 1

print(f"CSV file has been created at {csv_file_path}")
