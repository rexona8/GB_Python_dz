# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

len_list_N = int(input("Введите длину массива: "))
array_A = []
for i in range(len_list_N):
    num = int(input("Введите значение массива: "))
    array_A.append(num)
print(f"Массив: {array_A}")

find_number_x = int(input("Введите число x: "))
near_x = 0
minraz = (abs(find_number_x - array_A[0]))
for i in range(0, len(array_A)):
    if (abs(find_number_x - array_A[i])) <= minraz:
        minraz = (abs(find_number_x-array_A[i]))
        near_x = array_A[i]
print(f"Самое ближайшее к числу х является {near_x}")