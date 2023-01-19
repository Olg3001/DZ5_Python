# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. Из всех арифметических операций допускаются 
# только +1 и -1. Также нельзя использовать циклы.

a = int(input('Input the first positive integer '))
b = int(input('Input the second positive integer '))

def sum(a, b):
    if b == 0:
        return a
    else:
        return a + sum(1, b - 1)            

if a < 0 and b < 0:
    print('Incorrect input. The integer should be positive')
else:
    result = sum(a, b)
    print(f'{a} + {b} = {result}')
