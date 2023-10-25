import requests
import json

# Open the file
with open('input.txt', 'r') as file:
    # Read the lines
    lines = file.readlines()

# print(lines[1].strip())
# print(lines[3].strip())

# Print each line
for line in lines:
    word = line.strip()
    print(f'{line.strip()}\n')  # strip() removes any leading or trailing whitespace

    lang = 'en-US'

# ==== POST Request ====

    print(f'Start POST Request')

    post = requests.post(
        "https://api.soundoftext.com/sounds",
        data=json.dumps({
            "engine": "Google",
            "data": {
                "text": word,
                "voice": lang
            }
        }),
        headers={"Content-Type": "application/json"},
    )

    print(post.text)  # displays the result body.
    # {"success":true,"id":"d622f420-0ad9-11ee-a44a-8501b7b1aefa"}

    response_id = post.json()['id']
    # print(response_id)

    print(f'Finish POST Request\n')

# ==== POST Request ====

# ==== GET Request ====

    print(f'Start GET Request')
    get = requests.get(
        "https://api.soundoftext.com/sounds/" + response_id + "",
        headers={"Content-Type": "application/json"},
    )
    # print(get.text) # displays the result body.
    # {"status":"Done","location":"https://files.soundoftext.com/d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3"}

    response_json = get.json()
    url = response_json["location"]
    print(f'{url}')
    print(f'Finish GET Request\n')
    # https://files.soundoftext.com/d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3

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
        silence = AudioSegment.silent(duration=1500)
        output_audio = silence + audio
        output_audio.export(output_file, format="mp3")

    add_silence(f'dwld/{filename}', f'dwld/{filename}')
    print('Added silents to file')
    print(f'Finish add silence name_file.mp3 \n')
# ==== add silence to start file ====

print('============================================================')



















# ==== Start translate from EN input.txt to UK output.txt ====
# https://py-googletrans.readthedocs.io/en/latest/

print('Start translate from EN input.txt to UK output.txt')

from googletrans import Translator

def translate_to(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='uk')
    return translation.text

# Read input file
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Translate each line and store in an array
translations = [translate_to(line.strip()) for line in lines]

# print("Translation of first element:")
# print(translations[0])
#
# print("\nTranslation of last element:")
# print(translations[3])

# Print translations
for translation in translations:
    print(translation)

# Write translations to output file
with open('output.txt', 'w', encoding='utf-8') as file:
    for translation in translations:
        file.write(translation + '\n')

print("Translations written to output.txt")

print('Finish translate from EN to UK input.txt => output.txt\n')

# ==== SFinish translate from EN input.txt to UK output.txt ====

print('============================================================')



















# Read input.txt and output.txt
with open('input.txt', 'r', encoding='utf-8') as input_file:
    input_lines = input_file.read().splitlines()

with open('output.txt', 'r', encoding='utf-8') as output_file:
    output_lines = output_file.read().splitlines()

# Create a dictionary to map input to output
mapping = dict(zip(output_lines, input_lines))

# Print each line
for item in output_lines:

    word = item.strip()
    print(f'{item.strip()}\n')  # strip() removes any leading or trailing whitespace
    lang = 'uk-UA'

# ==== POST Request ====

    print(f'Start POST Request')

    post = requests.post(
        "https://api.soundoftext.com/sounds",
        data=json.dumps({
            "engine": "Google",
            "data": {
                "text": word,
                "voice": lang
            }
        }),
        headers={"Content-Type": "application/json"},
    )

    print(post.text)  # displays the result body.
    # {"success":true,"id":"d622f420-0ad9-11ee-a44a-8501b7b1aefa"}

    response_id = post.json()['id']
    # print(response_id)

    print(f'Finish POST Request\n')

# ==== POST Request ====

# ==== GET Request ====

    print(f'Start GET Request')
    get = requests.get(
        "https://api.soundoftext.com/sounds/" + response_id + "",
        headers={"Content-Type": "application/json"},
    )
    # print(get.text) # displays the result body.
    # {"status":"Done","location":"https://files.soundoftext.com/d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3"}

    response_json = get.json()
    url = response_json["location"]
    print(f'{url}')
    print(f'Finish GET Request\n')
    # https://files.soundoftext.com/d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3

# ==== GET Request ====

# ==== get name_file.mp3 ====

    output_value = mapping.get(item, "Not Found")
    print(f'Rename file {item}_ua.mp3 -> {output_value}_ua.mp3')

    filename = output_value + "-aa.mp3"

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



#json_data_input = '{"data": {"engine": "Google", "voice_in": "en-US", "voice_out": "uk-UA", "voice_out_silent": 1500, "lines": ["World", "Jacket", "Radio", "Bag"]}}'

json_data_input = '{' \
                  '        "in_lang": "en-US",' \
                  '        "out_lang": "uk-UA",' \
                  '        "silent": 1500,' \
                  '        "lines": [' \
                  '            "World",' \
                  '            "Jacket",' \
                  '            "Radio",' \
                  '            "Bag"' \
                  '        ]' \
                  '    }' \
                  '}'

# Load the JSON data
parsed_data = json.loads(json_data)

# Access the values
engine = parsed_data["data"]["engine"]
voice_in = parsed_data["data"]["voice_in"]
voice_out = parsed_data["data"]["voice_out"]
voice_out_silent = parsed_data["data"]["voice_out_silent"]
lines = parsed_data["data"]["lines"]

# Print the values
print(f"Engine: {engine}")
print(f"Voice In: {voice_in}")
print(f"Voice Out: {voice_out}")
print(f"Voice Out Silent: {voice_out_silent}")
print(f"Lines: {', '.join(lines)}")


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

