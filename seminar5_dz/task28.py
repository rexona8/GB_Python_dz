# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def sum(num1, num2):
    if num1 == 0:
        return num2
    return sum(num1 - 1, num2 + 1)

a = int(input("Введите целое, не отрицательное число a: "))
b = int(input("Введите целое, не отрицательное число b: "))

print(sum(a, b))