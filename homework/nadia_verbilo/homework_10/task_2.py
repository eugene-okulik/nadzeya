def repeat_me(count=''):
    def decorate(func):
        def wrapper(*args):
            for _ in range(count):
                func(*args)
        return wrapper
    return decorate


@repeat_me(2)
def example(text):
    print(text)


example('print me')
