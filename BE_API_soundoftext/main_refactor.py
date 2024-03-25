import requests
import json
from googletrans import Translator
from association_langs import get_output_language
from json_data import json_data
from pydub import AudioSegment

# https://py-googletrans.readthedocs.io/en/latest/

# ============  translate text lang_in => lang_to  association_langs.py ============
def translator(lang_in_associated, lang_out_associated, lines_in):

    print(f'\n========== Start translate text ==========')
    def translate_to(text):
        translator = Translator()
        translation = translator.translate(text, src=lang_in_associated, dest=lang_out_associated)
        return translation.text

    #print(f"translations_in {lines_in}")
    lines_out = [translate_to(line) for line in lines_in]
    print(f"translations_out {lines_out}")
    print(f'========== Finish translate text ==========\n')

    return lines_out
# ============  translate text lang_in => lang_to  association_langs.py ============

def api_soundoftext_com(func_lang_in, func_lang_out, func_lines_in, func_lines_out, func_lang_in_associated, func_lang_out_associated, func_silent):

    print('============================================================')
    print(f"func_lang_in: {func_lang_in}")                              # en-US
    print(f"func_lang_out: {func_lang_out}")                            # uk-UA
    print(f"func_lang_in_associated: {func_lang_in_associated}")        # en
    print(f"func_lang_out_associated: {func_lang_out_associated}")      # uk
    print(f"func_lines_in: {func_lines_in}")                            # Lines: World, Jacket, Radio, Bag
    print(f"func_lines_out: {func_lines_out}")                          # Lines: Світ, Куртка, Радіо, Мішок
    print(f"func_silent: {func_silent}")                                # func_silent: 1500
    print('============================================================')

    lang = func_lang_in
    lines = func_lines_in
    print(f"lang: {lang}")  # en-US
    print(f"lines: {lines}")  # Lines: World, Jacket, Radio, Bag

    input_lines = func_lines_in
    output_lines = func_lines_out

    mapping = dict(zip(output_lines, input_lines))


    def en_trans(line, func_lang, lang_input):

        print(f'Word ===> {line}')
        #    lang = 'en-US'

# ==================== POST Request ====================
        print(f'\n################## Start POST Request ##################')

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

        print(f'{post.text}')  # displays the result body.
        # {"success":true,"id":"d622f420-0ad9-11ee-a44a-8501b7b1aefa"}

        response_id = post.json()['id']
        # print(response_id)

        print(f'################## Finish POST Request ##################\n')
# ==================== POST Request ====================

# ==================== GET Request ====================
        print(f'################## Start GET Request ##################')
        get = requests.get(
            "https://api.soundoftext.com/sounds/" + response_id + "",
            headers={"Content-Type": "application/json"},
        )
        # print(get.text) # displays the result body.
        # {"status":"Done","location":"https://files.soundoftext.com/d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3"}

        response_json = get.json()
        url = response_json["location"]
        print(f'{url}')
        print(f'################## Finish GET Request ##################\n')
# ==================== GET Request ====================

# ==================== get name_file.mp3 ====================
        if lang_input == 1:         # 1 - input language

            print(f'################## Start get name_file.mp3 from header ##################')
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
                        filename = filename.replace(".mp3", "_" + func_lang_in_associated + ".mp3")  # func_lang_in_associated  # 1 - input language
                        break
                print(filename)
                # Tenement.mp3
            else:
                print(f"Error: Unable to download the file. Status code: {response.status_code}")

            print(f'################## Finish get name_file.mp3 from header ##################\n')
# ==================== get name.mp3 ====================

# ==================== get name_file.mp3 ====================
        if lang_input == 2:          # 2 - output language
            print(f'################## Start get name_file_ua.mp3 ##################')

            output_value = mapping.get(line, "Not Found")
            print(f"Rename file {line}_" + func_lang_out_associated + ".mp3 -> {output_value}_" + func_lang_out_associated + ".mp3")    # func_lang_out_associated  # 2 - output language

            filename = output_value + "-" + func_lang_out_associated + ".mp3"                                               # func_lang_out_associated  # 2 - output language

            print(f'################## Finish get name_file_ua.mp3 ##################\n')
# ==================== get name.mp3 ====================

# ==================== save name.mp3 ====================
        print('################## Download name.mp3 Starting... ##################')

        print(f'{response_id}.mp3 ==> {filename}')
        # d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3 ==> Tenement.mp3

        r = requests.get(url)
        with open(f'dwld/{filename}', 'wb') as output_file:
            output_file.write(r.content)
        print(f'File name {filename}')
        print('################## Download name.mp3 Completed!!! ##################\n')
# ==================== save name.mp3 ====================

# ==================== add silence to start file ====================
        if lang_input == 1:          # 1 - input language

            # For work library pydub need add FFmpeg
            # WINDOWS
            # Envirement variable
            # FFMpeg C:\ffmpeg\bin\ffmpeg.exe;C:\ffmpeg\bin\ffplay.exe;C:\ffmpeg\bin\ffprobe.exe
            # "Run as administrator." console
            # setx /m PATH "C:\ffmpeg\bin;%PATH%"

            # FUNCOTION example send paramerer

            print(f'################## Start add silence name_file.mp3 ##################')

            def add_silence(input_file, output_file):
                audio = AudioSegment.from_file(input_file, format="mp3")
                silence = AudioSegment.silent(duration=1500)
                output_audio = silence + audio
                output_audio.export(output_file, format="mp3")

            add_silence(f'dwld/{filename}', f'dwld/{filename}')
            print('Added silents to file')
            print(f'################## Finish add silence name_file.mp3 ##################\n')
