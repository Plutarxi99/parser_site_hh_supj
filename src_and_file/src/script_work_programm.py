from src_and_file.src.func_for_work_json import *


def work_programm():
    # Получаем экземляры класса
    ex = get_data_json()

    # Применяем полиморфизм классов и записываем в файлы полученный данные
    for x in ex:
        x.get()
        x.save_in_file_json()
        x.write_in_data_on_filter()

    # Цикл для использования программы
    while True:
        user = int(input('1: Отфильтровать по з\п от меньшего к большему\n'
                         '2: Отфильтровать по з\п от большего к меньшему\n'
                         '3: Записать в общий файл\n'
                         '4: Очистить полученные файлы\n'
                         '5: Очистить общий файл\n'
                         '6: Вернуться к поиску профессий\n'
                         '0: Закончить программу\n'))
        if user == 1:
            write_in_general_file()
            filter_salary(True)
            continue
        elif user == 2:
            write_in_general_file()
            filter_salary(False)
            continue
        elif user == 3:
            write_in_general_file()
            continue
        elif user == 4:
            ex[0].clear_file_json()
            ex[1].clear_file_json()
        elif user == 5:
            clear_general_file(data_general_user)
        elif user == 6:
            work_programm()
        elif user == 0:
            break
