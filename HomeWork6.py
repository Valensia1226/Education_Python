import random

def Task1(N):
    print(N + int(str(N) + str(N)) + int(str(N) + str(N) + str(N)))

def Task2():
    flag = False
    array = [random.randint(1, 10) for _ in range(15)]
    print(array)
    number = input('Введите трехзначное число: ')
    # for i in range(len(number)):
    #     number[i] = int(number[i])
    for i in range(len(array)):
        if number[0] == str(array[i]) and number[1] == str(array[i + 1]) and number[2] == str(array[i + 2]): 
            print('да')
            flag = True
    if flag == False: print('нет')
       
def SimpleNumberTest(N):       
    i = 2
    while i < N:
        if N % i == 0: 
            return False
        i += 1
    return True
        
def Task3():
    znam = [1, 2]
    for i in range(3, 12):
        if SimpleNumberTest(i) == True: znam.append(i)
    print(znam)
    for i in range(len(znam)):
        for j in range(1, len(znam)):
            if znam[i] // znam[j] < 1: print(f'{znam[i]} / {znam[j]}')  