def finished(func):
    def wrapper(*args):
        func(*args)
        print('finished')
    return wrapper


@finished
def example(text):
    print(text)


example('print me')
