import csv

def replace_in_file(source_file_path, csv_file_path, output_file_path):
    # Cargar las traducciones desde el archivo CSV
    translations = {}
    with open(csv_file_path, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            original_text = row[1]
            translated_text = row[0]
            translations['"' + original_text + '"'] = '"' + translated_text + '"'

    # Leer el contenido del archivo fuente
    with open(source_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Reemplazar el texto según las traducciones
    for original, translated in translations.items():
        content = content.replace(original, translated)

    # Guardar el contenido modificado en un nuevo archivo
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Uso del script
source_code_path = 'project.gbsproj'  # Cambia esto al path de tu archivo de código fuente
csv_path = 'translation_labels.csv'                  # Cambia esto al path de tu archivo CSV
output_path = 'project.gbsproj.out'                 # Path del archivo de salida

replace_in_file(source_code_path, csv_path, output_path)
