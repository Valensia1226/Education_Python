def Fibonacci(n):
    if n == 0: return 0
    elif n == 1 or n == 2: return 1
    else: return Fibonacci(n - 1) + Fibonacci(n - 2)

def Task1(N):
    data = list()
    i = 0
    for i in range(i, N + 1):
        data.append(Fibonacci(i))
    print(data)

def Task2(a):
    fructs = ['апельсин', 'авокадо', 'груша', 'банан']
    choice = list()
    length = len(fructs)
    for i in range(length):
        el = str(fructs[i])
        if el[0] == a: choice.append(el)
    print(f'{a} - > {choice}')

def OpenFile(name = 'test.txt'):
    data = open(name, 'r+', encoding='utf-8')
    text = data.readlines()
    bot = {}
    for i in range(len(text)):
        phrase = text[i].split(':')
        bot[phrase[0]] = phrase[1]
    data.close()
    return bot

def Task3():
    print('Я не очень умный бот, но люблю общаться. Если захочешь завершить диалог, скажи "пока"')
    question = ''
    while question != 'пока':
        bot = OpenFile()
        flag = False
        question = input().lower()
        for key, value in bot.items():
            if question == key: 
                print(value)
                flag = True
            elif question[:len(question) - 1] == key: 
                print(value) #проверка на знак в конце строки (например !)
                flag = True
        if flag == False:
            print('Я не знаю, что с этим делать. Что мне нужно ответить?')
            answer = input().lower()
            if question[-1] == '!': question = question[:len(question) - 1] #чтобы в дальшейшем работала проверка на восклицательный знак в конце строки
            data = open('test.txt', 'a', encoding='utf-8')
            data.write('\n' + question + ':' + answer)
            data.close()
            print('Спасибо! Я это запомню. Скажи что-нибудь еще!')

Task3()