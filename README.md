# GBStudio translation tools v0.0.0.1
Created for translating the GBStudio game "A Cat & His Boy".

Thanks to GBStudio saving the whole project as a JSON file, we can easily extract all the texts and replace to and from a CSV file.

# Usage (very alpha!)
- extract_texts.py - Extracts all the known tags for texts from project.gbsproj and puts them in translation_labels.csv
- replace_texts_with_labels.py - Replaces in project.gbsproj all the extracted texts from project.gbsproj and saves it to project.gbsproj.out
- apply_translation.py - TBD.
