import re

# Define the paths to the input and output files
input_file_path = 'C:/Users/hc158/GitHub/Python/BE_API_soundoftext/sqlite/rutraker/05_edit.txt'
output_file_path = 'C:/Users/hc158/GitHub/Python/BE_API_soundoftext/sqlite/rutraker/05_format.txt'

# Open the input file and read the contents
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    text = input_file.read()

# Transform the content into a single line
single_line_text = ' '.join(text.split())

# Adjust the regular expression to match words with hyphens, periods, and parentheses
# This pattern is designed to match a broader range of words before the [transcription]
# It now accommodates words with hyphens, periods, and optionally matches words with parentheses
formatted_text = re.sub(r' ([\w\.\-]+(\([\w\.\-]+\))? \[\S+\]) ', r'\n\1 ', single_line_text)

# Write the formatted text to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(formatted_text)

print("Transformation complete. The content has been reformatted and written to the output file.")
