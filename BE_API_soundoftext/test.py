for i in range(2):
    if i == 0:
        print("Выполняется первый раз")
        # Ваш код для первой итерации
    if i == 1:
        print("Выполняется второй раз")
        # Ваш код для второй итерации



# def api_soundoftext_com(lang1, lang2=None, lang3=None):
#     if lang2 is not None:
#         # Process the first case with lang1 and lang2
#         print(f"Processing first case with lang1: {lang1}, lang2: {lang2}")
#
#     if lang3 is not None:
#         # Process the second case with lang1 and lang3
#         print(f"Processing second case with lang1: {lang1}, lang3: {lang3}")
#
# lang2="Spanish"
# lang3="French"
#
# # Example usage:
# api_soundoftext_com("English", lang2)
# api_soundoftext_com("English", lang3)

# ============== JSON DATA  ==============

# def get_output_language(lang_in):
#     language_mapping = {
#         "af-ZA": "af",
#         "ar-AE": "ar",
#         "bn-IN": "bn",
#         "bs": "bs",
#         "ca-ES": "ca",
#         "cs-CZ": "cs",
#         "cy": "cy",
#         "da-DK": "da",
#         "de-DE": "de",
#         "el-GR": "el",
#         "en-US": "en",
#         "en-GB": "en",
#         "en-AU": "en",
#         "eo": "eo",
#         "es-ES": "es",
#         "es-MX": "es",
#         "et": "et",
#         "fi-FI": "fi",
#         "fr-FR": "fr",
#         "fr-CA": "fr",
#         "fil-PH": "fr",
#         "gu": "gu",
#         "hi-IN": "hi",
#         "hr-HR": "hr",
#         "hu-HU": "hu",
#         "hy": "hy",
#         "id-ID": "id",
#         "is-IS": "is",
#         "it-IT": "it",
#         "ja-JP": "ja",
#         "km": "km",
#         "kn": "kn",
#         "ko-KR": "ko",
#         "la": "la",
#         "lv": "lv",
#         "mk": "mk",
#         "ml": "ml",
#         "mr": "mr",
#         "my": "my",
#         "ne": "ne",
#         "nl-NL": "nl",
#         "nb-NO": "no",
#         "pl-PL": "pl",
#         "pt-BR": "pt",
#         "ro-RO": "ro",
#         "ru-RU": "ru",
#         "si": "si",
#         "sk-SK": "sk",
#         "sq": "sq",
#         "sr-RS": "sr",
#         "sv-SE": "sv",
#         "sw": "sw",
#         "ta": "ta",
#         "te": "te",
#         "th-TH": "th",
#         "tr-TR": "tr",
#         "uk-UA": "uk",
#         "ur": "ur",
#         "vi-VN": "vi",
#         "cmn-Hant-TW": "zh-tw",
#         "cmn-Hant-TW": "zh-cn"
#     }
#     return language_mapping.get(lang_in, lang_in)
#
# # Example usage
# lang_in = "af-ZA"
# lang_out = get_output_language(lang_in)
# print(f"lang_in: {lang_out} lanf_out: {lang_in}")  # This will print "af"
#
# lang_in = "ar-AE"
# lang_out = get_output_language(lang_in)
# print(f"lang_in: {lang_out} lanf_out: {lang_in}")  # This will print "af"
#
# lang_in = "uk-UA"
# lang_out = get_output_language(lang_in)
# print(f"lang_in: {lang_out} lanf_out: {lang_in}")  # This will print "af"
#
# lang_in = "en-US"
# lang_out = get_output_language(lang_in)
# print(f"lang_in: {lang_out} lanf_out: {lang_in}")  # This will print "af"


# ============== JSON DATA  ==============

# ============== JSON import 2 ==============

