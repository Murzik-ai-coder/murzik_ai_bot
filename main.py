from telebot import *
from groq import Groq

import json

with open('config.json') as f:
    d = json.load(f)
    tg_token = d["tg_token"]
    api_key = d["api_key"]

bot = telebot.TeleBot(tg_token)
client = Groq(
    api_key=api_key,
)

@bot.message_handler(commands=['start'])
def start(message):

    bot.send_message(message.chat.id, 'Привет')

@bot.message_handler()
def AI(message):
    try:
        question = message.text.strip()
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question,
                }

            ],
            model="gemma2-9b-it",
            temperature = 1,
            stream=False,
        )
        bot.send_message(message.chat.id,chat_completion.choices[0].message.content)
    except Exception as err:
        bot.send_message(message.chat.id,"Ошибка : "+ str(err)[:50])

bot.polling(none_stop=True)