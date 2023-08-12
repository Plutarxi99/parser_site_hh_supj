import requests
from exception import GetDataSearchHHSchedule, GetDataSearchHHEmployment, GetDataSearchHHExperience


class GetDataSearchHH:
    true_schedule = ['fullDay', 'shift', 'flexible', 'remote', 'flyInFlyOut']
    true_employment = ['full', 'part', 'project', 'volunteer', 'probation']
    true_experience = ['noExperience', 'between1And3', 'between3And6', 'moreThan6']
    true_search_fields = ['name', 'company_name', 'description']

    def __init__(self,
                 name_vacation: str,
                 area_part=113,
                 limit_count_page=10,
                 no_magic_part='false',
                 choise_salary=None,
                 search_fields_part=None,
                 schedule_part=None,
                 employment_part=None,
                 experience_part=None,
                 page_part=0,
                 ):

        super().__init__()
        # Название ваканскии при инициализации класса
        self.no_magic_part = None
        self.schedule_part = None
        self.name_vacation = name_vacation
        self.text = f'text="{self.name_vacation}"'

        # Указываем регион выбора профессий
        # self.area_part = area_part
        # self.area = f"area={self.area_part}"
        if isinstance(area_part, int):
            self.area_part = area_part
            self.area = f'area={self.area_part}'
        elif area_part == '' or self.area_part is None:
            self.area = f''
        else:
            raise Exception('Число надо')

        # График работы
        """
        fullDay - Полный день
        shift - Сменный график
        flexible - Гибкий график
        remote - Удаленная работа
        flyInFlyOut - Вахтовый метод
        """
        # Делаем блок исключений для корректного отображения данных
        if schedule_part in self.true_schedule:
            self.schedule_part = schedule_part
            self.schedule = f'schedule={self.schedule_part}'
        elif schedule_part == '' or self.schedule_part is None:
            self.schedule = f''
        else:
            raise GetDataSearchHHSchedule

        # Тип занятости
        """
        full - Полная занятость
        part - Частичная занятость
        project - Проектная работа
        volunteer - Волонтерство
        probation - Стажировка
        """
        # Делаем блок исключений для корректного отображения данных
        if employment_part in self.true_employment:
            self.employment_part = employment_part
            self.employment = f'employment={self.employment_part}'
        elif employment_part == '' or employment_part is None:
            self.employment = f''
        else:
            raise GetDataSearchHHEmployment
        # self.employment_part = employment_part
        # self.employment = f'employment={self.employment_part}'

        # Опыт работы.
        """
        noExperience - Нет опыта
        between1And3 - От 1 года до 3 лет
        between3And6 - От 3 до 6 лет
        moreThan6 - Более 6 лет
        """
        if experience_part in self.true_experience:
            self.experience_part = experience_part
            self.experience = f'experience={self.experience_part}'
        elif experience_part == '' or experience_part is None:
            self.experience = f''
        else:
            raise GetDataSearchHHExperience
        # self.experience_part = experience_part
        # self.experience = f"experience={self.experience_part}"

        # Область поиска где написана искомая ваканския
        """
        name - в названии вакансии
        company_name - в названии компании
        description - в описании вакансии
        """
        # self.search_fields_part = search_fields_part
        # self.search_fields = f"search_field={self.search_fields_part}"
        if search_fields_part in self.true_search_fields:
            self.search_fields_part = search_fields_part
            self.search_fields = f'search_fields={self.search_fields_part}'
        elif search_fields_part == '' or search_fields_part is None:
            # self.search_fields = f''
            self.search_fields = f'search_field=name&search_field=company_name&search_field=description'
        else:
            raise Exception('''name - в названии вакансии
                            company_name - в названии компании
                            description - в описании вакансии''')

        # Выбор зарплаты
        # self.choise_salary = choise_salary
        # self.salary = f'salary={self.choise_salary}'

        if isinstance(choise_salary, int):
            self.choise_salary = choise_salary
            self.salary = f'salary={self.choise_salary}'
        elif choise_salary == '' or choise_salary is None:
            self.salary = f''
        else:
            raise Exception('''Зарплата не такая должна быть''')

        # Сколько ваканский на странице
        self.limit_count_page = limit_count_page
        self.per_page = f'per_page={self.limit_count_page}'

        # Номер страницы
        self.page_part = page_part
        self.page = f'page={self.page_part}'

        """
        Если значение true — автоматическое преобразование вакансий отключено. 
        По умолчанию – false. При включённом автоматическом преобразовании, 
        будет предпринята попытка изменить текстовый запрос пользователя 
        на набор параметров.
        """
        if self.no_magic_part == 'true':
            self.no_magic_part = no_magic_part
            self.no_magic = f'no_magic={no_magic_part}'
        else:
            self.no_magic_part = 'false'
            self.no_magic = f'no_magic={no_magic_part}'

    def get(self):
        # Получение ссылки для работы
        URL = (f'https://api.hh.ru/vacancies?'
               f'&{self.schedule}'
               f'&{self.employment}'
               f'&{self.experience}'
               f'&{self.search_fields}'
               f'&{self.text}'
               f'&{self.salary}'
               f'&{self.area}'
               f'&{self.per_page}'
               f'&{self.page}'
               f'&no_magic=false'
               f'&only_with_salary=true'  # Показывать вакансии только с указанием зарплаты
               f'')
        response = requests.get(URL)
        data_j = response.json()
        return data_j

    # def get_text_magic(self):
    #     # Получение ссылки для работы
    #     URL = (f'https://api.hh.ru/vacancies?'
    #            f'&{self.text}'
    #            f'&{self.per_page}'
    #            f'&{self.page}'
    #            f'&no_magic=false'
    #            f'&only_with_salary=true'  # Показывать вакансии только с указанием зарплаты
    #            f'')
    #     response = requests.get(URL)
    #     data_j = response.json()
    #     return data_j