# import json
#
# def translate_to(lang_in, lang_out, lines_in):
#     print('Start translate from EN input.txt to UK output.txt')
#
#     print(f'Print lang in = {lang_in}')
#     print(f'Print lang out = {lang_out}')
#     print(f'Print line in ={lines_in}')
#
#     if en-US
#
#     from googletrans import Translator
#     def translate_to(text):
#         translator = Translator()
#         translation = translator.translate(text, src='en', dest='uk')
#         return translation.text
#
#     translations = [translate_to(line.strip()) for line in lines_in]
#
#     for translation in translations:
#         print(translation)
#
#     with open('output.txt', 'w', encoding='utf-8') as file:
#         for translation in translations:
#             file.write(translation + '\n')
#
#     print('Finish translate from EN to UK input.txt => output.txt\n')
#
# json_data = '''
# {
#     "lang_in": "en-US",
#     "lang_out": "uk-UA",
#     "silent": 1500,
#     "lines_in": [
#         "World",
#         "Jacket",
#         "Radio",
#         "Bag"
#     ]
# }
# '''
#
# # Load the JSON data
# parsed_data = json.loads(json_data)
#
# # Access the values
# lang_in = parsed_data["lang_in"]
# lang_out = parsed_data["lang_out"]
# silent = parsed_data["silent"]
# lines_in = parsed_data["lines_in"]
#
# # Call the function
# translate_to(lang_in, lang_out, lines_in)


# ============== JSON import 2 ==============




# ============== JSON import 1 ==============
# import json
#
# json_data = '''
# {
#     "in_lang": "en-US",
#     "out_lang": "uk-UA",
#     "silent": 1500,
#     "lines": [
#         "World",
#         "Jacket",
#         "Radio",
#         "Bag"
#     ]
# }
# '''
#
# # Load the JSON data
# parsed_data = json.loads(json_data)
#
# # Access the values
# in_lang = parsed_data["in_lang"]    # In Language: en-US
# out_lang = parsed_data["out_lang"]  # Out Language: uk-UA
# silent = parsed_data["silent"]      # Silent: 1500
# lines = parsed_data["lines"]        # Lines: World, Jacket, Radio, Bag
#
# # Print the values
# print(f"In Language: {in_lang}")
# print(f"Out Language: {out_lang}")
# print(f"Silent: {silent}")
# print(f"Lines: {', '.join(lines)}")


# ============== JSON import 1 ==============

# ==============   Translate SCRIPT 4  ==============

# # Read input.txt and output.txt
# with open('input.txt', 'r', encoding='utf-8') as input_file:
#     input_lines = input_file.read().splitlines()
#
# with open('output.txt', 'r', encoding='utf-8') as output_file:
#     output_lines = output_file.read().splitlines()
#
# # Create a dictionary to map input to output
# mapping = dict(zip(output_lines, input_lines))
#
# # Print the mapped values
#
# for item in output_lines:
#     output_value = mapping.get(item, "Not Found")
#     print(f'{item} -> {output_value}')

# Світ -> World
# Куртка -> Jacket
# Радіо -> Radio
# Мішок -> Bag



# # Read input.txt and output.txt
# with open('input.txt', 'r', encoding='utf-8') as input_file:
#     input_lines = input_file.read().splitlines()
#
# with open('output.txt', 'r', encoding='utf-8') as output_file:
#     output_lines = output_file.read().splitlines()
#
# # Create a dictionary to map input to output
# mapping = dict(zip(input_lines, output_lines))
#
# # Print the mapped values
#
# for item in input_lines:
#     output_value = mapping.get(item, "Not Found")
#     print(f'{item} -> {output_value}')
#
#
# World -> Світ
# Jacket -> Куртка
# Radio -> Радіо
# Bag -> Мішок

# ==============   Translate SCRIPT 4  ==============


# ==============   Translate SCRIPT 3  ==============

# # https://py-googletrans.readthedocs.io/en/latest/
#
# from googletrans import Translator
# def translate_to_ukrainian(text):
#     translator = Translator()
#     translation = translator.translate(text, src='en', dest='uk')
#     return translation.text
#
# # Example usage
# english_text = "Hello, how are you?"
# ukrainian_translation = translate_to_ukrainian(english_text)
# print(english_text)
# print(ukrainian_translation)

