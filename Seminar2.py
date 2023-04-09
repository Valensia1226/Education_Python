#Task 0
def Task0(N):
    i = 1
    count = 0
    for i in range(i, N + 1):
        if N % i == 0:
            count += 1
            # if i % 2 == 0:
            #     print(f'{i} - четный')
            # else: print(f'{i} - нечетный')
    return count

#Task 1
def Task1():
    for X in range(0, 2):
        for Y in range(0, 2):
            print(f'{X} {Y} = {int(not(X) or Y)}')

#Task 2
def Task2():
    text1 = input('Введите первую строку: ')
    text2 = input('Введите вторую строку: ')
    print(text2.count(text1))

def Task22():
    text1 = input('Введите первую строку: ')
    text2 = input('Введите вторую строку: ')
    count = 0
    for i in range(len(text2)):
        if text2[i:i+len(text1)]==text1: count = count + 1
    print(count)

#Task 3
def Task3():
    N = 5
    number = 0
    for i in range(1, N + 1):
        if i == 1: number = 1
        else: number = -(number * 3)
        print(number, end=' ')

#Task4
def Task4():
    count = 0
    col = 0
    for n in range(10, 10001):
        count = Task0(n)
        if count == 10: 
            col += 1
            print(n)
    print()
    print(col)