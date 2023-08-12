from talk_for_user import talk_to_user
from analysisofdataHH import AnalysisOfDataHH
from getdatasearchhh import GetDataSearchHH


def work_programm(count_page):
    dict_ttu = talk_to_user()
    print(dict_ttu)
    for x in range(count_page):
        data_json = GetDataSearchHH(name_vacation=dict_ttu['vac'],
                                    area_part=dict_ttu['area'],
                                    schedule_part=dict_ttu['sched'],
                                    employment_part=dict_ttu['employ'],
                                    experience_part=dict_ttu['exp'],
                                    search_fields_part=dict_ttu['field'],
                                    choise_salary=dict_ttu['salary'],
                                    limit_count_page=dict_ttu['per_page'],
                                    page_part=x,
                                    no_magic_part=dict_ttu['magic']
                                    ).get()
        print(data_json)
        file_json = AnalysisOfDataHH(data_json)
        input()
