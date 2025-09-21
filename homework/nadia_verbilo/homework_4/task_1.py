my_dict = {'tuple': (1, 2, 3, 4, 5),
           'list': [7, 'text', 3.0, True, 'text'],
           'dict': {1: 'value1', 2: 'value2', 3: 'value3', 4: 'value4', 5: 'value5'},
           'set': {'name', False, 10, 'age', 100}}
print(my_dict['tuple'][-1])
my_dict['list'].append(6)
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = (1, 2, 3)
my_dict['dict'].pop(5)
my_dict['set'].add(50)
my_dict['set'].remove(100)

print(my_dict)
