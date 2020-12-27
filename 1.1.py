name = input('Как вас зовут?')
print(f'Привет, {name}.\nС наступающим!')

my_number = 7
user_number = int(input('Введите число от 0 до 5: '))

while user_number > 5 or user_number < 0:
    print('Упс!')
    user_number = int(input('Попробуем еще раз! Введите число от 0 до 5: '))
    continue

a = my_number + user_number
b = my_number * user_number

result = int(input(f'Сумма моего и вашего числа равна {a}, а произведение {b}. Какое число я загадал? '))

if result == my_number:
    print('Точно! Это 7. До новых встреч!')
else:
    print('Не совсем! Это 7. Будьте здоровы!')
