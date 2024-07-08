import csv

def replace_in_file(source_file_path, csv_file_path, output_file_path):
    # Load translations from CSV file
    translations = {}
    with open(csv_file_path, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            original_text = row[0]   #row 0 contains the labels to be replaced
            translated_text = row[1] #row 1 contains english translations
            translations['"' + original_text + '"'] = '"' + translated_text + '"'

    # Read source code
    with open(source_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace text labels with translations
    for original, translated in translations.items():
        content = content.replace(original, translated)

    # Save the modified content in a new file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Script options
source_code_path = 'project.gbsproj.labeled'  # Change this to the path of your GB Studio project file (.gbsproj)
csv_path = 'translations.csv'                 # Change this to the path of your CSV file
output_path = 'project-en.gbsproj'            # Output file path

replace_in_file(source_code_path, csv_path, output_path)
