# Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def print_info(data): # функция вывода на экран
    # temp = read_file - можно использовать на случай, если понадобится изменить данные извне
    print("", *data)


def read_file(): # функция считывания с файла информации
    with open("telephone_directory.txt", "r", encoding = "utf - 8") as file:
        temp = file.readlines()
    return temp


def write_file(data): # функция записив в файл информации
    with open("telephone_directory.txt", "a", encoding="utf-8") as f:
        fio = input("Введите ФИО: ")
        phone_number = input("Введите номер телефона: ")
        f.write(f"{fio} - {phone_number}\n")
        print(f"Добавлена запись : {fio} - {phone_number}")


def search(book: str, search_str: str):
    book = book.split("\n")
    result = []
    for line in book:
        if search_str in line:
            result.append(line)
    return result


def find_data(data):
    search_line = input("Введите ФИО или номер для поиска: ")
    with open("telephone_directory.txt", "r", encoding='utf-8') as f:
        tel_book = f.read()
        find_list = search(tel_book, search_line)
        return find_list


def find_one_line(data):
    find_list = find_data(data)
    if len(find_list) > 1:
        print("Найдены записи:")
        for index in range(len(find_list)):
            print(f"{index + 1} - {find_list[index]}")
        index_element = int(input("Введите номер записи для редактирования: ")) - 1
        print(f"Для редактирования выбрана запись - {find_list[index_element]}")
        return find_list[index_element]
    elif len(find_list) == 1:
        print(f"Для редактирования выбрана запись - {find_list[0]}")
        return find_list[0]
    else:
        print("Поиск не дал результатов.")
        return ""


def edit_data(data):
    with open("telephone_directory.txt", "r", encoding='utf-8') as f:
        tel_book = f.read()
    tel_book_lines = tel_book.split("\n")
    target_line = find_one_line(data)
    while len(target_line) == 0:
        target_line = find_one_line(data)
    edited_line = edit_line(target_line)
    tel_book_lines[tel_book_lines.index(target_line)] = edited_line
    print(f"Запись: {target_line}, изменена на {edited_line}")
    with open("telephone_directory.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))


def edit_line(line: str):
    elements = line.split(" - ")
    fio = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    if len(fio) == 0:
        fio = elements[0]
    if len(phone) == 0:
        phone = elements[1]
    return f"{fio} - {phone}"


def remove_data(data):
    with open("telephone_directory.txt", "r", encoding='utf-8') as f:
        tel_book = f.read()
    tel_book_lines = tel_book.split("\n")
    find_list = find_data(data)
    while len(find_list) == 0:
        find_list = find_data(data)
    if len(find_list) > 0:
        print("Найдены записи:")
        for index in range(len(find_list)):
            print(f"{index + 1} - {find_list[index]}")
        index_for_remove = int(
            input("Введите номер строки для удаления, или 0 для удаления всех найденных строк: ")) - 1
        if 0 <= index_for_remove < len(find_list):
            print(f"Удалена запись: {find_list[index_for_remove]}")
            tel_book_lines.pop(tel_book_lines.index(find_list[index_for_remove]))
        elif index_for_remove == -1:
            for index in find_list:
                tel_book_lines.pop(tel_book_lines.index(index))
            print(f"Удалено записей: {len(find_list)}")
        else:
            print("Удалено записей: 0")
    with open("telephone_directory.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))


def menu(): # основная функция меню
    data = read_file()
    while True:
        print("Выберите действие: ")
        print("1 - вывести информацию на экран")
        print("2 - добавить контакт")
        print("3 - поиск контакта")
        print("4 - изменение контакта")
        print("5 - удаление контакта")
        print("0 - выход из программы")
        n = int(input("Что Вы выбираете? "))
        if n == 0:
            break
        elif n == 1:
            print_info(data)
        elif n == 2:
            write_file(data)
        elif n == 3:
            for i in find_data(data):
                print(i)
        elif n == 4:
            edit_data(data)
        elif n == 5:
            remove_data(data)
        else:
            print("Ничего не выбрано")


if __name__ == "__main__": # условие проверки файла, если понадобится отдельный модуль
    menu()