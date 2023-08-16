import os
import pathlib

# Создаем абсолютный путь до папки с файлами
script_dir = os.path.dirname(__file__)

file_path_vac_for_filt = (pathlib.PurePath(f'{script_dir}')
        .joinpath('vacation_for_filter.json'))
"""Создаем путь до нужного файла,
где хранятся записанные ваканскии с заданными параметрами"""

# Создаем путь до нужного файла
file_path_print_for_user = (pathlib.PurePath(f'{script_dir}')
        .joinpath('file_for_user.json'))
"""Создаем путь до нужного файла,
где записывается файл для чтения пользователя"""
