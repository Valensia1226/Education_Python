def Task1():
    def likeMapFunc(func, array):
        return (el for el in array if func(el))

    numbers = [8, 8, 2, 2, 4]
    print(numbers)
    
    numbers = list(map(lambda x: x + 5, numbers))
    print(numbers)
    
    numbers = list(likeMapFunc(lambda x: x + 5, numbers))
    print(numbers)

def Task2():
    def repeatCol(N): 
        def repeat(func):   
            def decorator(*args): 
                for i in range(N):
                    func(*args)
            return decorator
        return repeatCol

    @repeatCol(5)
    def message():
        print('Hello')

    @repeat(5)
    def sum(a, b):
        print(a + b)

    message()
    sum(3, 5)


import telebot
import requests
import time

bot = telebot.TeleBot("5724189873:AAHs8nNm8yqrRZcY1eL_X5tHwwScje3GHVA") 

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=['text'])
def greetings(message):
	text = message.text
	if text == 'котик':
		req = requests.get(f'https://cataas.com/cat?{time.time()}')
		bot.send_photo(message.from_user.id, req.content)
    elif 'привет' in text:
        bot.reply_to(message, f'Привет, {message.from_user.first_name}')

bot.polling()
