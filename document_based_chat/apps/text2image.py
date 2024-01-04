import requests

API_URL = "https://api-inference.huggingface.co/models/dataautogpt3/OpenDalleV1.1"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	print(vars(response))
	return response.content
image_bytes = query({
	"inputs": "Sparrow bird",
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))
print(image)
image.save("C:/kunal/work/chat_robot.jpeg")