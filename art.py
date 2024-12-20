import base64
import random
import time


import requests


def generate(IAM_TOKEN, prompt, bot, chat_id):
    try:
        URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync"
        # Building a request
        data = {
            "modelUri": "art://b1g68uo7ch9fbmg0rq8e/yandex-art/latest",
            "generationOptions": {
              "seed": str(round(random.randint(1001,99999999))),
              "aspectRatio": {
                 "widthRatio": "2",
                 "heightRatio": "1"
               }
            },
            "messages": [
              {
                "weight": "1",
                "text": prompt
              }
            ]
            }


        # Sending the request
        response = requests.post(
            URL,
            headers={
                "Accept": "application/json",
                "Authorization": f"Api-key {IAM_TOKEN}"
            },
            json=data,
        )


        id = response.json()["id"]

        msg = None

        for i in range(30):
            print(f"iteration {i}")
            if not msg is None:
                bot.delete_message(chat_id, msg.id)
            msg = bot.send_message(chat_id, f'Генерирую {i}')
            time.sleep(1)

            r = requests.get(f"https://llm.api.cloud.yandex.net:443/operations/{id}",headers={
                "Authorization": f"Api-key {IAM_TOKEN}"
            })
            if r.status_code == 200:
                json = r.json()
                if not json["done"]:
                    continue
                im = json["response"]["image"]
                if not msg is None:
                    bot.delete_message(chat_id, msg.id)
                return base64.b64decode(im)
            return []
    except:
        bot.send_message(chat_id, "Ошибка")