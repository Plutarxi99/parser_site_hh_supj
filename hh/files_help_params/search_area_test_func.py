import json
import objectpath

def search_area():
    with open('area_id.json', 'r') as file:
        content = json.load(file)
        return content


if __name__ == '__main__':
    con = search_area()
    data_country = objectpath.filter_dict(con, 'name')
    data_ = objectpath.filter_dict(con, keys='name')
    # print(len(con))
    # Список стран
    # for x in range(len(con)):
    #     print(con[x]['name'])
    #
    # # Список Республик и областей
    # print(len(con[0]['areas']))
    # for a in range(len(con[0]['areas'])):
    #     print(con[0]['areas'][a])

    # 1817
    # print(len(con[0]['areas']))
    # for y in range(len(con[0]['areas'])):
    #     for k, v in con[0]['areas'][y].items():
    #         if v == "Белгородская область":
    #             print(k, v)
    # print(con[0]['areas'][0]['id'])
    for x in range(len(con)):
        print(con[x]['name'])
        country = input()
        if country == 'Россия':
            print(con[0]['areas'])
        else:
            break

