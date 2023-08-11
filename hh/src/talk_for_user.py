def talk_to_user():
    """
    Функция общается с пользователем и получает от него информация
    для поиска требуемой вакансии.
    В ответ мы получаем словарь, который вставляется в экземляр класса
    для получения json запросов
    :return: dict_answer {dict}
    """

    while True:
        true_schedule = ['fullDay', 'shift', 'flexible', 'remote', 'flyInFlyOut']
        true_employment = ['full', 'part', 'project', 'volunteer', 'probation']
        true_experience = ['noExperience', 'between1And3', 'between3And6', 'moreThan6']
        true_search_fields_part = ['name', 'company_name', 'description']

        word_cancel = 'Отмена', 0
        print('Привет! Если хочешь найти вакансию, которую ты хочешь'
              ', тебе надо ответить на пару запросов.')
        name_vacation_input = input('Напиши название вакансии, '
                                    'которую хочешь найти\n')

        area_part_input = int(input('Напиши в каком регионе в котором хочешь работать\n'))

        while True:
            schedule_part_input = int(input('Напиши какой график работы тебе нужен\n'
                                            'Выбери цифру:\n'
                                            '1: Полный день\n'
                                            '2: Сменный график\n'
                                            '3: Гибкий график\n'
                                            '4: Удаленная работа\n'
                                            '5: Вахтовый метод\n'
                                            '0: Отмена'))
            if schedule_part_input not in [0, 1, 2, 3, 4, 5]:
                continue
            else:
                break

        while True:
            employment_part_input = int(input('Напиши какой тип занятости хочешь найти\n'
                                              'Выбери цифру:\n'
                                              '1: Полная занятость\n'
                                              '2: Частичная занятость\n'
                                              '3: Проектная работа\n'
                                              '4: Волонтерство\n'
                                              '5: Стажировка\n'
                                              '0: Отмена'))
            if employment_part_input not in [0, 1, 2, 3, 4, 5]:
                continue
            else:
                break

        while True:
            experience_part_input = int(input('Напиши какой опыт требуется для вакансии\n'
                                              'Выбери цифру:\n'
                                              '1: Нет опыта\n'
                                              '2: От 1 года до 3 лет\n'
                                              '3: От 3 до 6 лет\n'
                                              '4: Более 6 лет\n'
                                              '0: Отмена'))
            if experience_part_input not in [0, 1, 2, 3, 4]:
                continue
            else:
                break

        while True:
            search_fields_part_input = int(input('Напиши где надо искать название вакансии\n'
                                                 'Выбери цифру:\n'
                                                 '1: в названии вакансии\n'
                                                 '2: в названии компании\n'
                                                 '3: в описании вакансии\n'
                                                 '0: Отмена'))
            if experience_part_input not in [0, 1, 2, 3]:
                continue
            else:
                break
        while True:
            choise_salary_input = int(input('Напиши какую зарплату хочешь\n'))
            if 0 > choise_salary_input:
                print('Зарплата должно быть не отрицательной')
            else:
                break


        while True:
            limit_count_page_input = int(input('Напиши сколько ваканский надо вывести\n'))
            if not 0 < limit_count_page_input < 100:
                continue
            else:
                break

        dict_answer = {
            'vac': name_vacation_input,
            'area': area_part_input,
            'sched': true_schedule[schedule_part_input - 1],
            'employ': true_employment[employment_part_input - 1],
            'exp': true_experience[experience_part_input - 1],
            'field': true_search_fields_part[search_fields_part_input],
            'salary': choise_salary_input,
            'page': limit_count_page_input
        }
        return dict_answer


if __name__ == '__main__':
    print(talk_to_user())
