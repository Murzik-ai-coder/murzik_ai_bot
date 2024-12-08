from telebot import *
from groq import Groq
import json
import AI
import sound

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

@bot.message_handler()
def chat(message):
    if not (message.chat.id in mode) or mode[message.chat.id] is None:
        bot.send_message(message.chat.id, 'выбери режим /gemini или /sound')
    elif mode[message.chat.id] == "Gemini":
        AI.AI(message,client,bot)
    elif mode[message.chat.id] == "Sound":
        sound.Sound(message,bot)



bot.polling(none_stop=True)