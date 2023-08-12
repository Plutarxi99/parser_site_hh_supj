import json
import hh.file_json_for_work_programm

data_off_filter = hh.file_json_for_work_programm.file_path_vac_for_filt
if __name__ == '__main__':
    for x in range(5):
        with open(data_off_filter, 'r', encoding='UTF-8') as f:
            content = json.load(f)
    # # Название вакансии
    #     vac_name = content['items'][x]['name']
    # # Занятость вакансии
    #     vac_employment = content['items'][x]['employment']['name']
    # # Требуемый опыт вакансии
    #     vac_experience = content['items'][x]['experience']['name']
    # # Зарплата
    #     vac_salary = content['items'][x]['salary']['from']
    # # Ссылка на вакансию
    #     vac_url = content['items'][x]['alternate_url']
    # # Что требуется при устройстве на вакансию
    #     vac_snippet = content['items'][x]['snippet']["requirement"]
    # # Название компании работадателя
    #     vac_work_app_name = content['items'][x]['employer']['name']
    # Адрес вакансии
            try:
                vac_address = content['items'][x].get('address')['raw']
            except:
                vac_address = content['items'][x].get('address')
            print(vac_address)