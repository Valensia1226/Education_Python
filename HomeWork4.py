import math

def PrimeDividers(N):
    dividerList = list()
    flag = True
    if N == 1: return 1
    for i in range(2, N//2):
        if N % i == 0:
            flag = True
            for j in range(2, i):
                if i % j == 0: 
                    flag = False
                    break
            if flag == True: dividerList.append(i)
    return dividerList
                
def Task1(N):
    primeDivider = PrimeDividers(N)
    primeFactors = list()
    primeFactors.append(primeDivider[0])
    N = N // primeDivider[0]
    count = 1
    for i in range(len(primeDivider)):
        for j in range(N//2):
            if N % primeDivider[i] == 0: 
                N = N // primeDivider[i]
                primeFactors.append(primeDivider[i])
                count = count + 1
                continue
            else: break
    print(primeFactors)
    print()
    print(f'количество = {count}')

def Task2():
    list1 = ['Сливочное', 'Бурёнка', 'Вафелька', 'Сладкоежка']
    list2 = ['Сливочное', 'Вафелька', 'Сладкоежка']
    length1 = len(list1)
    length2 = len(list2)
    if length1 == length2: print('Все на месте') #в предположении, что бренды на складе и в ассортименте не могут быть совсем разными
    for i in range(length1):
        flag = False
        for j in range(length2):
            if list1[i] == list2[j]: 
                flag = True
                break
        if flag == False: print(list1[i])

def Task3(number):
    accuracy = str(number).split('.')
    print(accuracy)
    length = len(accuracy[1])
    pi = math.pi
    rez = str(pi)
    print(number)
    print(rez[0:length + 2])

Task3(0.1)