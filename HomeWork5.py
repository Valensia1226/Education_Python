import random
import collections

def Task1():
    numbers = [random.randint(1, 10) for _ in range(6)]
    print(f'{numbers} -> {list(filter(lambda x: x > 5, numbers))}')

#одна случайная возрастающая последовательность
def Task2():
    numbers = [random.randint(1, 10) for _ in range(random.randint(5, 10))]
    num = list()
    n = random.choice(numbers) #выбираем случайное число из списка
    num.append(n)
    index = numbers.index(n) #определяем индекс этого числа, чтобы начать поиск по списку с него
    print(numbers)
    for i in range(index, len(numbers)):
        if numbers[i] > num[-1]: num.append(numbers[i]) #сравниваем с последним добавленным в новый список
    print(num)

#все возрастающие последовательности
def Task2_2():
    numbers = [random.randint(1, 10) for _ in range(random.randint(5, 10))]
    num = list()
    print(numbers)
    for i in range(len(numbers)):
        num.clear()
        num.append(numbers[i])
        for j in range(i + 1, len(numbers)):
            if numbers[j] > num[-1]: num.append(numbers[j])
        if len(num) > 1: print(num)

def Task3():
    numbers = [random.randint(1, 10) for _ in range(10)]
    count = 0
    repit = collections.Counter(numbers)
    for i in repit.values():
        if i > 1: count += i
    print(f'{numbers} -> количество совпадающих элементов = {count}')
    numbers = set(numbers)
    print(f'Список уникальных элементов: {numbers}')