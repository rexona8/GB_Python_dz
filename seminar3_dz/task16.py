# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

len_list_N = int(input("Введите длину массива: "))
array_A = []
for i in range(len_list_N):
    num = int(input("Введите значение массива: "))
    array_A.append(num)
print(f"Массив: {array_A}")

find_number_x = int(input("Введите число x, которое нужно найти: "))
count = 0
for i in range(0, len(array_A)):
    if find_number_x == array_A[i]:
        count += 1
print(f"Заданное число x встречается {count} раз/раза")