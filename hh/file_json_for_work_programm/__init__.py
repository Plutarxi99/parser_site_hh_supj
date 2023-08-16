import os
import pathlib

# Создаем абсолютный путь до папки с файлами
script_dir = os.path.dirname(__file__)


file_path_vac_for_filt_hh = (pathlib.PurePath(f'{script_dir}')
        .joinpath('vacation_for_filter_hh.json'))
"""
HeadHunter
Создаем путь до нужного файла,
где хранятся записанные ваканскии с заданными параметрами
"""

# Создаем путь до нужного файла
file_path_print_for_user_hh = (pathlib.PurePath(f'{script_dir}')
                               .joinpath('file_for_user_hh.json'))
"""
HeadHunter
Создаем путь до нужного файла,
где записывается файл для чтения пользователя
"""
