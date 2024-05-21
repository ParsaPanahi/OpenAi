import telebot
from OpsAi import Ai
import random
from gtts import gTTS
import openai

# Developer Tel @mrkral
# This bot is developed by Parsa Panahi. For more projects, visit my GitHub: https://github.com/ParsaPanahi
# TeleGram Channels @MeshkiTm - @irkral

token = '---' #Token Telegram Bot
openai.api_key = "s7-pbSFOHl5ATIDn1h0cdPCJ" # OpenAi api Key
bot = telebot.TeleBot(token)
	
bot.set_my_commands([

    telebot.types.BotCommand("/start", "🤖 Start the bot"),
    telebot.types.BotCommand("/help", "🆘 How to use the bot"),
    telebot.types.BotCommand("/speak", "🗣 Convert texts to speech"),
    telebot.types.BotCommand("/imagine", "📸 Create a custom image")
    
])

@bot.message_handler(commands=['start']) # start text
def Welcome(message):
	bot.reply_to(message,'Hello! How can I assist you today?')

@bot.message_handler(commands=['help']) # Help Text
def help(message):
	bot.reply_to(message,'''OpenAi is a Telegram bot that uses advanced GPT technology to provide customized responses, create personalized images and convert text to high-quality audio.

/start — Start/restart the bot
/imagine prompt — Create a custom image based on your texts prompt
/speak prompt — Convert your texts prompt to speech audio format

If you have any questions or suggestions, please contact @mrkral''')

@bot.message_handler(commands=['speak'])
def speak(message):
	url = "https://t.me/KralMeme/7"
	text = message.text[7:]
	if text == '':
	       bot.send_audio(message.chat.id,url,caption='Hello! How can I assist you today?', reply_to_message_id=message.message_id)
	       return
	
	brok = bot.reply_to(message,'⏳ Processing...')
	if text.isascii():
		language = 'en'
	else:
		language = 'fa'
	speech = gTTS(text=text, lang=language)
	speech.save("speech.mp3")
	
	with open("speech.mp3", "rb") as audio:
		bot.delete_message(message.chat.id, brok.message_id)
		bot.send_audio(message.chat.id, audio,reply_to_message_id=message.message_id)
#
def generate_image(text_input):
    image = openai.Image.create(
        prompt=text_input,
        n=1,
        size="1024x1024"
    )
    return image.get("data")[0]['url']
    
@bot.message_handler(commands=['imagine'])
def imagine_world(message):
    user_input = message.text[9:]
    if user_input == '':
        list = [
        "Imagine a world where pizza grew on trees. 'I'll have a pepperoni and mushroom, please.",
        "Imagine a world where everyone had a tiny elephant for a pet. They'd be so cute!",
        "Imagine a world where everyone had a superpower, but they were all really lame like the ability to turn invisible but only when nobody's looking.",
        "Imagine a world where you could talk to animals. I bet the squirrels have some juicy gossip.",
        "Imagine a world where cats rule the world and humans are their pets. I, for one, welcome our feline overlords.",
        "Imagine a world where the sky was filled with balloons instead of clouds. I hope they're all tied down!",
        "Imagine a world where everything was in black and white, like an old movie. I hope I look good in shades of gray.",
        "Imagine a world where the ocean was made of lemonade. I hope they have enough sugar!",
        "Imagine a world where every time you sneeze, a random object appears in front of you. Watch out for flying toasters!",
        "Imagine a world where the only music was polka. I don't think I could dance that fast!",
        "Imagine a world where everyone had a tiny elephant for a pet. They'd be so cute!",
        "Imagine a world where everyone wore roller skates instead of shoes. The sidewalks would be chaos!",
        "Imagine a world where gravity was different on different parts of the planet. You'd have to be careful where you landed.",
        "Imagine a world where you could control the weather. 'I feel like snow today.",
        "Imagine a world where you could fly, but you had to do it by flapping your arms like a chicken. I hope you're not afraid of heights!",
        "Imagine a world where plants could talk, and they were all really sassy. 'Water me, dahling, I'm thirsty!",
        "Imagine a world where the sky was filled with balloons instead of clouds. I hope they're all tied down!",
        "Imagine a world where your thoughts appeared as bubbles above your head. I'd be in trouble if anyone could read mine!",
        "Imagine a world where you could fly, but you had to do it by flapping your arms like a chicken. I hope you're not afraid of heights!"]
        bot.reply_to(message, random.choice(list))
        return 
    brok = bot.reply_to(message,'⏳ Processing...')
    image_url = generate_image(user_input)
    bot.delete_message(message.chat.id, brok.message_id)
    bot.send_photo(message.chat.id, image_url,reply_to_message_id=message.message_id)
	
@bot.message_handler(content_types=['text'])
def reply_to_message(message):
    brok = bot.reply_to(message,'⏳ Processing...')
    a = message.text
    s = Ai(query=a)
    bot.delete_message(message.chat.id, brok.message_id)
    bot.reply_to(message, s.chat())

# Developer Tel @mrkral
# This bot is developed by Parsa Panahi. For more projects, visit my GitHub: https://github.com/ParsaPanahi
# TeleGram Channels @MeshkiTm - @irkral

bot.infinity_polling()