import json
from operator import itemgetter
import src_and_file.file_json_for_work_programm
import hh.file_json_for_work_programm
import sj.file_json_for_work_programm
from hh.src.getdatasearchhh import GetDataSearchHH
from sj.src.getdatasearchsj import GetDataSearchSJ
from src_and_file.src.talk_for_user import talk_to_user

data_on_filter_hh = hh.file_json_for_work_programm.file_path_print_for_user_hh
data_on_filter_sj = sj.file_json_for_work_programm.file_path_print_for_user_sj
data_general_user = src_and_file.file_json_for_work_programm.file_path_print_for_user


def filter_salary(reverse: bool):
    """
    Фильтрует з\п
    """
    with open(data_general_user, 'r', encoding='UTF-8') as file:
        content = json.load(file)
        content['items'].sort(key=itemgetter('Зарплата от'), reverse=reverse)
    with open(data_general_user, 'w') as f_1:
        json.dump(content, f_1, indent=2, ensure_ascii=False)


def write_in_general_file():
    """
    Записывает в общий файл вакансии полученные парсингом
    """
    with open(data_on_filter_sj, 'r') as f_sj:
        content_sj = json.load(f_sj)
    with open(data_on_filter_hh, 'r') as f_hh:
        content_hh = json.load(f_hh)

    for x in range(len(content_hh['items'])):
        content_sj['items'].insert(x, content_hh['items'][x])
    with open(data_general_user, 'w') as file:
        json.dump(content_sj, file, indent=2, ensure_ascii=False)


def clear_general_file(data_general):
    """
    Очищает файл json полученный путем фильтрации
    """
    open(data_general, "w").close()


def get_data_json():
    """
    Делает экземпляры класса
    :return: Кортеж из экзмеляров
    """
    dict_ttu = talk_to_user() # Вызов функций для фильтрации полученного результата
    data_json_hh = GetDataSearchHH(name_vacation=dict_ttu[0]['vac'],
                                   area_part=dict_ttu[0]['area'],
                                   schedule_part=dict_ttu[0]['sched'],
                                   employment_part=dict_ttu[0]['employ'],
                                   experience_part=dict_ttu[0]['exp'],
                                   search_fields_part=dict_ttu[0]['field'],
                                   choise_salary=dict_ttu[0]['salary'],
                                   limit_count_page=dict_ttu[0]['per_page'],
                                   page_part=0,
                                   no_magic_part=dict_ttu[0]['magic']
                                   )
    data_json_sj = GetDataSearchSJ(name_vacation=dict_ttu[1]['vac'],
                                   area_part=dict_ttu[1]['area'],
                                   schedule_part=dict_ttu[1]['sched'],
                                   employment_part=dict_ttu[1]['employ'],
                                   experience_part=dict_ttu[1]['exp'],
                                   search_fields_part=dict_ttu[1]['field'],
                                   choise_salary=dict_ttu[1]['salary'],
                                   limit_count_page=dict_ttu[1]['per_page'],
                                   page_part=0,
                                   )
    return data_json_hh, data_json_sj
