# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за
# проезд и получали билет с номером. Счастливым билетом называют такой билет с 
# шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е.
# билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

number = int(input("Введите номер билета: "))

first_number = number // 100000
second_number = (number % 100000) // 10000
third_number = (number % 10000) // 1000
fourth_number = (number % 1000) // 100
fifth_number = (number % 100) // 10
sixth_number = number % 10

left_side = first_number + second_number + third_number
right_side = fourth_number + fifth_number + sixth_number

if 99999 < number < 1000000:
    if left_side == right_side:
        print(F"{number} -> yes")
    else:
        print(F"{number} -> no")
else:
    print("На билете должно быть 6 цифр")