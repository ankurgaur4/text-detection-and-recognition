import requests
from gtts import gTTS
from pygame import mixer
import cv2
import numpy as np

from matplotlib.patches import Polygon
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
cap = cv2.VideoCapture(1)
img = cap.read()[1]

cv2.imwrite("toUpload.jpg",img)
cap.release()
cv2.destroyAllWindows()
image_path = "toUpload.jpg"
image_data = open(image_path, "rb").read()
image_url = "https://i.pinimg.com/736x/6a/39/53/6a39538be581281fa41ba3e9a3627554--funny-names-funny-signs.jpg"
ocr_url="https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/ocr"
headers  = {'Ocp-Apim-Subscription-Key': 'd6a8e1a722424331b20f771d535f8f91',
            "Content-Type": "application/octet-stream"
            }
params   = {'language': 'unk', 'detectOrientation ': 'true'}
data     = {'url': image_url}
response = requests.post(ocr_url, headers=headers, params=params, data=image_data)
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
