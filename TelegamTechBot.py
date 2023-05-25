import telebot
import requests
import time
import random

bot = telebot.TeleBot("TOKEN") 
deal = {}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Здравствуйте, напишите ваш вопрос и мы свяжемся с вами в ближайшее время.")

@bot.message_handler(commands=['deal'])
def send_answer(message):
	data = open('deal.txt', 'r', encoding='utf-8')
	b = data.readline().split(":")
	print(b[1])
	answer = input('Введите ответ: ')
	bot.reply_to(message.from_user.id, answer)
	data.close()

@bot.message_handler(content_types=['text'])
def tech(message):
	text = message.text
	data = open('deal.txt', 'a+', encoding='utf-8')
	data.write(f'id {message.from_user.id}: {text}\n')
	data.close()
	bot.send_message(message.from_user.id, f'Запрос принят!')


bot.polling()