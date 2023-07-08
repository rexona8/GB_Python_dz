# Задача 32: Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. неменьше заданного минимума и не больше
# заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random


len_list = int(input("Введите кол-во элементов списка: "))
lst = [random.randint(0, 1000) for i in range(len_list)]

upper_limit = int(input("Введите верхнюю границу элементов списка: "))
lower_limit = int(input("Введите нижнюю границу элементов списка: "))

lst_range_index = []
for i in range (0, len(lst)):
    if upper_limit > lst[i] > lower_limit:
        lst_range_index.append(i)

print(lst)      
print(lst_range_index)