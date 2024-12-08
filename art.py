import base64
import time

import requests


def generate(IAM_TOKEN, prompt):
    URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync"
    # Building a request
    data = {
        "modelUri": "art://b1g68uo7ch9fbmg0rq8e/yandex-art/latest",
        "generationOptions": {
          "seed": "1863",
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
            "Authorization": f"Bearer {IAM_TOKEN}"
        },
        json=data,
    )


    id = response.json()["id"]

    for i in range(30):
        print(f"iteration {i}")
        time.sleep(1)

        r = requests.get(f"https://llm.api.cloud.yandex.net:443/operations/{id}",headers={
            "Authorization": f"Bearer {IAM_TOKEN}"
        })
        if r.status_code == 200:
            json = r.json()
            if not json["done"]:
                continue
            im = json["response"]["image"]
            return base64.b64decode(im)
        return []