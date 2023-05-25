import telebot
import requests
import time
import random

bot = telebot.TeleBot("TOKEN") 
counter = []
number = str(random.randint(1, 1000))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=['text'])
def greetings(message):
	#print(message)
	text = message.text.lower()
	if text == 'котик':
		req = requests.get(f'https://cataas.com/cat?{time.time()}')
		bot.send_photo(message.from_user.id, req.content)
	
	elif 'привет' in text:
		bot.reply_to(message, f'Привет, {message.from_user.first_name}')

	elif 'игра' in text:
		bot.send_message(message.from_user.id, 'Я загадал число от 1 до 1000. Попробуй угадать, какое число я загадал?')
	elif text == number:
		counter.append(1)
		bot.send_message(message.from_user.id, f'Поздравляю, правильно! Это было невероятно! Количество попыток = {len(counter)}')
		counter.clear()
	elif text == 'стоп':
		bot.send_message(message.from_user.id, f'Игра окончена. Количество попыток = {len(counter)}')
		counter.clear()
	elif text > number:
		bot.send_message(message.from_user.id, f'Мое число меньше. Попробуй еще или напиши "стоп", чтобы закончить')
		counter.append(1)
		print(len(counter))
	elif text < number:
		bot.send_message(message.from_user.id, f'Мое число больше. Попробуй еще или напиши "стоп", чтобы закончить')
		counter.append(1)
		print(len(counter))

bot.polling()