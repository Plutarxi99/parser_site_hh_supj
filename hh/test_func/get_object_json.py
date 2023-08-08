import requests


class GetObjectJsonHH:

    def __init__(self):
        self.url = f'https://api.hh.ru/'
        self.hh_vacancy = None
        self.hh_region = None

    def get_object(self, url):
        response = requests.get(url)
        data_j = response.json()
        return data_j

    def get_vacancy(self, text_vacancy: str):
        url = self.url
        url_vac = f'{url}vacancies?name={text_vacancy}'
        obj_vac = self.get_object(url_vac)
        return obj_vac['items'][1]['name']

    def get_region(self, region: int):
        url = self.url
        url_vac = f'{url}vacancies?area={region}'
        obj_vac = self.get_object(url_vac)
        return obj_vac['items']


if __name__ == '__main__':
    # vakancy = 'электрик'
    # id_region = 1
    # URL = f'https://api.hh.ru/vacancies?text={vakancy}&area={id_region}'
    j = GetObjectJsonHH()
    print(j.get_vacancy("тепло"))
    # print(j.get_region(25))
    # print(j.url.keys())