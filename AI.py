from telebot import *

import requests

def AI(message,bot,IAM_TOKEN):

    data = {
      "modelUri": "gpt://b1g68uo7ch9fbmg0rq8e/yandexgpt/rc",
      "completionOptions": {
        "stream": False,
        "temperature": 1

      },
      "messages": [

        {
          "role": "user",
          "text": message.text #"Ламинат подойдет для укладке на кухне или в детской комнате – он не боиться влаги и механических повреждений благодаря защитному слою из облицованных меламиновых пленок толщиной 0,2 мм и обработанным воском замкам."
        }
      ]
    }


    response = requests.post(
        "https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
        headers={
            "Accept": "application/json",
            "Authorization": f"Api-key {IAM_TOKEN}"
        },
        json=data,
    ).json()
    bot.send_message(message.chat.id, response["result"]["alternatives"][0]["message"]["text"])