#HomeWork
def Factorial(n):
    rezult = 0
    if n == 0 or n == 1: rezult = 1
    else: rezult = n*Factorial(n - 1)
    return rezult

def Task1(N):
    for i in range(1, N + 1):
        print(Factorial(i), end=' ')

print()
N = 4
print(f'Факториалы чисел от 1 до {N}:', end=' ')
Task1(N)
print()

def Task2():
    for X in range(0, 2):
        for Y in range(0, 2):
            for Z in range(0, 2):
                print(f'{X} | {Y} | {Z} | {int(not(X and Y) or Z)}')

print()
print(f'Таблица истинности:')
print(f'X | Y | Z | not(X and Y) or Z')
Task2()
print()

def Task3():
    text1 = input('Введите первую строку: ')
    text2 = input('Введите вторую строку: ')
    for i in range(len(text1)):
        count = 0
        for j in text2:
            if j == text1[i]: count += 1
        print(f'{text1[i]} -> {count}')

#or
# def Task3():
#     text1 = input('Введите первую строку: ')
#     text2 = input('Введите вторую строку: ')
#     for i in range(len(text1)):
#         print(f'{text1[i]} -> {text2.count(text1[i])}')

print(f'Количество вхождений символов первой строки во второй:')
Task3()
print()

def Task4(N):
    data = []
    for i in range(-N, N + 1):
        data.append(i)
    print(data)
    for i in range(1, 3):
        temp = data[-1]
        data.insert(0, temp)
        data.pop(len(data) - 1)
    print(data)

N = 3
print(f'Список элементов от {-N} до {N}, сдвинутый на 2 позиции вправо:')
Task4(N)