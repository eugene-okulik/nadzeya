import random


def fibonacci(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1


def my_gen():
    yield random.randrange(1, 5)
    for num in my_gen():
        print(num)

