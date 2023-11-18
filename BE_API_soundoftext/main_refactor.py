import requests
import json
from googletrans import Translator
from association_langs import get_output_language
from json_data import json_data
from pydub import AudioSegment

# ============  translate text lang_in => lang_to  ============
def translator(lang_in_associated, lang_out_associated, lines_in):

    print(f'========== Start translate text ==========')
    def translate_to(text):
        translator = Translator()
        translation = translator.translate(text, src=lang_in_associated, dest=lang_out_associated)
        return translation.text

    lines_out = [translate_to(line) for line in lines_in]

    return lines_out
    #print(f'========== Finish translate text ==========')

# ============  translate text lang_in => lang_to  ============

def api_soundoftext_com(func_lang_in, func_lang_out, func_lines_in, func_lines_out, func_lang_in_associated, func_lang_out_associated, func_silent):

    for i in range(2):

        if i == 0:
            lang = func_lang_in
            lines = func_lines_in
            print(f"lang: {lang}")
            print(f"lines: {lines}")

        if i == 1:
            lang = func_lang_out
            lines = func_lines_out
            print(f"lang: {lang}")
            print(f"lines: {lines}")

# Read input.txt and output.txt files
        if i == 1:

            input_lines = func_lines_in
            output_lines = func_lines_out

            mapping = dict(zip(output_lines, input_lines))

            # Print each line
            for item in output_lines:
                line = item.strip()
                print(f'{item.strip()}\n')  # strip() removes any leading or trailing whitespace
                lang = 'uk-UA'

        if i == 0:
            for line in lines:
                print()
        else:

# ==== POST Request Start ====

            print(f'Start POST Request')

            post = requests.post(
                "https://api.soundoftext.com/sounds",
                data=json.dumps({
                    "engine": "Google",
                    "data": {
                        "text": line,
# func_lang_out
                        "voice": lang
                    }
                }),
                headers={"Content-Type": "application/json"},
            )

            print(
                f"{post.text}")  # displays the result body.        # print {"success":true,"id":"d622f420-0ad9-11ee-a44a-8501b7b1aefa"}
            response_id = post.json()['id']
            print(f"{response_id}")  # print e162af40-48a8-11ed-a44a-8501b7b1aefa

            print(f'Finish POST Request\n')

# ==== POST Request finish ====

# ==== GET Request Start ====

            print(f'Start GET Request')
            get = requests.get(
                "https://api.soundoftext.com/sounds/" + response_id + "",
                headers={"Content-Type": "application/json"},
            )
            # print(get.text) # displays the result body.
            # {"status":"Done","location":"https://files.soundoftext.com/d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3"}

            response_json = get.json()
            url = response_json["location"]
            print(f'{url}')  # https://files.soundoftext.com/d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3
            print(f'Finish GET Request\n')

# ==== GET Request ====

            if i == 0:
# ==== get EN name_file.mp3 ====

                print(f'Start get name_file.mp3 from header')
                response = requests.get(url)

                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    print(f"Status code: {response.status_code}")
                    # Get the Content-Disposition header
                    content_disposition = response.headers.get('Content-Disposition')

                    # Print the Content-Disposition header
                    print(f"Header")
                    print(
                        f"Content-Disposition: {content_disposition}")  # Content-Disposition: attachment; filename*=UTF-8''Tenement.mp3; filename=Tenement.mp3

                    parameters = content_disposition.split(';')
                    # Iterate through the parameters to find the one containing 'filename='
                    for parameter in parameters:
                        if 'filename=' in parameter:
                            filename = parameter.split('=')[-1].strip()
# func_lang_out_associated
# func_lang_in_associated
                            filename = filename.replace(".mp3", "_en.mp3")
                            break
                    print(filename)
                    # Tenement.mp3
                else:
                    print(f"Error: Unable to download the file. Status code: {response.status_code}")

                print(f'Finish get name_file.mp3 from header \n')

# ==== get EN name.mp3 Finish ====

# ==== get name_file.mp3 ====
            if i == 1:
                output_value = mapping.get(item, "Not Found")
                print(f'Rename file {item}_ua.mp3 -> {output_value}_ua.mp3')

                filename = output_value + "-ua.mp3"
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

            print(f'Start add silence name_file.mp3')

            if i == 0:
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

# Load the JSON data
parsed_data = json.loads(json_data)

# Parser JSON
lang_in = parsed_data["lang_in"]
lang_out = parsed_data["lang_out"]
silent = parsed_data["silent"]
lines_in = parsed_data["lines_in"]
# ============  json_data.py  ============

# ============  association_langs.py  ============
# Lang assosiace                def translator
lang_in_associated = get_output_language(lang_in)               # lang_in_associated en
lang_out_associated = get_output_language(lang_out)             # lang_out_associated uk
lines_out = translator(lang_in_associated, lang_out_associated, lines_in)

print(f"###############################################")
print(f"lang_in {lang_in}, lines_in {lines_in}, lang {lang_out}, lines_out {lines_out}, silent {silent}")       # lang uk-UA, lines ['Світ', 'Куртка', 'Радіо', 'Мішок'], silent 1500
print(f"###############################################")
api_soundoftext_com(lang_in, lang_out, lines_in, lines_out, lang_in_associated, lang_out_associated, silent)