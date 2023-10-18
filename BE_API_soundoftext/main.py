import requests
import json
# import sys
# import uuid

# Open the file
with open('list.txt', 'r') as file:
    # Read the lines
    lines = file.readlines()

    # print(lines[1].strip())
    # print(lines[3].strip())

    # Print each line
    for line in lines:
        word = line.strip()
        print(line.strip())  # strip() removes any leading or trailing whitespace

        lang = 'en-US'

# ==== POST Request ====
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

# ==== GET Request ====

        get = requests.get(
            "https://api.soundoftext.com/sounds/" + response_id + "",
            headers={"Content-Type": "application/json"},
        )
        # print(get.text) # displays the result body.
        # {"status":"Done","location":"https://files.soundoftext.com/d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3"}

        response_json = get.json()
        url = response_json["location"]
        print(url)
        # https://files.soundoftext.com/d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3

# ==== get name.mp3 ====

        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the Content-Disposition header
            content_disposition = response.headers.get('Content-Disposition')

            # Print the Content-Disposition header
            print(f"Content-Disposition: {content_disposition}")
            # Content-Disposition: attachment; filename*=UTF-8''Tenement.mp3; filename=Tenement.mp3

            parameters = content_disposition.split(';')
            # Iterate through the parameters to find the one containing 'filename='
            for parameter in parameters:
                if 'filename=' in parameter:
                    filename = parameter.split('=')[-1].strip()
                    break
            print(filename)
            # Tenement.mp3
        else:
            print(f"Error: Unable to download the file. Status code: {response.status_code}")

# ==== save name.mp3 ====

        print(f'{response_id}.mp3 ==> {filename}')
        # d622f420-0ad9-11ee-a44a-8501b7b1aefa.mp3 ==> Tenement.mp3

        print('\nDownload Starting...')
        r = requests.get(url)
        with open(f'dwld/{filename}', 'wb') as output_file:
            output_file.write(r.content)
        print(f'File name {filename}')
        print('Download Completed!!!')

# ==== add silence to start file ====

        # For work library pydub need add FFmpeg
        # WINDOWS
        # Envirement variable
        # FFMpeg C:\ffmpeg\bin\ffmpeg.exe;C:\ffmpeg\bin\ffplay.exe;C:\ffmpeg\bin\ffprobe.exe
        # "Run as administrator." console
        # setx /m PATH "C:\ffmpeg\bin;%PATH%"

        # FUNCOTION example send paramerer
        from pydub import AudioSegment
        def add_silence(input_file, output_file):
            audio = AudioSegment.from_file(input_file, format="mp3")
            silence = AudioSegment.silent(duration=5000)
            output_audio = silence + audio
            output_audio.export(output_file, format="mp3")

        add_silence(f'dwld/{filename}', f'dwld/{filename}')
