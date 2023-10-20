import requests
from fall_detection.configs.config import *

def send_message_with_image(image_path, caption):
    API_KEY = TELEGRAM_BOT_API
    FALL_DETECTION_GROUP_CODE = TELEGRAM_FD_GROUP_CODE
    url = f"https://api.telegram.org/bot{API_KEY}/sendPhoto"

    with open(image_path, "rb") as file:
        files = {"photo": (image_path, file)}
        payload = {"caption": caption, "chat_id": FALL_DETECTION_GROUP_CODE}

        response = requests.post(url, data=payload, files=files)

        if response.status_code == 200 and response.json().get("ok"):
            return True
        else:
            print("Failed to send message with image. Response content:", response.content)
            return False
