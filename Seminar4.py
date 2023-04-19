import random
#замена элемента кортежа
def change_element(numbers, index):
    return numbers[:index] + (random.randint(1, 100), ) + numbers[index+1:]

def Task1():
    numbers = tuple(random.randint(1, 100) for _ in range(10))
    index = 2

    print(numbers)
    numbers = change_element(numbers, index)
    print(numbers)
    print(type(numbers))

def calculation(a, b):
    return a + b, a - b, a * b, a / b

def Task2(a, b):
    summ, dif, mult, dele = calculation(a, b)
    print(summ, dif, mult, dele) #можно записать в 4 разных переменных

def Task3():
    numbers = list(random.randint(1, 20) for _ in range(10))
    print(numbers)
    numbersLength = len(numbers)
    numbers = set(numbers)
    print(numbers)
    numbersLen = len(numbers)
    dif = numbersLength - numbersLen
    print(dif)

def Task4():
    smart = {'Илья', 'Георгий', 'Лев', 'Демьян', 'Антон', 'Владислав', 'Боря', 'Стас', 'Марк', 'Влад'}
    beautiful = {'Илья', 'Федор', 'Семен', 'Олег', 'Лев', 'Антон', 'Артем', 'Боря', 'Стас', 'Марк', 'Ян'}
    strong = {'Федор', 'Георгий', 'Олег', 'Демьян', 'Артем', 'Елисей', 'Боря', 'Стас', 'Влад'}
    print(smart & beautiful & strong) #побитовое И, and работает только с true и false, с множествами нужны &
    #или
    print(smart.intersection(beautiful).intersection(strong))

Task4()