# ==================== add silence to start file ====================

        print('\n============================================================\n \n')


    for line in lines_in:
        lang_input = 1          # 1 - input language
        en_trans(line, func_lang_in, lang_input)

    for line in lines_out:
        lang_input = 2          # 2 - output language
        en_trans(line, func_lang_out, lang_input)


########################################################################################################################
# START   START   START   START   START   START   START   START   START   START   START   START   START   START   START
########################################################################################################################

# ============  json_data.py  ============
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
# ============ json_data.py  ============

# ============ translation word ============
# Lang assosiace   def translator
lang_in_associated = get_output_language(lang_in)               # lang_in_associated en
lang_out_associated = get_output_language(lang_out)             # lang_out_associated uk
lines_out = translator(lang_in_associated, lang_out_associated, lines_in)
print(f"- Lines_out {lines_out}")
# ============ translation word ============

# ============ calling the main function ============
print(f"###############################################")
print(f"lang_in {lang_in}, lines_in {lines_in}, lang {lang_out}, lines_out {lines_out}, lang_in_associated {lang_in_associated}, lang_out_associated {lang_out_associated}, silent {silent}")       # lang uk-UA, lines ['Світ', 'Куртка', 'Радіо', 'Мішок'], silent 1500
print(f"###############################################")
api_soundoftext_com(lang_in, lang_out, lines_in, lines_out, lang_in_associated, lang_out_associated, silent)
# ============ calling the main function ============

########################################################################################################################
# LOG OUTPUT LOG OUTPUT LOG OUTPUT LOG OUTPUT LOG OUTPUT LOG OUTPUT LOG OUTPUT LOG OUTPUT LOG OUTPUT LOG OUTPUT
########################################################################################################################

#             == == == == == == Load the JSON data parser start == == == == == == == == =
#             - Language In: en - US
#             - Language Out: uk - UA
#             - Silent: 1500
#             - Lines_In: World, Jacket, Radio, Bag
#             == == == == == == Load the JSON data parser finish == == == == == == == == =
#
#             == == == == == Start translate text == == == == ==
#             translations_out['Світ', 'Куртка', 'Радіо', 'Мішок']
#             == == == == == Finish translate text == == == == ==#
#             - Lines_out['Світ', 'Куртка', 'Радіо', 'Мішок']
#             ###############################################
#             lang_in
#             en - US, lines_in['World', 'Jacket', 'Radio', 'Bag'], lang
#             uk - UA, lines_out['Світ', 'Куртка', 'Радіо', 'Мішок'], lang_in_associated
#             en, lang_out_associated
#             uk, silent
#             1500
#             ###############################################

#             == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
#             func_lang_in: en - US
#             func_lang_out: uk - UA
#             func_lang_in_associated: en
#             func_lang_out_associated: uk
#             func_lines_in: ['World', 'Jacket', 'Radio', 'Bag']
#             func_lines_out: ['Світ', 'Куртка', 'Радіо', 'Мішок']
#             func_silent: 1500
#             == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
#             lang: en - US
#             lines: ['World', 'Jacket', 'Radio', 'Bag']




#             Word == = > World
#
#             ################## Start POST Request ##################
#             {"success": true, "id": "ecfd7250-4a2d-11ed-a44a-8501b7b1aefa"}
#             ################## Finish POST Request ##################
#
#             ################## Start GET Request ##################
#             https: // files.soundoftext.com / ecfd7250 - 4 a2d - 11 ed - a44a - 8501  b7b1aefa.mp3
#             ################## Finish GET Request ##################
#
#             ################## Start get name_file.mp3 from header ##################
#             Status
#             code: 200
#             Header
#             Content - Disposition: attachment;
#             filename *= UTF - 8
#             ''
#             World.mp3;
#             filename = World.mp3
#             World_en.mp3
#             ################## Finish get name_file.mp3 from header ##################
#
#             ################## Download name.mp3 Starting... ##################
#             ecfd7250 - 4 a2d - 11  ed - a44a - 8501 b7b1aefa.mp3 == > World_en.mp3
#             File name World_en.mp3
#             ################## Download name.mp3 Completed!!! ##################
#
#             ################## Start add silence name_file.mp3 ##################
#             Added silents to file
#             ################## Finish add silence name_file.mp3 ###################
#
#             == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
#
#           .............................................................................
#
#             == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
#
#             Word == = > Світ
#
#             ################## Start POST Request ##################
#             {"success": true, "id": "e1e8de40-7119-11ee-a44a-8501b7b1aefa"}
#             ################## Finish POST Request ##################
#
#             ################## Start GET Request ##################
#             https: // files.soundoftext.com / e1e8de40 - 7119 - 11  ee - a44a - 8501 b7b1aefa.mp3
#             ################## Finish GET Request ##################
#
#             == == == == == Start get name_file_ua.mp3 == == == == ==
#             Rename file  Світ_uk.mp3 -> {output_value} _uk.mp3
#             == == == == == Finish get name_file_ua.mp3 == == == == ==
#
#             ################## Download name.mp3 Starting... ##################
#             e1e8de40 - 7119 - 11  ee - a44a - 8501 b7b1aefa.mp3 == > World - uk.mp3
#             File name World - uk.mp3
#             ################## Download name.mp3 Completed!!! ##################
#
#             == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==

