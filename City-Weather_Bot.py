import requests
import telebot
import json


bot = telebot.TeleBot('6319159382:AAHnNEAgjlyP3P2LnELeK6hOBheXfM4ePWw')
                       
api = 'b5309e500c0126600a828749f74b9508'

@bot.message_handler(commands = ['start'])
def main(message):
    bot.reply_to(message, 'Привет , напиши название города в котором хочешь знать погоду')

@bot.message_handler(content_types= ['text'])
def main(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot.reply_to(message,f'Сейчас погода : {data["main"]["temp"]} градуса')
    else:
        bot.send_message ( message.chat.id ,'Город указан не верно')
    


bot.polling(none_stop = True)