# ==============   Translate SCRIPT 3  ==============

# ==============   Translate SCRIPT 2  ==============

# https://stackoverflow.com/questions/73881616/attributeerror-when-using-googletrans-module

# from tkinter import*
# from tkinter import ttk
# from googletrans import Translator,LANGUAGES
#
# def change(text="type",src="English",dest="Hindi"):
#     text1=text
#     src1=src
#     dest1=dest
#     trans = Translator()
#     trans1 = trans.translate(text,src=src1,dest=dest1)
#     return trans1.text
#
# def data():
#     s =comb_sor.get()
#     d =comb_dest.get()
#     msg = Sor_txt.get(1.0,END)
#     textget = change(text=msg,src=s,dest=d)
#     dest_txt.delete(1.0,END)
#     dest_txt.insert(END,textget)
#
#
# root = Tk()
# root.title("Translater")
# root.geometry("500x800")
# root.config(bg="#FFE1F3")
#
# lab_txt=Label(root,text="Translator", font=("Time New Roman",40,"bold"),fg="#478C5C")
# lab_txt.place(x=100,y=40,height=50,width=300)
#
# frame=Frame(root).pack(side=BOTTOM)
#
# lab_txt=Label(root,text="Source Text", font=("Time New Roman",20,"bold"),fg="#FFFF8A",bg="#FDA172")
# lab_txt.place(x=100,y=100,height=20,width=300)
#
#
# Sor_txt =Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
# Sor_txt.place(x=10,y=130,height=150,width=480)
#
# list_text = list(LANGUAGES.values())
# comb_sor = ttk.Combobox(frame,value=list_text)
# comb_sor.place(x=10,y=300,height=20,width=100)
# comb_sor.set("English")
#
# button_change = Button(frame,text="Translate",relief=RAISED,command=data)
# button_change.place(x=120,y=300,height=40,width=100)
#
# comb_dest = ttk.Combobox(frame,value=list_text)
# comb_dest.place(x=230,y=300,height=20,width=100)
# comb_dest.set("English")
#
# lab_txt=Label(root,text="Dest Text", font=("Time New Roman",20,"bold"),fg="#2E2EFF")
# lab_txt.place(x=100,y=360,height=50,width=300)
#
# dest_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
# dest_txt.place(x=10,y=400,height=150,width=480)
#
# root.mainloop()

# ==============   Translate SCRIPT 2  ==============

# ==============   Translate SCRIPT 1  ==============

# # https://pypi.org/project/translate/
# from translate import Translator
#
# def translate_word(word, source_lang, target_lang):
#     translator= Translator(to_lang=target_lang, from_lang=source_lang)
#     translation = translator.translate(word)
#     return translation
#
# source_word = "Hello, how are you?"
# source_lang = "en"  # English
# target_lang = "uk"  # French
#
# translated_word = translate_word(source_word, source_lang, target_lang)
# print(f"Translated word: {translated_word}")

# ==============   Translate SCRIPT 1  ==============

# ==============   GLUE SCRIPT 1  ==============

# from pydub import AudioSegment
#
# infiles = ["Radio.mp3", "Jacket.mp3"]
# outfile = "sounds.mp3"
#
# # Load the audio files
# audio1 = AudioSegment.from_file(infiles[0], format="mp3")
# audio2 = AudioSegment.from_file(infiles[1], format="mp3")
#
# # Combine the audio files
# combined = audio1 + audio2
#
# # Export the combined audio
# combined.export(outfile, format="mp3")

# ==============   GLUE SCRIPT 1 ==============

# ==============   GLUE SCRIPT 3 ==============

