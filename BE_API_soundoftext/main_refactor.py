import requests
import json
from googletrans import Translator
from association_langs import get_output_language
from json_data import json_data

def translate_lines(lines_in):
    print(f'|| Start translate from {lang_in} to {lang_out}')
    print(f'|| Print lines{lines_in}')





def translator(lines_in):
    from googletrans import Translator

    def translate_to(text):
        translator = Translator()
        translation = translator.translate(text, src='en', dest='uk')
        return translation.text

    # Read input file
    with open('input.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    translations = [translate_to(line.strip()) for line in lines]

    for translation in translations:
        print(translation)

    with open('output.txt', 'w', encoding='utf-8') as file:
        for translation in translations:
            file.write(translation + '\n')





# ============  json_data.py  ============

# Load the JSON data
parsed_data = json.loads(json_data)

# Parser JSON
lang_in = parsed_data["lang_in"]
lang_out = parsed_data["lang_out"]
silent = parsed_data["silent"]
lines_in = parsed_data["lines_in"]

# Print the values
# print(f"In Language: {lang_in}")
# print(f"Out Language: {lang_out}")
# print(f"Silent: {silent}")
print(f"Lines: {', '.join(lines_in)}")

# ============  json_data.py  ============

# ============  association_langs.py  ============

# Lang assosiace
lang_in_associated = get_output_language(lang_in)
lang_out_associated = get_output_language(lang_out)

print(f"lang_in: {lang_in} ==> {lang_in_associated}")       # lang_in: en-US ==> en
print(f"lang_in: {lang_out} ==> {lang_out_associated}")     # lang_in: uk-UA ==> uk

# ============  association_langs.py  ============






# input
#
# API parameters
# lang
# Engin
# Word
#
# module POST
# module GET
#
    # Google translate
    # lang1 -> lang2
#
# name of file _ln.mp3, -ln.mp3
#
# silense time 1500 ms
#
# modul rename file lang
#
# modile download

