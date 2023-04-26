# # Задача 32: Определить индексы элементов массива (списка),
# # значения которых принадлежат заданному диапазону (т.е. не
# # меньше заданного минимума и не больше заданного
# # максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random

def find_elements (min_int,max_int,input_list):
    result_list = list()
    for i in range(len(input_list)):
        if min_int  <= input_list[i] <= max_int:
            result_list.append(i)
    return result_list

print(input_list:=[random.randint(1,10) for _ in range(10)])

min_int = int (input(('Ввидите минимальный порог: ')))
max_int = int(input('Введите максимальный элемент: '))

print(find_elements(min_int,max_int,input_list))