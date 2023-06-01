import numpy as np

#Задача 1. Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.
def Task1():
    numbers = [56, 37, 48, 45, 46, 43, 41, 45, 47, 48, 57, 63]
    uniq_list, uniq_count = np.unique(numbers, return_counts=True)
    print(uniq_count)
    count = 0
    uniq_count = list(uniq_count)
    for el in uniq_count:
        if el == 1:
            count += 1
    print(f'Количество уникальных элементов = {count}')

#Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки
def Task2():
    num1 = [1, 2, 3, 4, 5]
    num2 = [1, 3, 3, 4, 5]
    num3 = [1, 2, 3, 4, 5]
    num4 = [1, 2, 7, 4, 5]
    num5 = [1, 2, 8, 4, 5]

    numbers = [num1, num2, num3, num4, num5]
    #тут немного непонятно, считаются ли одинаковыми строки, где одинаковые числа стоят в одной и той же последовательности
    #или же, если числа те же, но стоят в другой последовательности - это тоже одинаковые? Я посчитала, что нет
    count = 0
    for i in range(5):
        for j in range(5):
            if (i != j) and (numbers[i] == numbers[j]):
                count += 1 #знаю, что одинаковые строки будут учитываться дважды, но так как нам важно не количество, а их наличие, то оставила алгоритм в таком виде
    if count != 0:
        print('Есть одинаковые строки')
    #полагаю, эта задача решается через метод np.corrcoef(numbers), однако я так и не разобралась, как он работает

#Создайте двумерный массив случайного размера. Найдите индексы максимального и минимального элементов в нём. Выведите элементы главной диагонали матрицы в виде одномерного массива.
def Task3():
    row = np.random.randint(3, 5)
    column = np.random.randint(3, 5)
    numbers = np.random.randint(1, 10, (row, column))
    print(numbers)
    min_index = np.argmin(numbers)
    max_index = np.argmax(numbers)
    print(f'Индекс минимального числа = {min_index}')
    print(f'Индекс максимального числа = {max_index}')
    
    #если индексы нужно вывести в классическом формате (строка, столбец):
    min_column_index = np.argmin(numbers[0])
    min_in_row = np.min(numbers[0]) 
    min_row_index = 0
    for i in range(1, row):
        min_in_i = np.min(numbers[i]) 
        if min_in_i < min_in_row:
            min_column_index = np.argmin(numbers[i])
            min_row_index = i
            min_in_row = min_in_i
    print(f'Минимальное число = {min_in_row}')
    print(f'Индекс минимального числа = {min_row_index}, {min_column_index}')
    
    max_column_index = np.argmax(numbers[0])
    max_in_row = np.max(numbers[0])
    max_row_index = 0
    for i in range(1, row):
        max_in_i = np.max(numbers[i])
        if max_in_i > max_in_row:
            max_column_index = np.argmax(numbers[i])
            max_row_index = i
            max_in_row = max_in_i
    print(f'Максимальное число = {max_in_row}')
    print(f'Индекс максимального числа = {max_row_index}, {max_column_index}')

    #вторая половина задачи возможна только при условии, что массив квадратный, а по условию он случайного размера
    if row == column:
        num = [numbers[0][0]]
        for i in range(1, row):
            for j in range(1, column):
                if i == j:
                    num.append(numbers[i][j])
        print(f'Элементы главной диагонали матрицы: {num}')
