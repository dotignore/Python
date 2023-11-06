import requests
import json
from googletrans import Translator
from association_langs import get_output_language
from json_data import json_data

# ============  translate text lang_in => lang_to  ============
def translator(lang_in_associated, lang_out_associated, lines_in):

    def translate_to(text):
        translator = Translator()
        translation = translator.translate(text, src=lang_in_associated, dest=lang_out_associated)
        return translation.text

    translations = [translate_to(line) for line in lines_in]

    for translation in translations:
        print(translation)

    with open('output.txt', 'w', encoding='utf-8') as file:
        for translation in translations:
            file.write(translation + '\n')

# ============  translate text lang_in => lang_to  ============

# ==== POST Request ====

def api_soundoftext_com(lang_in, lines_in, silent):

#    print(f'test input lang = {lang_in_associated}')
#    print(f'test input words = {lines_in}\n')
#    print(f'for')

    for line in lines_in:
#        print(f'\ttest input words in cycle = {line}')

    # ==== POST Request ====

        print(f'Start POST Request')

        post = requests.post(
            "https://api.soundoftext.com/sounds",
            data=json.dumps({
                "engine": "Google",
                "data": {
                    "text": line,
                    "voice": lang_in
                }
            }),
            headers={"Content-Type": "application/json"},
        )
# {"success":true,          "id":"ecfd7250-4a2d-11ed-a44a-8501b7b1aefa"}
#  {"success":false,        "message":"SoundRequest validation failed: voice: `en` is not a valid enum value for path `voice`."}

        print(f"{post.text}")  # displays the result body.
        # print {"success":true,"id":"d622f420-0ad9-11ee-a44a-8501b7b1aefa"}

        response_id = post.json()['id']
        # print(response_id)
        print(f"{response_id}")
        # print e162af40-48a8-11ed-a44a-8501b7b1aefa

        print(f'Finish POST Request\n')

    # ==== POST Request ====

    # ==== GET Request ====

        print(f'Start GET Request')
        get = requests.get(
            "https://api.soundoftext.com/sounds/" + response_id + "",  headers={"Content-Type": "application/json"},
        )
        # print(get.text) # displays the result body.
        # {"status":"Done","location":"https://files.soundoftext.com/d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3"}

        response_json = get.json()
        url = response_json["location"]
        print(f'{url}')                         # https://files.soundoftext.com/d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3
        print(f'Finish GET Request\n')

    # ==== GET Request ====

    # ==== get name_file.mp3 ====

        print(f'Start get name_file.mp3 from header')
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print(f"Status code: {response.status_code}")
            # Get the Content-Disposition header
            content_disposition = response.headers.get('Content-Disposition')

            # Print the Content-Disposition header
            print(f"Header")
            print(f"Content-Disposition: {content_disposition}")
            # Content-Disposition: attachment; filename*=UTF-8''Tenement.mp3; filename=Tenement.mp3

            parameters = content_disposition.split(';')
            # Iterate through the parameters to find the one containing 'filename='
            for parameter in parameters:
                if 'filename=' in parameter:
                    filename = parameter.split('=')[-1].strip()
                    filename = filename.replace(".mp3", "_en.mp3")
                    break
            print(filename)
            # Tenement.mp3
        else:
            print(f"Error: Unable to download the file. Status code: {response.status_code}")

        print(f'Finish get name_file.mp3 from header \n')

    # ==== get name.mp3 ====

    # ==== save name.mp3 ====

        print('Download name.mp3 Starting...')

        print(f'{response_id}.mp3 ==> {filename}')
        # d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3 ==> Tenement.mp3

        r = requests.get(url)
        with open(f'dwld/{filename}', 'wb') as output_file:
            output_file.write(r.content)
        print(f'File name {filename}')
        print('Download name.mp3 Completed!!!\n')

    # ==== save name.mp3 ====

    # ==== add silence to start file ====

        # For work library pydub need add FFmpeg
        # WINDOWS
        # Envirement variable
        # FFMpeg C:\ffmpeg\bin\ffmpeg.exe;C:\ffmpeg\bin\ffplay.exe;C:\ffmpeg\bin\ffprobe.exe
        # "Run as administrator." console
        # setx /m PATH "C:\ffmpeg\bin;%PATH%"

        # FUNCOTION example send paramerer
        from pydub import AudioSegment

        print(f'Start add silence name_file.mp3')
        def add_silence(input_file, output_file):
            audio = AudioSegment.from_file(input_file, format="mp3")
            silence = AudioSegment.silent(duration=silent)
            output_audio = silence + audio
            output_audio.export(output_file, format="mp3")

        add_silence(f'dwld/{filename}', f'dwld/{filename}')
        print('Added silents to file')
        print(f'Finish add silence name_file.mp3 \n')

    # ==== add silence to start file ====

    print('============================================================')


# ============  json_data.py  ============

# Load the JSON data
parsed_data = json.loads(json_data)

# Parser JSON
lang_in = parsed_data["lang_in"]
lang_out = parsed_data["lang_out"]
silent = parsed_data["silent"]
lines_in = parsed_data["lines_in"]

# # Print the values
# print(f"In Language: {lang_in}")        # In Language: en-US
# print(f"Out Language: {lang_out}")      # Out Language: uk-UA
# print(f"Silent: {silent}")              # Silent: 1500
# print(f"Lines: {', '.join(lines_in)}")  # Lines: World, Jacket, Radio, Bag

# ============  json_data.py  ============

# ============  association_langs.py  ============

# Lang assosiace
lang_in_associated = get_output_language(lang_in)
lang_out_associated = get_output_language(lang_out)

print(f"lang_in: {lang_in} ==> {lang_in_associated}")       # lang_in: en-US ==> en
print(f"lang_out: {lang_out} ==> {lang_out_associated}")     # lang_out: uk-UA ==> uk

# ============  association_langs.py  ============

# ============  translate text lang_in => lang_to  ============
                                                            # lang_in: en-US ==> en
                                                            # lang_out: uk-UA ==> uk
                                                            # lines_in: World, Jacket, Radio, Bag

# translator(lang_in_associated, lang_out_associated, lines_in)

# ============  translate text lang_in => lang_to  ============

api_soundoftext_com(lang_in, lines_in, silent)














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

