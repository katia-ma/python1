# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input("Введите число: ")
a = number + number
b = a + number

new = int(number)+int(a)+int(b)
print(f"Ваше новое число: {new}")
