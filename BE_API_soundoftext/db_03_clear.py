import re

# Assuming the pattern to remove is time, English word, and dash, like "13:10:49 the - "
pattern_to_remove = r"\d{2}:\d{2}:\d{2}\t\w+\s-\s"

# Путь к исходному файлу
input_path = r"C:\Users\hc158\GitHub\Python\BE_API_soundoftext\sqlite\words_ru_20k.txt"
# Путь к файлу для сохранения очищенных данных
output_path = r"C:\Users\hc158\GitHub\Python\BE_API_soundoftext\sqlite\words_ru_20k_clear.txt"

# Reading the lines from the input file
with open(input_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Cleaning each line according to the specified pattern
cleaned_lines = [re.sub(pattern_to_remove, "", line) for line in lines]

# Writing the cleaned lines to the output file
with open(output_path, 'w', encoding='utf-8') as file:
    file.writelines(cleaned_lines)

print(f"Data has been cleaned and saved to {output_path}")
