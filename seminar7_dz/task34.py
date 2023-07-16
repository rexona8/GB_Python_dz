# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:                                                 Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам                Парам пам-пам


vowels_dict = {"А": 1, "Е": 1, "Ё": 1, "И": 1, "О": 1,
                "У": 1, "Ы": 1, "Э": 1, "Ю": 1, "Я": 1,}

# poem = input("Введите стих: ")
poem = "пара-ра-рам рам-пам-папам па-ра-па-дам".upper()
vowels_count = 0
phrase = poem.count(" ") + 1    # + 1, так как мне нужно засчитать последнюю фразу в счетчик

for i in poem:
    for k, v in vowels_dict.items():
        if k in i:
            vowels_count += v
if vowels_count % phrase == 0:
    print("Парам пам-пам")
else:
    print("Пам парам")