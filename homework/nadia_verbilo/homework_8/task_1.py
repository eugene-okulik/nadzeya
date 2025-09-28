import random


user_input = input('Your salary is: ')
random_bonus = random.choice([True, False])
print(random_bonus)

if random_bonus:
    print(f'{user_input}, {int(user_input) + int(random.random() * 100)}')
else:
    print(f'{user_input}, {user_input}')