# Add silence to the end of an MP3 python
# ffmpeg -i input.mp3 -af "silenceremove=start_periods=1:start_duration=1:start_threshold=-60dB:detection=peak,aformat=dblp,areverse,silenceremove=start_periods=1:start_duration=1:start_threshold=-60dB:detection=peak,aformat=dblp,areverse" output.flac

# For work library pydub need add FFmpeg
# WINDOWS
# Envirement variable
# FFMpeg C:\ffmpeg\bin\ffmpeg.exe;C:\ffmpeg\bin\ffplay.exe;C:\ffmpeg\bin\ffprobe.exe
# "Run as administrator." console
# setx /m PATH "C:\ffmpeg\bin;%PATH%"

# FUNCOTION example send paramerer
# from pydub import AudioSegment
# def add_silence(input_file, output_file):
#     audio = AudioSegment.from_file(input_file, format="mp3")
#     silence = AudioSegment.silent(duration=5000)
#     output_audio = silence + audio
#     output_audio.export(output_file, format="mp3")
# add_silence("Jacket.mp3", "output.mp3")

# ==============   GLUE SCRIPT 3 ==============

# # Open the file
# with open('list.txt', 'r') as file:
#     # Read the lines
#     lines = file.readlines()
#
#     # print(lines[1].strip())
#     # print(lines[3].strip())
#
#     # Print each line
#     for line in lines:
#         print(line.strip())  # strip() removes any leading or trailing whitespace





# import requests
#
# url = "https://files.soundoftext.com/d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3"
# response = requests.get(url)
#
# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Get the Content-Disposition header
#     content_disposition = response.headers.get('Content-Disposition')
#
#     # Print the Content-Disposition header
#     #print(f"Content-Disposition: {content_disposition}")
#
#     parameters = content_disposition.split(';')
#     # Iterate through the parameters to find the one containing 'filename='
#     for parameter in parameters:
#         if 'filename=' in parameter:
#             filename = parameter.split('=')[-1].strip()
#             break
#     print(filename)
# else:
#     print(f"Error: Unable to download the file. Status code: {response.status_code}")




# import requests
#
# json_response = {
#     "status": "Done",
#     "location": "https://files.soundoftext.com/d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3"
#     }
#
# url = json_response['location']
# response = requests.get(url)
#
# if response.status_code == 200:
#     mp3_content = response.content
#     file_path = 'output.mp3'
#     with open(file_path, 'wb') as file:
#         file.write(mp3_content)
#     print(f"MP3 file downloaded successfully to {file_path}")
# else:
#     print(f"Failed to download the MP3. Status code: {response.status_code}")

# import requests
# import uuid
# import json
#
#
# print('Download Starting...')
# url = 'https://files.soundoftext.com/d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3'
# r = requests.get(url)
#
# with open(f'dwld/{filename}', 'wb') as output_file:
#     output_file.write(r.content)
#
# print('Download Completed!!!')



# import requests
# import uuid
# print('Download Starting...')
# url = 'https://files.soundoftext.com/d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3'
# r = requests.get(url)
# filename = str(uuid.uuid4())
# filename = url.split('/')[-1]  # this will take only -1 splitted part of the url
#
# with open(f'dwld/{filename}', 'wb') as output_file:
#     output_file.write(r.content)
# print('Download Completed!!!')

# import requests
# url = 'https://files.soundoftext.com/d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3'
# fileName = 'dwld\d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3'
# req = requests.get(url)
# file = open(fileName, 'wb')
# for chunk in req.iter_content(100000):
#     file.write(chunk)
# file.close()



# import requests
# print('Download Starting...')
# url = 'https://www.python.org/static/img/python-logo@2x.png'
# req = requests.get(url)
# with open('dwld/python-logo@2x.png', 'wb') as f:
#     f.write(req.content)
# print("Download Completed!!!")
#
# import requests
# url = 'https://www.facebook.com/favicon.ico'
# r = requests.get(url, allow_redirects=True)
# open('dwld/facebook.ico', 'wb').write(r.content)