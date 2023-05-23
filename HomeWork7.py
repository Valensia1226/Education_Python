def Task1():
    def likeMapFunc(func, array):
        return (el for el in array if func(el))

    numbers = [8, 8, 2, 2, 4]
    print(numbers)
    
    numbers = list(map(lambda x: x + 5, numbers))
    print(numbers)
    
    numbers = list(likeMapFunc(lambda x: x + 5, numbers))
    print(numbers)

def Task2():
    def repeatCol(N): 
        def repeat(func):   
            def decorator(*args): 
                for i in range(N):
                    func(*args)
            return decorator
        return repeatCol

    @repeatCol(5)
    def message():
        print('Hello')

    @repeat(5)
    def sum(a, b):
        print(a + b)

    message()
    sum(3, 5)