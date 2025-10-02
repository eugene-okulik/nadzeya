while True:
    user_input = input('Пожалуйста, введите цифру: ')
    if int(user_input) == 1:
        break
    else:
        print('Вы не угадали! Попробуйте еще раз!')
        continue
print('Вы угадали! Поздравляем!')
