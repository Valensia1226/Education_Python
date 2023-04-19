def Task1(N):
    i = 2
    count = 0
    while N > 1:
        if N % 2 == 0: 
            count += 1
            N = N // 2
            print(2, end=' ')
            continue
        if N % 3 == 0:
            count += 1
            N = N // 3
            print(3, end=' ')
            continue
        if N % 5 == 0:
            count += 1
            N = N // 5
            print(5, end=' ')
            continue
        if N % 7 == 0:
            count += 1
            N = N // 7
            print(7, end=' ')
            continue
        if N % 5 == 0:
            count += 1
            N = N // 5
            print(5, end=' ')
            continue
    print()
    print(f'количество = {count}')

Task1(60)