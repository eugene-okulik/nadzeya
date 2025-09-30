temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

new_list = filter(lambda x: x > 28, temperatures)
temperatures2 = list(new_list)

print(temperatures2)
print(max(temperatures2))
print(min(temperatures2))
average = sum(temperatures2) / len(temperatures2)
print(round(average, 2))
