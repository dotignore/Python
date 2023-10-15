import requests
import json
# import sys
# import uuid

r = requests.get(
    "https://api.soundoftext.com/sounds/d622f420-0ad9-11ee-a44a-8501b7b1aefa",
    headers={"Content-Type": "application/json"},
)

print(r.text) # displays the result body.