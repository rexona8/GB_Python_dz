# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите число: "))

left_number = number // 100
central_number = (number // 10) % 10
right_number = number % 10

if 99 < number < 1000:
    print(f"Сумма цифр введенного числа {left_number} + {central_number} + {right_number}:")
    print(f"Равна {left_number + central_number + right_number}")
    
else:
    print("Число не трёхзначное")