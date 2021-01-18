# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что
# создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle


def my_count(num, end_num):
    for el in count(num):
        if el > end_num:
            break
        else:
            print(el)


my_count(num=int(input("Start the list with ")), end_num=int(input("End the list with ")))


def my_cycle(my_list, repetitions):
    i = 0
    for el in cycle(my_list):
        if i > repetitions:
            break
        print(el)
        i += 1


my_list = [17, 26]
my_cycle(my_list, repetitions=int(input("Введите число повторений.")))