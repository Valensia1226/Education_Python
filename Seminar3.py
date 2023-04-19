import random
import string

def one():
    numbers = []
    for el in range(11):
        numbers.append(el)
    print(numbers)

def second():
    length = 7
    numbers = [0]*length #0 повторяется 7 раз, список определенной длины
    for index in range(length):
        numbers[index] = random.randint(0, 10)   #обращение по индексу
    print(numbers)


def Task0(length):
    numbers = [random.randint(0, 10) for el in range(length)]
    print(numbers)
    sum = 0
    for i in range(length):
        sum = sum + numbers[i]
    print(f'Сумма {sum}', end=' ')
    if sum % 2 == 0: print('является четной')
    else: print('является нечетной')

def Task1(length):
    numbers = [random.randint(0, 25) for el in range(length)]
    print(numbers)
    sum1 = sum2 = 0
    for i in range(length // 2):
        sum1 += numbers[i]
    for i in range(length // 2, length):
        sum2 += numbers[i]
    if sum1 > sum2: print(f'В первой половине осадков выпало больше: {sum1} > {sum2}')
    else: print(f'Во второй половине осадков выпало больше: {sum1} < {sum2}')
    
def Task2():
    form = dict(Имя = input('Ваше имя: '), Возраст = input('Ваш возраст: '), Хобби = input('Ваше хобби: '), Любимое_животное = input('Ваше любимое животное: '))
    print()
    for key, value in form.items():
        print("{0}: {1}".format(key,value))

def Task3(length):
    letters_and_digits = string.ascii_letters + string.digits
    password = ''.join(random.sample(letters_and_digits, length))
    #случайная выборка нескольких элементов последовательности (последовательность, количество элементов)
    print(password)

def Task4():
    goods = {'ручка': 5, 'карандаш': 3, 'ластик': 4}
    good = ''
    sum = 0
    while good != 'стоп':
        good = input('Введите наименование или "стоп" для завершения: ').lower()
        if good in goods: sum = sum + goods[good]
        else: print('Такого наименования нет')
    print(f'Сумма чека = {sum}')

