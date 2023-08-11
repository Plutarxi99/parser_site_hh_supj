import datetime
import json
import pathlib
import hh.file_json_for_work_programm
from getdatasearchhh import GetDataSearchHH


# class MixinPrintForUser:
#     def __init__(self):
#         print('Привет! Если хочешь найти вакансию, которую ты хочешь'
#               'тебе надо задать пару запросов.')
#         self.name_vacation =

class AnalysisOfDataHH:
    """
    Класс для записи в json файл.
    Записывает исходные и отфильтрованные полученные данные в "vacation_for_filter.json"
    Читает и переводит в читательный формат для пользователя
    """

    def __init__(self, file_json):
        self.file_json = file_json

    def write_in_data_on_filter(self):
        data_off_filter = hh.file_json_for_work_programm.file_path_vac_for_filt
        data_on_filter = hh.file_json_for_work_programm.file_path_print_for_user

        for x in range(self.file_json['per_page']):
            with open(data_off_filter, 'r', encoding='UTF-8') as f:
                content = json.load(f)
                # Название вакансии
                vac_name = content['items'][x]['name']
                # Занятость вакансии
                vac_employment = content['items'][x]['employment']['name']
                # Требуемый опыт вакансии
                vac_experience = content['items'][x]['experience']['name']
                # Ссылка на вакансию
                vac_url = content['items'][x]['alternate_url']
                # Что требуется при устройстве на вакансию
                vac_snippet = content['items'][x]['snippet']["requirement"]
                # Название компании работадателя
                vac_work_app_name = content['items'][x]['employer']['name']
                # Адрес вакансии
                vac_address = content['items'][x]['address']

                searching_data = {'items': [{
                    'Название ваканскии': vac_name,
                    'Тип занятости': vac_employment,
                    'Опыт работы': vac_experience,
                    'url': vac_url,
                    'Требования': vac_snippet,
                    'Название компании': vac_work_app_name,
                    'Адрес': vac_address
                }]}
                searching_data_app = {'items': {
                    'Название ваканскии': vac_name,
                    'Тип занятости': vac_employment,
                    'Опыт работы': vac_experience,
                    'url': vac_url,
                    'Требования': vac_snippet,
                    'Название компании': vac_work_app_name,
                    'Адрес': vac_address
                }}

            # # Делаем запись в json формате в файл указанной функции data
            # with open(data_on_filter, "w") as file:
            #     # Записываем данные в файл JSON
            #     json.dump(searching_data, file, indent=2, ensure_ascii=False)
            with open(data_on_filter, 'r+') as f_1:
                try:
                    contic = json.load(f_1)
                    with open(data_on_filter, 'r+') as file:
                        # First we load existing data into a dict.
                        file_data = json.load(file)
                        # Join new_data with file_data inside emp_details
                        file_data["items"].append(searching_data_app['items'])
                        # Sets file's current position at offset.
                        file.seek(0)
                        # convert back to json.
                        json.dump(file_data, file, indent=2, ensure_ascii=False)
                except:
                    with open(data_on_filter, "w") as file:
                        # Записываем данные в файл JSON
                        json.dump(searching_data, file, indent=2, ensure_ascii=False)

    def append_in_data_on_filter(self, other_file_json):
        data_off_filter = hh.file_json_for_work_programm.file_path_vac_for_filt
        data_on_filter = hh.file_json_for_work_programm.file_path_print_for_user

        for x in range(other_file_json['per_page']):
            with open(data_off_filter, 'r', encoding='UTF-8') as f:
                content = json.load(f)

                vac_name = content['items'][x]['name']
                vac_employment = content['items'][x]['employment']['name']
                vac_experience = content['items'][x]['experience']['name']
                vac_url = content['items'][x]['alternate_url']
                vac_snippet = content['items'][x]['snippet']["requirement"]
                vac_work_app_name = content['items'][x]['employer']['name']
                vac_address = content['items'][x]['address']

                searching_data_app = {'items': {
                    'Название ваканскии': vac_name,
                    'Тип занятости': vac_employment,
                    'Опыт работы': vac_experience,
                    'url': vac_url,
                    'Требования': vac_snippet,
                    'Название компании': vac_work_app_name,
                    'Адрес': vac_address
                }}

            with open(data_on_filter, 'r+') as file:
                # First we load existing data into a dict.
                file_data = json.load(file)
                # Join new_data with file_data inside emp_details
                file_data["items"].append(searching_data_app['items'])
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                json.dump(file_data, file, indent=4, ensure_ascii=False)

    def save_in_file_json(self):
        """
        Сохраняет результат поиска в json файл "vacation_for_filter.json"
        :return:
        """
        data = hh.file_json_for_work_programm.file_path_vac_for_filt
        with open(data, "w") as file:
            # Записываем данные в файл JSON
            json.dump(self.file_json, file, indent=2, ensure_ascii=False)
