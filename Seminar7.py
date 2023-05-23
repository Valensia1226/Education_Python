import time

def stopwatch(func): #функция высшего порядка
    def decorator(): 
        start_time = time.time()
        func()
        print(f'время выполнения {time.time() - start_time}')
    return decorator

@stopwatch
def our_math_str():
    num = '132'
    result = int(num) + int(num*2) + int(num*3)
    print(result)

@stopwatch
def our_math_int():
    num = 132
    result = num + num*1000 + num + num*1000000 + num*1000 + num
    print(result)

our_math_str()
our_math_int()

def our_format(func):
    def decorator(*args):
        for arg in args:
            print(f'{arg} + ', end='')
        print('\b\b= ', end='')

        func(*args)
    return decorator

@our_format
def sum(a, b):
    print(a + b)

@our_format
def sum4(a, b, c, d):
    print(a + b + c + d)

sum(3, 51)
sum4(4, 6, 1, 0)

def greetings(hello):
    def our_greetings(func):
        def decorator():
            name = func()
            print(f'{hello}, {name}')
        return decorator
    return our_greetings

@greetings('Привет')
def get_name():
    return input('Как тебя зовут?\n')

get_name()