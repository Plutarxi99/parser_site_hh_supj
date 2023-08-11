import json
import os
import pathlib

import requests


class GetObjectJsonHH:

    def __init__(self):
        self.url = f'https://api.hh.ru/'
        self.hh_vacancy = None
        self.hh_region = None

    def get_object(self, url):
        response = requests.get(url)
        data_j = response.json()
        return data_j

    def get_vacancy(self, text_vacancy: str):
        url = self.url
        url_vac = f'{url}vacancies?name={text_vacancy}'
        obj_vac = self.get_object(url_vac)
        return obj_vac['items'][1]['name']

    def get_region(self, region: int):
        url = self.url
        url_vac = f'{url}vacancies?area={region}'
        obj_vac = self.get_object(url_vac)
        return obj_vac['items']



if __name__ == '__main__':
    # # vakancy = 'электрик'
    # # id_region = 1
    # # URL = f'https://api.hh.ru/vacancies?text={vakancy}&area={id_region}'
    # j = GetObjectJsonHH()
    # print(j.get_vacancy("тепло"))
    # # print(j.get_region(25))
    # # print(j.url.keys())
    # data = (pathlib.PurePath('/parser_site_hh_supj/hh/file_json_for_work_programm')
    #         .joinpath('vacation_for_filter.json'))
    # import os
    #
    # script_dir = os.path.dirname(__file__)
    # file_path = os.path.join(script_dir, '/vacation_for_filter.json')
    # with open(file_path, 'r') as fi:
    #     pass
    # print(data)
    # import hh.file_json_for_work_programm
    # # print(hh.file_json_for_work_programm.file_path_vac_for_filt)
    # # print(hh.file_json_for_work_programm.file_path_print_for_user)
    # data = hh.file_json_for_work_programm.file_path_vac_for_filt
    # with open(data, 'r') as f:
    #     content = json.load(f)
    #     print(type(content))
    import json


    # function to add to JSON
    def write_json(new_data, filename='tbl.json'):
        with open(filename, 'r+', encoding='UTF-8') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["items"].append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent=4)

        # python object to be appended


    y = {
      "id": "83813907",
      "premium": 'false',
      "name": "Разработчик React Junior",
      "department": 'null',
      "has_test": 'false',
      "response_letter_required": 'false',
      "area": {
        "id": "1",
        "name": "Москва",
        "url": "https://api.hh.ru/areas/1"
      },
      "salary": 'null',
      "type": {
        "id": "open",
        "name": "Открытая"
      },
      "address": {
        "city": 'null',
        "street": 'null',
        "building": 'null',
        "lat": 0.0,
        "lng": 0.0,
        "description": 'null',
        "raw": "м. Нагатинская",
        "metro": 'null',
        "metro_stations": '[]',
        "id": "179983"
      },
      "response_url": 'null',
      "sort_point_distance": 'null',
      "published_at": "2023-07-21T14:06:58+0300",
      "created_at": "2023-07-21T14:06:58+0300",
      "archived": 'false',
      "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=83813907",
      "insider_interview": 'null',
      "url": "https://api.hh.ru/vacancies/83813907?host=hh.ru",
      "alternate_url": "https://hh.ru/vacancy/83813907",
      "relations": [],
      "employer": {
        "id": "650939",
        "name": "Интерпроком,ООО",
        "url": "https://api.hh.ru/employers/650939",
        "alternate_url": "https://hh.ru/employer/650939",
        "logo_urls": {
          "90": "https://hhcdn.ru/employer-logo/379996.jpeg",
          "original": "https://hhcdn.ru/employer-logo-original/157882.jpg",
          "240": "https://hhcdn.ru/employer-logo/452853.jpeg"
        },
        "vacancies_url": "https://api.hh.ru/vacancies?employer_id=650939",
        "accredited_it_employer": 'false',
        "trusted": 'true'
      },
      "snippet": {
        "requirement": "Ожидания по опыту: Высшее образование. Опыт программирования на языке JavaScript (Node.js, React) от 1 года. Знание SQL. Опыт использования инструментов...",
        "responsibility": 'null'
      },
      "contacts": 'null',
      "schedule": 'null',
      "working_days": [],
      "working_time_intervals": [],
      "working_time_modes": [],
      "accept_temporary": 'false',
      "professional_roles": [
        {
          "id": "96",
          "name": "Программист, разработчик"
        }
      ],
      "accept_incomplete_resumes": 'false',
      "experience": {
        "id": "between1And3",
        "name": "От 1 года до 3 лет"
      },
      "employment": {
        "id": "full",
        "name": "Полная занятость"
      },
      "adv_response_url": 'null',
      "is_adv_vacancy": 'false'
    }

    write_json(y)