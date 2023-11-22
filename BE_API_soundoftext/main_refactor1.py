import requests
import json
from googletrans import Translator
from association_langs import get_output_language
from json_data import json_data
from pydub import AudioSegment

def translator(lang_in_associated, lang_out_associated, lines_in):

    def translate_to(text):
        translator = Translator()
        translation = translator.translate(text, src=lang_in_associated, dest=lang_out_associated)
        return translation.text
    lines_out = [translate_to(line) for line in lines_in]

    return lines_out

def api_soundoftext_com(func_lang_in, func_lang_out, func_lines_in, func_lines_out, func_lang_in_associated, func_lang_out_associated, func_silent):

    mapping = dict(zip(func_lines_out, func_lines_in))
    def en_trans(line, func_lang, lang_input):

        post = requests.post(
            "https://api.soundoftext.com/sounds",
            data=json.dumps({
                "engine": "Google",
                "data": {
                    "text": line,
                    "voice": func_lang
                }
            }),
            headers={"Content-Type": "application/json"},
        )

        response_id = post.json()['id']

        get = requests.get(
            "https://api.soundoftext.com/sounds/" + response_id + "",
            headers={"Content-Type": "application/json"},
        )
        response_json = get.json()
        url = response_json["location"]

        if lang_input == 1:         # 1 - input language
            response = requests.get(url)

            if response.status_code == 200:
                content_disposition = response.headers.get('Content-Disposition')
                parameters = content_disposition.split(';')
                for parameter in parameters:
                    if 'filename=' in parameter:
                        filename = parameter.split('=')[-1].strip()
                        filename = filename.replace(".mp3", "_" + func_lang_in_associated + ".mp3")  # func_lang_in_associated  # 1 - input language
                        break
            else:
                print(f"Error: Unable to download the file. Status code: {response.status_code}")

        if lang_input == 2:          # 2 - output language
            output_value = mapping.get(line, "Not Found")
            filename = output_value + "-" + func_lang_out_associated + ".mp3"                                               # func_lang_out_associated  # 2 - output language

        r = requests.get(url)
        with open(f'dwld/{filename}', 'wb') as output_file:
            output_file.write(r.content)

        if lang_input == 1:          # 1 - input language

            def add_silence(input_file, output_file):
                audio = AudioSegment.from_file(input_file, format="mp3")
                silence = AudioSegment.silent(duration=1500)
                output_audio = silence + audio
                output_audio.export(output_file, format="mp3")

            add_silence(f'dwld/{filename}', f'dwld/{filename}')

    for line in lines_in:
        lang_input = 1          # 1 - input language
        en_trans(line, func_lang_in, lang_input)

    for line in lines_out:
        lang_input = 2          # 2 - output language
        en_trans(line, func_lang_out, lang_input)

parsed_data = json.loads(json_data)

lang_in = parsed_data["lang_in"]
lang_out = parsed_data["lang_out"]
silent = parsed_data["silent"]
lines_in = parsed_data["lines_in"]

lang_in_associated = get_output_language(lang_in)               # lang_in_associated en
lang_out_associated = get_output_language(lang_out)             # lang_out_associated uk
lines_out = translator(lang_in_associated, lang_out_associated, lines_in)

api_soundoftext_com(lang_in, lang_out, lines_in, lines_out, lang_in_associated, lang_out_associated, silent)
