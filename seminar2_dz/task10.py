# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

coins = int(input("Введите кол-во монеток: "))
head_side = 0
tail_side = 0
reverse_coin = 0
for i in range(coins):
    coins_side = int(input("Введите сторону монетки (1 - орёл или 0 - решка): "))
    if coins_side == 0:
        tail_side = tail_side + 1
    elif coins_side == 1:
        head_side = head_side + 1
    if tail_side > head_side:
        reverse_coin = reverse_coin = tail_side
    if head_side > tail_side:
        reverse_coin = reverse_coin = head_side
print(f"{coins} монет, на стороне орла {head_side}, на стороне решки {tail_side}")
print(f"Нужно перевернуть {reverse_coin} раз/раза")