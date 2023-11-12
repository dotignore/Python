# C:\Users\hc158\GitHub\Python\BE_API_soundoftext\Python\Scripts\python.exe C:/Users/hc158/GitHub/Python/BE_API_soundoftext/strange_behaviour.py
# ============ Load the JSON data parser start =================
# - Language In: en-US
# - Language Out: uk-UA
# - Silent: 1500
# - Lines_In: World, Jacket, Radio, Bag
# ============ Load the JSON data parser finish =================
# ========== Start translate text ==========
# - Lines_out ['Світ', 'Куртка', 'Радіо', 'Мішок']
# ###############################################
# lang en-US, lines ['World', 'Jacket', 'Radio', 'Bag'], lang uk-UA, lines ['Світ', 'Куртка', 'Радіо', 'Мішок'], silent 1500
# ###############################################
# qqq: en-US
# www: ['World', 'Jacket', 'Radio', 'Bag']
# eee: uk-UA
# rrr: ['Світ', 'Куртка', 'Радіо', 'Мішок']
# ttt: 1500
# 1qqq def - Silent: 1500
# ============================================================
#
# Process finished with exit code 0


import requests
import json
from googletrans import Translator
from association_langs import get_output_language
from json_data import json_data

# ============  translate text lang_in => lang_to  ============
def translator(lang_in_associated, lang_out_associated, lines_in):

    print(f'========== Start translate text ==========')
    def translate_to(text):
        translator = Translator()
        translation = translator.translate(text, src=lang_in_associated, dest=lang_out_associated)
        return translation.text

    #print(f"translations_in {lines_in}")
    lines_out = [translate_to(line) for line in lines_in]
    #print(f"translations_out {lines_out}")

    return lines_out
    #print(f'========== Finish translate text ==========')
# ============  translate text lang_in => lang_to  ============

# ==== POST Request ====

def api_soundoftext_com(qqq, www, eee, rrr, ttt):
    print(f"qqq: {qqq}")  # In Language: en-US
    print(f"www: {www}")  # Lines: World, Jacket, Radio, Bag
    print(f"eee: {eee}")  # Silent: 1500
    print(f"rrr: {rrr}")  # Out Language: uk-UA
    print(f"ttt: {ttt}")  # Lines: Світ, Куртка, Радіо, Мішок
    print(f"1qqq def - Silent: {silent}")  # Silent: 1500
    print('============================================================')

print('============ Load the JSON data parser start =================')
# Load the JSON data
parsed_data = json.loads(json_data)

# Parser JSON
lang_in = parsed_data["lang_in"]
lang_out = parsed_data["lang_out"]
silent = parsed_data["silent"]
lines_in = parsed_data["lines_in"]

# Print the values
print(f"- Language In: {lang_in}")        # In Language: en-US
print(f"- Language Out: {lang_out}")      # Out Language: uk-UA
print(f"- Silent: {silent}")              # Silent: 1500
print(f"- Lines_In: {', '.join(lines_in)}")  # Lines: World, Jacket, Radio, Bag
print('============ Load the JSON data parser finish =================')
# ============  json_data.py  ============
# ============  association_langs.py  ============
# Lang assosiace                def translator
lang_in_associated = get_output_language(lang_in)               # lang_in_associated en
lang_out_associated = get_output_language(lang_out)             # lang_out_associated uk
lines_out = translator(lang_in_associated, lang_out_associated, lines_in)
print(f"- Lines_out {lines_out}")

# print(f"###############################################")
# print(f"lang {lang_in}, lines {lines_in}, silent {silent}")         # lang en-US, lines ['World', 'Jacket', 'Radio', 'Bag'], silent 1500
# print(f"###############################################")
# api_soundoftext_com(lang_in, lines_in, silent)
#
# print(f"###############################################")
# print(f"lang {lang_out}, lines {lines_out}, silent {silent}")       # lang uk-UA, lines ['Світ', 'Куртка', 'Радіо', 'Мішок'], silent 1500
# print(f"###############################################")
# api_soundoftext_com(lang_out, lines_out, silent)

print(f"###############################################")
print(f"lang {lang_in}, lines {lines_in}, lang {lang_out}, lines {lines_out}, silent {silent}")       # lang uk-UA, lines ['Світ', 'Куртка', 'Радіо', 'Мішок'], silent 1500
print(f"###############################################")
api_soundoftext_com(lang_in, lines_in, lang_out, lines_out, silent)