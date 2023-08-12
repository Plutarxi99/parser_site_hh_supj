import getdatasearchhh


def talk_to_user():
    """
    Функция общается с пользователем и получает от него информация
    для поиска требуемой вакансии.
    В ответ мы получаем словарь, который вставляется в экземляр класса
    для получения json запросов
    :return: dict_answer {dict}
    """

    while True:
        true_schedule = ('', 'fullDay', 'shift', 'flexible', 'remote', 'flyInFlyOut')
        true_employment = ('', 'full', 'part', 'project', 'volunteer', 'probation')
        true_experience = ('', 'noExperience', 'between1And3', 'between3And6', 'moreThan6')
        true_search_fields_part = ('', 'name', 'company_name', 'description')

        print('Привет! Если хочешь найти вакансию, которую ты хочешь'
              ', тебе надо ответить на пару вопросов.')

        while True:
            print('Можно более детально выбрать вакансию или '
                  'написать всё в одной строк\n'
                  '1: Достаточно написать в одной строке, что ты хочешь\n'
                  '2: Детальный поиск по заданным критериям')
            ch = int(input())
            if ch == 1:
                name_vacation_input = input('Напиши название вакансии, '
                                            'которую хочешь найти\n')

                dict_text = {
                    'vac': name_vacation_input,
                    'area': '',
                    'sched': '',
                    'employ': '',
                    'exp': '',
                    'field': '',
                    'salary': '',
                    'magic': 'true',
                    'per_page': 5,
                    'page': 5
                }
                return dict_text
            elif ch == 2:
                break
            else:
                continue
        name_vacation_input = input('Напиши название вакансии, '
                                    'которую хочешь найти\n')

        while True:
            try:
                area_part_input = int(input('Напиши в каком регионе в котором хочешь работать\n'))
                break
            except:
                print('Вы указали строку. Укажите id региона. Попробуйте ещё раз! '
                      'Нажмите "Enter" для продолжения')
                input()
                continue

        while True:
            schedule_part_input = int(input('Напиши какой график работы тебе нужен\n'
                                            'Выбери цифру:\n'
                                            '1: Полный день\n'
                                            '2: Сменный график\n'
                                            '3: Гибкий график\n'
                                            '4: Удаленная работа\n'
                                            '5: Вахтовый метод\n'
                                            '0: Отмена. Если не хотите использовать этот фильтр'))
            if schedule_part_input == 0:
                break
            elif schedule_part_input not in [1, 2, 3, 4, 5]:
                print('Укажите число, которое есть в списке. '
                      'Попробуйте ещё раз! '
                      'Нажмите "Enter" для продолжения')
                input()
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
                                              '0: Отмена. Если не хотите использовать этот фильтр'))
            if employment_part_input == 0:
                break
            elif employment_part_input not in [1, 2, 3, 4, 5]:
                print('Укажите число, которое есть в списке. '
                      'Попробуйте ещё раз! '
                      'Нажмите "Enter" для продолжения')
                input()
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
                                              '0: Отмена. Если не хотите использовать этот фильтр'))
            if experience_part_input == 0:
                break
            elif experience_part_input not in [1, 2, 3, 4]:
                print('Укажите число, которое есть в списке. '
                      'Попробуйте ещё раз! '
                      'Нажмите "Enter" для продолжения')
                input()
                continue
            else:
                break

        while True:
            search_fields_part_input = int(input('Напиши где надо искать название вакансии\n'
                                                 'Выбери цифру:\n'
                                                 '1: в названии вакансии\n'
                                                 '2: в названии компании\n'
                                                 '3: в описании вакансии\n'
                                                 '0: Отмена. Если не хотите использовать этот фильтр'))
            if search_fields_part_input == 0:
                break
            if search_fields_part_input not in [1, 2, 3]:
                print('Укажите число, которое есть в списке. '
                      'Попробуйте ещё раз! '
                      'Нажмите "Enter" для продолжения')
                input()
                continue
            else:
                break

        while True:
            choise_salary_input = int(input('Напиши какую зарплату хочешь\n'))
            if not choise_salary_input > 0:
                print('Зарплата должно быть не отрицательной')
            else:
                break

        # while True:
        #     limit_count_page_input = int(input('Напиши сколько ваканский надо вывести\n'))
        #     if not 0 < limit_count_page_input < 100:
        #         continue
        #     else:
        #         break

        dict_answer = {
            'vac': name_vacation_input,
            'area': area_part_input,
            'sched': true_schedule[schedule_part_input],
            'employ': true_employment[employment_part_input],
            'exp': true_experience[experience_part_input],
            'field': true_search_fields_part[search_fields_part_input],
            'salary': choise_salary_input,
            'per_page': 10,
            'page': 0,
            'magic': 'false'
        }
        return dict_answer
