# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и
# количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def generate_list(first_number, step, size):
    result_list = list()
    for i in range(size):
        result_list.append(first_number+(i)*step)
    return result_list


first_number = int(input('Введите первое число: '))
step = int(input('Введиете шаг: '))
size = int(input('Ввеидте размер списка: '))

print(generate_list(first_number, step, size))
