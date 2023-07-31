import requests


# https://shatura.hh.ru/search/vacancy?text=тепло&area=1
# vakancy = 'электрик'
# id_region = 1
# URL = f'https://api.hh.ru/vacancies?text={vakancy}&area={id_region}'

def test_url():

    # Область поиска
    """
    name - в названии вакансии
    company_name - в названии компании
    description - в описании вакансии
    """
    search_fields_part = "name"
    search_fields = f"search_field={search_fields_part}"

    # Опыт работы.
    """
    noExperience - Нет опыта
    between1And3 - От 1 года до 3 лет
    between3And6 - От 3 до 6 лет
    moreThan6 - Более 6 лет
    """
    experience_part = "between1And3"
    experience = f"experience={experience_part}"

    # Тип занятости
    """
    full - Полная занятость
    part - Частичная занятость
    project - Проектная работа
    volunteer - Волонтерство
    probation - Стажировка
    """
    employment_part = "full"
    employment = f'employment={employment_part}'

    # График работы
    """
    fullDay - Полный день
    shift - Сменный график
    flexible - Гибкий график
    remote - Удаленная работа
    flyInFlyOut - Вахтовый метод
    """
    schedule_part = "fullDay"
    schedule = f'schedule={schedule_part}'

    #

    # Указываем регион выбора профессий
    area_part = 1
    area = f"area={area_part}"

    # Кластер для зарплаты
    claster_part = "salary"
    claster = f'vacancy_cluster={claster_part}'

    # Кластер по возрастанию/убыванию зарплат
    """
    salary_desc - по убыванию зарплат
    salary_asc - по возрастанию зарплаты
    """
    claster_option_part = "salary_asc"
    claster_option = f'order_by={claster_option_part}'

    t = "Junior"
    text = f'text="{t}"'

    URL = (f'https://api.hh.ru/vacancies?'
           f'&{schedule}'
           f'&{employment}'
           # f'&{experience}'
           # f'&{search_fields}'
           # f'&{text}'
           f'&salary=150000'
           f'&{area}'
           # f'&{claster}'
           # f'&{claster_option}'          
           # f'&clusters=true'
           # f'&only_with_salary=true') # вилка зарплаты указана
           # f'&per_page=0'           
           f'')
    # URL = f'https://api.hh.ru/vacancies?vacancy_cluster=salary&vacancy_search_order=salary_asc&per_page=0'
    # URL = f'https://api.hh.ru/vacancies?{claster}&{claster_option}&per_page=0'
    response = requests.get(URL)
    data_j = response.json()

    # content = response.content
    # headers = response.headers['items']
    # id = []
    # for x in data_j:
    #     id.append(x['areas'])
    # return response
    return data_j
# print(test_url())


def get_schedule():
    """Занятость в вакансии"""
    URL = 'https://api.hh.ru/vacancies?schedule=fullDay'
    response = requests.get(URL)
    data_j = response.json()
    return data_j['items'][0]['employment']['name'] # Полная занятость

def iter_vacancy():
    """Итерация объекта вакансия"""
    URL = 'https://api.hh.ru/vacancies?text="Junior"&area=20' # clusters=true
    response = requests.get(URL)
    data_j = response.json()
    l = len(data_j['items'])
    # for x in data_j['items']:
        # return data_j
    return data_j

if __name__ == '__main__':

    print(test_url())
    # print(get_schedule())
    # print(iter_vacancy())
    # print(data_j['items'][0]['employment']['name']) # Полная занятость
    # data = req.content.decode()
    # req.close()
    # count_of_employers = json.loads(data)

# URL = 'https://api.hh.ru/vacancies?schedule=fullDay'
# req = requests.get(URL)
# data_j = req.json()

