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
    mode = None

@bot.message_handler(commands=['home'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')
    mode = None

mode = None

@bot.message_handler(commands=['gemini'])
def AI_start(message):
    global mode
    mode = "Gemini"
    bot.send_message(message.chat.id, 'Теперь я буду отправлять сообщения в модель Gemini')

@bot.message_handler(commands=['sound'])
def sound_start(message):
    global mode
    mode = "Sound"
    bot.send_message(message.chat.id, 'Теперь я буду отправлять сообщения в модель Sound')

@bot.message_handler()
def chat(message):
    if mode == None:
        bot.send_message(message.chat.id, 'выбери режим /gemini или /sound')
    elif mode == "Gemini":
        AI.AI(message,client,bot)
    elif mode == "Sound":
        sound.Sound(message,bot)



bot.polling(none_stop=True)