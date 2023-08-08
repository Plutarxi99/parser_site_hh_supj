import datetime
import json

import isodate

from getdatasearchhh import GetDataSearchHH


class AnalysisOfDataHH(GetDataSearchHH):

    def __init__(self, name_vacation: str,
                 area_part: int,
                 schedule_part: str,
                 employment_part: str,
                 experience_part: str,
                 search_fields_part: str,
                 choise_salary: int,
                 limit_count_page: int
                 ):
        super().__init__(name_vacation,
                         area_part,
                         schedule_part,
                         employment_part,
                         experience_part,
                         search_fields_part,
                         choise_salary,
                         limit_count_page)
        self.json = self.get()

    def get_attrib(self):
        self.list_name_vacation = []
        self.list_url_vacation = []
        self.list_address_vacation = []
        self.list_employment_vacation = []
        self.list_experience_vacation = []
        self.list_snippet_vacation = []
        self.list_work_app_url_vacation = []
        self.list_work_app_name_vacation = []
        self.list_time_published_vacation = []
        for x in range(self.limit_count_page):
            # Название вакансии
            vac_name = self.json['items'][x]['name']
            self.list_name_vacation.append(vac_name)

            # Ссылка на вакансию
            vac_url = self.json['items'][x]['alternate_url']
            self.list_url_vacation.append(vac_url)

            # Адрес вакансии
            vac_address = self.json['items'][x]['address']
            self.list_address_vacation.append(vac_address)

            # Зарплата

            # Время публикации вакансии
            vac_time_published = self.json['items'][x]['published_at']
            date_time_obj = datetime.datetime.strptime(vac_time_published, '%Y-%m-%dT%H:%M:%S%z')
            # print('Дата:', date_time_obj.date())
            # print('Время:', date_time_obj.time())
            # print('Дата и время:', date_time_obj)
            self.list_time_published_vacation.append(date_time_obj.date())

            # Название компании работадателя
            vac_work_app_name = self.json['items'][x]['employer']['name']
            self.list_work_app_name_vacation.append(vac_work_app_name)

            # Ссылка на работадателя
            vac_work_app_url = self.json['items'][x]['employer']['alternate_url']
            self.list_work_app_url_vacation.append(vac_work_app_url)

            # Что требуется при устройстве на вакансию
            vac_snippet = self.json['items'][x]['snippet']["requirement"]
            self.list_snippet_vacation.append(vac_snippet)

            # Требуемый опыт вакансии
            vac_experience = self.json['items'][x]['experience']['name']
            self.list_experience_vacation.append(vac_experience)

            # Занятость вакансии
            vac_employment = self.json['items'][x]['employment']['name']
            self.list_employment_vacation.append(vac_employment)
        return self.list_snippet_vacation
    def save_vacation(self):
        data = 'vacation_for_filter'
        for x in range(self.limit_count_page):
            vac_name = self.json['items'][x]['name']
            vac_employment = self.json['items'][x]['employment']['name']
            vac_experience = self.json['items'][x]['experience']['name']
            vac_url = self.json['items'][x]['alternate_url']
            vac_snippet = self.json['items'][x]['snippet']["requirement"]
            vac_work_app_name = self.json['items'][x]['employer']['name']
            vac_address = self.json['items'][x]['address']

            searching_data = {
                'Название ваканскии': vac_name,
                'Тип занятости': vac_employment,
                'Опыт работы': vac_experience,
                'url': vac_url,
                'Требования': vac_snippet,
                'Название компании': vac_work_app_name,
                'Адрес': vac_address
            }
            # Делаем запись в json формате в файл указанной функции data
            with open(data, "w") as file:
                # Записываем данные в файл JSON
                json.dump(searching_data, file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    u = AnalysisOfDataHH(name_vacation="Junior",
                         area_part=1,
                         schedule_part="fullDay",
                         employment_part="full",
                         experience_part="between1And3",
                         search_fields_part="name",
                         choise_salary=30000,
                         limit_count_page=5
                         )
    print(u.save_vacation())
