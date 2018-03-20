import requests
from gtts import gTTS
from pygame import mixer
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
image_url = "http://www.mindset2millions.com/wp-content/uploads/2015/10/Inspirational-picture-quote-a-negative-mind-will-never-give-you-a-positive-life.jpg"
ocr_url="https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/ocr"
headers  = {'Ocp-Apim-Subscription-Key': 'd6a8e1a722424331b20f771d535f8f91'}
params   = {'language': 'unk', 'detectOrientation ': 'true'}
data     = {'url': image_url}
response = requests.post(ocr_url, headers=headers, params=params, json=data)
response.raise_for_status()

analysis = response.json()

line_infos = [region["lines"] for region in analysis["regions"]]
word_infos = []
for line in line_infos:
    for word_metadata in line:
        for word_info in word_metadata["words"]:
            word_infos.append(word_info)
word_infos
alltext=" "

for i in word_infos:
    alltext+=i["text"].lower()+" "

print(alltext)
tts = gTTS(alltext, lang='en', slow=False)
tts.save("thello.mp3")


mixer.init()
mixer.music.load('thello.mp3')
mixer.music.play()
