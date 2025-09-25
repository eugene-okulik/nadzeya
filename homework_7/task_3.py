text1 = 'результат операции: 42'
text2 = 'результат операции: 514'
text3 = 'результат работы программы: 9'
text4 = 'результат: 2'


def calc(text):
    num = text.index(':') + 2
    num_result = int(text[num::]) + 10
    print(num_result)


calc(text1)
calc(text2)
calc(text3)
calc(text4)
