from gradio_client import Client

def Sound(message, bot):
    try:
        question_sound = message.text.strip()
        client = Client("OpenSound/EzAudio")
        result = client.predict(
                text=question_sound,
                length=10,
                guidance_scale=5,
                guidance_rescale=0.75,
                ddim_steps=50,
                eta=1,
                random_seed=0,
                randomize_seed=True,
                api_name="/generate_audio"
        )
        with open(result, "rb") as f:
            bot.send_audio(message.chat.id,audio=f)
    except:
        bot.send_message(message.chat.id, "Ошибка")