class GetDataSearchHHError(Exception):
    def __init__(self):
        self.message = 'Что-то не так'

    def __str__(self):
        return self.message


class GetDataSearchHHSchedule(GetDataSearchHHError):
    true_schedule = {'fullDay': 'Полный день',
                       'shift': 'Сменный график',
                       'flexible': 'Гибкий график',
                       'remote': 'Удаленная работа',
                       'flyInFlyOut': 'Вахтовый метод'}
    """
    Ислключение на график работы (schedule)
    Проверка на верное вхождение поиска
            # График работы

        fullDay - Полный день
        shift - Сменный график
        flexible - Гибкий график
        remote - Удаленная работа
        flyInFlyOut - Вахтовый метод
    """

    def __init__(self):
        self.message = (f'\nНет такого критерия поиска\n'
                        f'Измени атрибут schedule_part в class GetDataSearchHH\n'
                        f'Ниже приведен словарь из корректных параметров\n'
                        f'{self.true_schedule}')


class GetDataSearchHHEmployment(GetDataSearchHHError):
    true_employment = {'full': 'Полная занятость',
                       'part': 'Частичная занятость',
                       'project': 'Проектная работа',
                       'volunteer': 'Волонтерство',
                       'probation': 'Стажировка'}
    """
    Ислключение на график работы (employment)
    Проверка на верное вхождение поиска
            # Тип занятости

        full - Полная занятость
        part - Частичная занятость
        project - Проектная работа
        volunteer - Волонтерство
        probation - Стажировка
    """

    def __init__(self):
        self.message = (f'\nНет такого критерия поиска\n'
                        f'Измени атрибут employment_part в class GetDataSearchHH\n'
                        f'Ниже приведен словарь из корректных параметров\n'
                        f'{self.true_employment}')


class GetDataSearchHHExperience(GetDataSearchHHError):
    true_experience = {'noExperience': 'Нет опыта',
                       'between1And3': 'От 1 года до 3 лет',
                       'between3And6': 'От 3 до 6 лет',
                       'moreThan6': 'Более 6 лет'}
    """
    Ислключение на график работы (experience)
    Проверка на верное вхождение поиска
            # Тип занятости

        noExperience - Нет опыта
        between1And3 - От 1 года до 3 лет
        between3And6 - От 3 до 6 лет
        moreThan6 - Более 6 лет
    """

    def __init__(self):
        self.message = (f'\nНет такого критерия поиска\n'
                        f'Измени атрибут experience_part в class GetDataSearchHH\n'
                        f'Ниже приведен словарь из корректных параметров\n'
                        f'{self.true_experience}')
