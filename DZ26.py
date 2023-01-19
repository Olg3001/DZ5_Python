# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B, и возводит
# число А в целую степень B с помощью рекурсии.

print('Programm to get A into degree B')
a = float(input('Input the number '))
b = int(input('Input the number degree '))

def degree(a, b):
    if b == 0:
        return 1
    elif b > 0:
        return a * degree(a, b - 1)
    else:
        return 1 / a * degree(1 / a, abs(b) - 1)

res = degree(a, b)
print(f'{a} in degree {b} = {res}')