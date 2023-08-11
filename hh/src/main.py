import json
from talk_for_user import talk_to_user
from analysisofdataHH import AnalysisOfDataHH
from qwe import GetDataSearchHH
import hh.file_json_for_work_programm

if __name__ == '__main__':

    # u = AnalysisOfDataHH(name_vacation="Сварщик",
    #                      area_part=1817,
    #                      schedule_part="fullDay",
    #                      employment_part="full",
    #                      experience_part="between1And3",
    #                      search_fields_part="name",
    #                      choise_salary=30000,
    #                      limit_count_page=5
    #                      )
    # u.save_in_file_json()
    # u.write_in_data_on_filter()
    #
    # ttu = talk_to_user()
    ttu = {
        'vac': 'Junior',
        'area': 1,
        'sched': '',
        'employ': '',
        'exp': '',
        'field': 'name',
        'salary': 30000,
        'page': 5
    }
    data_json = GetDataSearchHH(name_vacation=ttu['vac'],
                                area_part=ttu['area'],
                                # schedule_part=ttu['sched'],
                                # employment_part=ttu['employ'],
                                # experience_part=ttu['exp'],
                                # search_fields_part=ttu['field'],
                                # choise_salary=ttu['salary'],
                                # limit_count_page=ttu['page']
                                ).get()
    print(data_json)
    file_json = AnalysisOfDataHH(data_json)
    file_json.save_in_file_json()
    file_json.write_in_data_on_filter()
    # file_json.append_in_data_on_filter()
    # data_json = hh.file_json_for_work_programm.file_path_vac_for_filt
    # with open(data_json, 'r', encoding='UTF-8') as f:
    #     content = json.load(f)
    #     print(len(content['items']))
    #
    # data_off_filter = hh.file_json_for_work_programm.file_path_vac_for_filt
    # data_on_filter = hh.file_json_for_work_programm.file_path_print_for_user
    #
    # for x in range(5):
    #     with open(data_off_filter, 'r', encoding='UTF-8') as f:
    #         content = json.load(f)
    #
    #         vac_name = content['items'][x]['name']
    #         vac_employment = content['items'][x]['employment']['name']
    #         vac_experience = content['items'][x]['experience']['name']
    #         vac_url = content['items'][x]['alternate_url']
    #         vac_snippet = content['items'][x]['snippet']["requirement"]
    #         vac_work_app_name = content['items'][x]['employer']['name']
    #         vac_address = content['items'][x]['address']
    #
    #         searching_data = {'items': [{
    #             'Название ваканскии': vac_name,
    #             'Тип занятости': vac_employment,
    #             'Опыт работы': vac_experience,
    #             'url': vac_url,
    #             'Требования': vac_snippet,
    #             'Название компании': vac_work_app_name,
    #             'Адрес': vac_address
    #         }]}
    #         searching_data_app = {'items': {
    #             'Название ваканскии': vac_name,
    #             'Тип занятости': vac_employment,
    #             'Опыт работы': vac_experience,
    #             'url': vac_url,
    #             'Требования': vac_snippet,
    #             'Название компании': vac_work_app_name,
    #             'Адрес': vac_address
    #         }}
    #     with open(data_on_filter, 'r+') as f_1:
    #         try:
    #             contic = json.load(f_1)
    #             with open(data_on_filter, 'r+') as file:
    #                 # First we load existing data into a dict.
    #                 file_data = json.load(file)
    #                 # Join new_data with file_data inside emp_details
    #                 file_data["items"].append(searching_data_app['items'])
    #                 # Sets file's current position at offset.
    #                 file.seek(0)
    #                 # convert back to json.
    #                 json.dump(file_data, file, indent=4, ensure_ascii=False)
    #         except:
    #             with open(data_on_filter, "w") as file:
    #                 # Записываем данные в файл JSON
    #                 json.dump(searching_data, file, indent=2, ensure_ascii=False)

