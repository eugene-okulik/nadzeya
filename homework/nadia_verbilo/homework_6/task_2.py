numbers = range(1, 101)
for number in numbers:
    if number % 15 == 0:
        print("fuzzbuzz")
    elif number % 3 == 0:
        print("fuzz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
