import json

import requests
from abstract.src.getdatasearch import *
from abstract.src.exception import *
import sj.file_json_for_work_programm


class GetDataSearchSJ(GetDataSearch):
    """
    Класс для работы ссылкой, для работы с файлом json
    """
    # Ссылка на необработанный json файл
    data_off_filter = sj.file_json_for_work_programm.file_path_vac_for_filt_sj
    # Ссылка на обработанный json файл
    data_on_filter = sj.file_json_for_work_programm.file_path_print_for_user_sj
    # KEY_ = 'SJ_SECRET_KEY'
    # KEY = os.environ.get(KEY_)
    key = 'v3.r.137748803.7d1255532a6bafc90ce2e3797ecd57ccf308fd2a.fa52ffb58437e94ac7ae4deb39de1ce4fe0f77ec'
    URL = f'https://api.superjob.ru/2.0/{key}/vacancies/'

    def __init__(self,
                 name_vacation: str,
                 choise_salary=None,
                 area_part=None,
                 limit_count_page=20,
                 search_fields_part=None,
                 schedule_part=None,
                 employment_part=None,
                 experience_part=None,
                 page_part=0,
                 no_magic_part=None
                 ):
        # Название вакансии
        self.file_json = None
        self.name_vacation = name_vacation

        """
            "experience":{
            "1":"без опыта",
            "2":"от 1 года",
            "3":"от 3 лет",
            "4":"от 6 лет"
        """
        self.experience_part = experience_part

        """
        "type_of_work":{
            "0":"не имеет значения",
            "6":"полный рабочий день",
            "7":"временная работа / freelance",
            "9":"работа вахтовым методом",
            "10":"неполный рабочий день",
            "12":"сменный график работы",
            "13":"частичная занятость"
        """
        self.schedule_part = schedule_part

        """
        "work_type":{
            "2":"Полная занятость",
            "3":"Частичная занятость",
            "4":"Временная"
        """
        self.employment_part = employment_part

        # Заработная плата
        self.choise_salary = choise_salary

        # Сколько ваканский на странице
        self.limit_count_page = limit_count_page

        # Номер страницы
        self.page_part = page_part

        # Регион
        self.area = area_part

        # Область поиска где написана искомая ваканския
        """
        то искать (в каком текстовом блоке вакансии искать).
        Список возможных значений:
        1 — должность
        2 — название компании
        3 — должностные обязанности
        4 — требования к квалификации
        5 — условия работы
        10 — весь текст вакансии
        """
        self.search_fields = search_fields_part

    def get(self):
        """
        Получение json запроса
        """
        # Получение ссылки для работы
        par = {'keyword': self.name_vacation,  # нвазвание вакансии
               'type_of_work': self.schedule_part,  # тип занятости
               'experience': self.experience_part,  # Опыт работы.
               'work_type': self.employment_part,  # тип работы
               'payment_from': self.choise_salary,  # Зарплата
               'count': self.limit_count_page,  # Сколько вывести вакансий
               'keywords': self.search_fields,  # где искать
               'town': self.area,  # Можно стройкой или id
               'page': self.page_part,  # Номер страницы
               'payment_defined': 'true',  # только с указанием зарплаты
               'archive': 'false',
               }

        response = requests.get(url=self.URL, params=par)
        if response.status_code == 200:
            data_j = response.json()
        else:
            raise GetDataSearchStatusCode
        self.file_json = data_j
        return data_j

    def write_in_data_on_filter(self):
        """
        Используется для записи в файл для пользователя
        """
        for x in range(len(self.file_json['objects'])):
            with open(self.data_off_filter, 'r', encoding='UTF-8') as f:
                content = json.load(f)
                # Название вакансии
                vac_name = content['objects'][x]['profession']
                # Занятость вакансии
                vac_employment = content['objects'][x]['type_of_work']['title']
                # Требуемый опыт вакансии
                vac_experience = content['objects'][x]['experience']['title']
                # Зарплата
                vac_salary_from = content['objects'][x]['payment_from']
                if vac_salary_from is None:
                    vac_salary_from = 0
                else:
                    vac_salary_from = vac_salary_from
                # Зарплата
                vac_salary_to = content['objects'][x]['payment_to']
                if vac_salary_to is None:
                    vac_salary_to = 0
                else:
                    vac_salary_to = vac_salary_to
                # Валюта
                vac_currency = content['objects'][x]['currency']
                # Ссылка на вакансию
                vac_url = content['objects'][x]['link']
                # Что требуется при устройстве на вакансию
                vac_snippet = content['objects'][x]['candidat']
                # Название компании работадателя
                vac_work_app_name = content['objects'][x]['client'].get('title', 'null')
                # Адрес вакансии
                vac_address = content['objects'][x].get('address')

                searching_data = {'items': [{
                    'Название ваканскии': vac_name,
                    'Тип занятости': vac_employment,
                    'Опыт работы': vac_experience,
                    'Зарплата от': vac_salary_from,
                    'Зарплата до': vac_salary_to,
                    'Валюта': vac_currency,
                    'API': 'SuperJob',
                    'url': vac_url,
                    'Требования': vac_snippet,
                    'Название компании': vac_work_app_name,
                    'Адрес': vac_address
                }]}
                searching_data_app = {'items': {
                    'Название ваканскии': vac_name,
                    'Тип занятости': vac_employment,
                    'Опыт работы': vac_experience,
                    'Зарплата от': vac_salary_from,
                    'Зарплата до': vac_salary_to,
                    'Валюта': vac_currency,
                    'API': 'SuperJob',
                    'url': vac_url,
                    'Требования': vac_snippet,
                    'Название компании': vac_work_app_name,
                    'Адрес': vac_address
                }}

            with open(self.data_on_filter, 'r+') as f_1:
                try:
                    contic = json.load(f_1)
                    with open(self.data_on_filter, 'r+') as file:
                        file_data = json.load(file)
                        file_data["items"].append(searching_data_app['items'])
                        file.seek(0)
                        json.dump(file_data, file, indent=2, ensure_ascii=False)
                except:
                    with open(self.data_on_filter, "w") as file:
                        # Записываем данные в файл JSON
                        json.dump(searching_data, file, indent=2, ensure_ascii=False)

    def save_in_file_json(self):
        """
        Сохраняет результат поиска в json файл "vacation_for_filter_sj.json"
        """

        with open(self.data_off_filter, "w") as file:
            # Записываем данные в файл JSON
            json.dump(self.file_json, file, indent=2, ensure_ascii=False)

    def clear_file_json(self):
        """
        Очищает файл json полученный путем фильтрации
        """
        open(self.data_on_filter, "w").close()
