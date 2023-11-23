import requests
import os
import yaml


config_path='src/fall_detection/configs/config.yaml'
with open(config_path, 'r') as file:
    config = yaml.safe_load(file)

def send_message_with_image(image_path, caption):
    API_KEY = os.getenv("TELEGRAM_BOT_API") or config['telegram_api_settings']['telegram_bot_api']
    FALL_DETECTION_GROUP_CODE = os.getenv("TELEGRAM_FD_GROUP_CODE") or config['telegram_api_settings']['telegram_fd_group_code']
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
