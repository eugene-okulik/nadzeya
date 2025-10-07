def manage_operations(func):

        def wrapper(first, second):

            if first == second:
                return func(first, second, "+")
            elif first > second:
                return func(second, first, "-")
            elif first < second:
                return func(first, second, "/")
            elif first or second < 0:
                return func(first, second, "*")
        return wrapper


@manage_operations
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    else:
        return first / second


user_input1 = input('Пожалуйста, введите цифру 1: ')
first = float(user_input1)
user_input2 = input('Пожалуйста, введите цифру 2: ')
second = float(user_input2)

print(calc(first, second))
