from abc import ABC, abstractmethod


class GetDataSearch(ABC):
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def write_in_data_on_filter(self):
        pass

    @abstractmethod
    def save_in_file_json(self):
        pass

    @abstractmethod
    def clear_file_json(self):
        pass

    def __str__(self):
        return 'Абстрактный класс. Как должен выглядить класс'
