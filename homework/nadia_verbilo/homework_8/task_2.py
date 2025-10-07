def fibonacci():
    fib1, fib2 = 0, 1
    while True:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


my_gen = fibonacci()


def fibonacci_num(n):
    for _ in range(n):
        next(my_gen)
    return next(my_gen)


print(fibonacci_num(5))
print(fibonacci_num(200))
print(fibonacci_num(1000))
# print(fibonacci_num(100000))
