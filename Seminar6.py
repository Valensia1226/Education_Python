import random
import collections

def Task1():
    numbers = [random.randint(1, 10) for _ in range(5)]
    length = len(numbers)
    print(numbers)
    numbers = set(numbers)
    length2 = len(numbers)
    print(numbers)
    if length == length2: print('уникальны')
    else: print('не уникальны')

def Task2():
    num1 = [random.randint(1, 9) for _ in range(5)]
    num2 = [random.randint(1, 9) for _ in range(5)]
    print(num1)
    print(num2)
    if collections.Counter(num1) == collections.Counter(num2):
        print('Cостоят из одних цифр')
    else: print('Не состоят из одних цифр')

def Task3_1():
    primer = input('Введите арифметическое выражение: ')
    primer = primer.replace(" ", "")
    for el in primer:
        if el == '+':
            pr = primer.split('+')
            rez = int(pr[0]) + int(pr[1])
        elif el == '-':
            pr = primer.split('-')
            rez = int(pr[0]) - int(pr[1])
        elif el == '*':
            pr = primer.split('*')
            rez = int(pr[0]) * int(pr[1])
        elif el == '/':
            pr = primer.split('/')
            rez = int(pr[0]) // int(pr[1])
    print(rez)

def Task3_2():
    primer = input('Введите арифметическое выражение: ')
    primer = primer.replace(" ", "")
    mult = primer.find('*')
    if mult != '-1':
        rez = int(primer[mult - 1]) * int(primer[mult + 1])
    primer = primer.replace(primer[mult - 1: mult + 2], str(rez))
    for el in primer:
        if el == '+':
            pr = primer.split('+')
            rez = int(pr[0]) + int(pr[1])
        elif el == '-':
            pr = primer.split('-')
            rez = int(pr[0]) - int(pr[1])
        elif el == '/':
            pr = primer.split('/')
            rez = int(pr[0]) // int(pr[1])
    print(rez)

def Task3_3():
    primer = input('Введите арифметическое выражение: ')
    rez = eval(primer)
    print(f'{primer} = {rez}')

def Task4():
    N = 1000
    price = [100, 50, 5]
    bulls_count = N // price[0]
    cow_count = N // price[1]
    bull_count = N // price[2]
 #три цикла и условие в конце, где количество быков умноженное на их стоимость + коров + телят = 1000
    print(f'bulls_count = {bulls_count}, cow_count = {cow_count}, bull_count = {bull_count}')
Task4()