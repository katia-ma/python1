# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Пожалуйста, введите число. Ваше число должно быть целым и больше 0: "))
if number <= 0 or number % 1 != 0:
    number = int(input("Ваше число не подходит. Попробуем снова! Введите целое положительное число: "))

maximum = number % 10
number = number // 10

while number > 0 and number % 10 > maximum:
    maximum = number % 10
    number = number // 10
print("Самая большая цифра:", maximum)
