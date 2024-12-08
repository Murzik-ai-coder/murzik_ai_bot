from telebot import *
from groq import Groq


def AI(message,client,bot):
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

