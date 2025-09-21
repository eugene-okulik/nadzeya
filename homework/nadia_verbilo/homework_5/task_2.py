text1 = 'результат операции: 42'
text2 = 'результат операции: 514'
text3 = 'результат работы программы: 9'
num_index1 = text1.index(':') + 2
num_index2 = text2.index(':') + 2
num_index3 = text3.index(':') + 2
num_result1 = int(text1[num_index1::]) + 10
num_result2 = int(text2[num_index2::]) + 10
num_result3 = int(text3[num_index3::]) + 10
print(num_result1)
print(num_result2)
print(num_result3)
