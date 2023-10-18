
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

# ==============   GLUE SCRIPT 2 ==============
#
# from pydub import AudioSegment
# orig_seg = AudioSegment.from_file('sample.wav')
# silence_seg = AudioSegment.silent(duration=1000) # 1000 for 1 sec, 2000 for 2 secs
#
# # for adding silence at the end of audio
# combined_audio = orig_seg + silence_seg
#
# for adding silence at the start of audio
# combined_audio = silence_seg + orig_seg
#
# ==============   GLUE SCRIPT 2 ==============

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
from pydub import AudioSegment
def add_silence(input_file, output_file):
    audio = AudioSegment.from_file(input_file, format="mp3")
    silence = AudioSegment.silent(duration=5000)
    output_audio = silence + audio
    output_audio.export(output_file, format="mp3")
add_silence("Jacket.mp3", "output.mp3")

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