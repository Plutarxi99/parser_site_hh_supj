import json
import requests
from abstract.src.exception import *
from abstract.src.getdatasearch import *
import hh.file_json_for_work_programm


class GetDataSearchHH(GetDataSearch):
    """
    Класс для работы ссылкой, для работы с файлом json
    """
    # Ссылка на необработанный json файл
    data_off_filter = hh.file_json_for_work_programm.file_path_vac_for_filt_hh
    # Ссылка на обработанный json файл
    data_on_filter = hh.file_json_for_work_programm.file_path_print_for_user_hh

    true_search_fields = ['name', 'company_name', 'description']

    def __init__(self,
                 name_vacation: str,
                 area_part: object = None,
                 limit_count_page: object = 20,
                 no_magic_part: object = 'false',
                 choise_salary: object = None,
                 search_fields_part: object = None,
                 schedule_part: object = None,
                 employment_part: object = None,
                 experience_part: object = None,
                 page_part: object = 0,
                 ):

        self.file_json = None

        # Название ваканскии при инициализации класса
        self.name_vacation = name_vacation

        # Указываем регион выбора профессий
        self.area_part = area_part

        # График работы
        """
        fullDay - Полный день
        shift - Сменный график
        flexible - Гибкий график
        remote - Удаленная работа
        flyInFlyOut - Вахтовый метод
        """
        self.schedule_part = schedule_part

        # Тип занятости
        """
        full - Полная занятость
        part - Частичная занятость
        project - Проектная работа
        volunteer - Волонтерство
        probation - Стажировка
        """
        self.employment_part = employment_part

        # Опыт работы.
        """
        noExperience - Нет опыта
        between1And3 - От 1 года до 3 лет
        between3And6 - От 3 до 6 лет
        moreThan6 - Более 6 лет
        """
        self.experience_part = experience_part

        # Область поиска где написана искомая ваканския
        """
        name - в названии вакансии
        company_name - в названии компании
        description - в описании вакансии
        """
        if search_fields_part in self.true_search_fields:
            self.search_fields_part = search_fields_part
        elif search_fields_part == '' or search_fields_part is None:
            self.search_fields_part = ('name', 'company_name', 'description')
        else:
            raise Exception('''name - в названии вакансии
                            company_name - в названии компании
                            description - в описании вакансии''')

        # Выбор зарплаты
        self.choise_salary = choise_salary

        # Сколько ваканский на странице
        self.limit_count_page = limit_count_page

        # Номер страницы
        self.page_part = page_part

        """
        Если значение true — автоматическое преобразование вакансий отключено. 
        По умолчанию – false. При включённом автоматическом преобразовании, 
        будет предпринята попытка изменить текстовый запрос пользователя 
        на набор параметров.
        """
        self.no_magic_part = no_magic_part

    def get(self):
        """
        Получение json запроса
        """
        url = 'https://api.hh.ru/vacancies?'
        if self.no_magic_part != 'true':
            par = {'text': self.name_vacation,
                   'schedule': self.schedule_part,
                   'experience': self.experience_part,
                   'employment': self.employment_part,
                   'search_fields': self.search_fields_part,
                   'salary': self.choise_salary,
                   'area': self.area_part,
                   'per_page': self.limit_count_page,
                   'page': self.page_part,
                   'only_with_salary': 'true'
                   }
        else:
            par = {'text': self.name_vacation,
                   'per_page': self.limit_count_page,
                   'page': self.page_part,
                   'no_magic': 'true',
                   'only_with_salary': 'true'
                   }

        response = requests.get(url=url, params=par)
        if response.status_code == 200:
            pass
        else:
            raise GetDataSearchStatusCode
        data_j = response.json()
        self.file_json = data_j

    def write_in_data_on_filter(self):
        """
        Используется для записи в файл для пользователя
        """
        for x in range(len(self.file_json['items'])):
            with open(self.data_off_filter, 'r', encoding='UTF-8') as f:
                content = json.load(f)

                # Название вакансии
                vac_name = content['items'][x]['name']
                # Занятость вакансии
                vac_employment = content['items'][x]['employment']['name']
                # Требуемый опыт вакансии
                vac_experience = content['items'][x]['experience']['name']
                # Зарплата
                vac_salary_from = content['items'][x]['salary']['from']
                if vac_salary_from is None:
                    vac_salary_from = 0
                else:
                    vac_salary_from = vac_salary_from
                # Зарплата
                vac_salary_to = content['items'][x]['salary']['to']
                if vac_salary_to is None:
                    vac_salary_to = 0
                else:
                    vac_salary_to = vac_salary_to
                # Валюта
                vac_currency = content['items'][x]['salary']['currency']
                # Ссылка на вакансию
                vac_url = content['items'][x]['alternate_url']
                # Что требуется при устройстве на вакансию
                vac_snippet = content['items'][x]['snippet']["requirement"]
                # Название компании работадателя
                vac_work_app_name = content['items'][x]['employer']['name']
                # Адрес вакансии
                try:
                    vac_address = content['items'][x].get('address')['raw']
                except:
                    vac_address = content['items'][x].get('address')

                searching_data = {'items': [{
                    'Название ваканскии': vac_name,
                    'Тип занятости': vac_employment,
                    'Опыт работы': vac_experience,
                    'Зарплата от': vac_salary_from,
                    'Зарплата до': vac_salary_to,
                    'Валюта': vac_currency,
                    'API': 'HeadHunter',
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
                    'API': 'HeadHunter',
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
                        # Объединяем всё единый формат
                        file_data["items"].append(searching_data_app['items'])
                        # Устанавливаем текущее положение файла со смещением
                        file.seek(0)
                        # преобразоваем обратно в json
                        json.dump(file_data, file, indent=2, ensure_ascii=False)
                except:
                    with open(self.data_on_filter, "w") as file:
                        # Записываем данные в файл JSON
                        json.dump(searching_data, file, indent=2, ensure_ascii=False)

    def save_in_file_json(self):
        """
        Сохраняет результат поиска в json файл "vacation_for_filter_hh.json"
        """
        with open(self.data_off_filter, "w") as file:
            # Записываем данные в файл JSON
            json.dump(self.file_json, file, indent=2, ensure_ascii=False)

    def clear_file_json(self):
        """
        Очищает файл json полученный путем фильтрации
        """
        open(self.data_on_filter, "w").close()
