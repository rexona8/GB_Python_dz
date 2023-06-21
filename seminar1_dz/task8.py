# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить
# k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

width = int(input("Введите ширину шоколадки: "))
height = int(input("Введите высоту шоколадки: "))
tiles = int(input("Введите желаемое колличество плиток шоколада: "))

if (tiles % width == 0 or tiles % height == 0) and tiles < width + height:
    print(f"{width} {height} {tiles} -> yes")
else:
    print(f"{width} {height} {tiles} -> no")