import os
import pathlib


# Создаем абсолютный путь до папки с файлами
script_dir = os.path.dirname(__file__)

abstract_class_getdatasearch = (pathlib.PurePath(f'{script_dir}')
        .joinpath('getdatasearch.py'))
"""Создаем путь до нужного файла,
где хранится абстрактный класс 
"""