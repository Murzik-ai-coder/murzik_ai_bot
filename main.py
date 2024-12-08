from telebot import *
from groq import Groq
import json
import AI
import art
import sound

with open('config.json') as f:
    d = json.load(f)
    tg_token = d["tg_token"]
    api_key = d["api_key"]
    yandex_art_token = d["yandex_art_token"]

bot = telebot.TeleBot(tg_token)
client = Groq(
    api_key=api_key,
)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')
    mode[message.chat.id] = None

@bot.message_handler(commands=['home'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')
    mode[message.chat.id] = None

mode = {}

@bot.message_handler(commands=['gemini'])
def AI_start(message):
    mode[message.chat.id] = "Gemini"
    bot.send_message(message.chat.id, 'Теперь я буду отправлять сообщения в модель Gemini')

@bot.message_handler(commands=['sound'])
def sound_start(message):
    mode[message.chat.id] = "Sound"
    bot.send_message(message.chat.id, 'Теперь я буду отправлять сообщения в модель Sound')

@bot.message_handler(commands=['art'])
def art_start(message):
    mode[message.chat.id] = "Art"
    bot.send_message(message.chat.id, 'Теперь я буду отправлять сообщения в модель Yandex Art')

@bot.message_handler()
def chat(message):
    chat_id = message.chat.id
    if not (chat_id in mode) or mode[chat_id] is None:
        bot.send_message(chat_id, 'выбери режим /gemini или /art')
    elif mode[chat_id] == "Gemini":
        AI.AI(message,client,bot)
    elif mode[chat_id] == "Sound":
        sound.Sound(message,bot)
    elif mode[chat_id] == "Art":
        bytes = art.generate(yandex_art_token, message.text.strip(),bot,chat_id)
        bot.send_photo(chat_id, bytes)

bot.polling(none_stop=True)