def fibonacci(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1


def print_fibonacci(n):
    my_list = list(fibonacci(n))
    print(my_list[-1])


print_fibonacci(5)
print_fibonacci(200)
print_fibonacci(1000)
# print_fibonacci(100000)
