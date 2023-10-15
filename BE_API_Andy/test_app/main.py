import sys
import requests
import json
import uuid


def get_mp3_by_word_and_language(word: str, language: str):

    url = "https://api.soundoftext.com/sounds"

    data = {
       "engine": "Google",
       "data": {
            "text": word,
            "voice": language,
       }
    }

    response = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

    if response.status_code != 200:
        raise Exception("Something went wrong")
    
    data = json.loads(response.content)

    if not data["success"]:
        raise Exception("API did not generate mp3")
    
    id = data["id"]

    get_url = f"https://api.soundoftext.com/sounds/{id}"
    
    get_response = requests.get(get_url)

    if get_response.status_code != 200:
        raise Exception("Something went wrong")
    
    mp3_file_data = json.loads(get_response.content)

    if mp3_file_data["status"] != "Done":
        raise Exception("File is not done")

    location = mp3_file_data["location"]

    mp3_file_response = requests.get(location, allow_redirects=True)

    file_name = f"{word}.mp3"
    file_path = f"temp/{file_name}"
    open(file_path, 'wb').write(mp3_file_response.content)

    return file_path


if __name__=="__main__":

    with open("dictionary.txt") as f:
        lines = f.read().splitlines()

        for word in lines:
            get_mp3_by_word_and_language(word=word, language="en-US")

