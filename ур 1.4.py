#Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = input('Введите число: ')
num_max = 0
i = 0
while i < len(number):
    if num_max < int(number[i]):
        num_max = int(number[i])
    i += 1
print(num_max)
