# parser_site_hh_supj
Привет! Программы нужна для парсинга такий сайтов: "https://hh.ru/" и "https://www.superjob.ru/".
Программа запускается из "/parser_site_hh_supj/main.py"
Программы имеет два режима для поиска вакансии:
1. Можно записать в одну строчку то, что ты ищешь. (прим. "Инженер Москва 45000"). И только в таком порядке.
2. Можно более детально использовать поиск. Использует такие параметры: график работы, тип занятости, опыт и где надо искать название вакансии.


Программы записывает:
1. Необработанные json файлы в "/parser_site_hh_supj/<abstract>/file_json_for_work_programm/vacation_for_filter_<abstract>.json"

2. Обработанные json файлы в "/parser_site_hh_supj/<abstract>/file_json_for_work_programm/file_for_user_<abstract>.json"

3. Записывает всё в общий файл:

   3.1 Необработанные json файл "/parser_site_hh_supj/src_and_file/file_json_for_work_programm/vacation_for_filter.json"
   
   3.2 Обработанный json файл "/parser_site_hh_supj/src_and_file/file_json_for_work_programm/file_for_user.json"

Программа имеет функцию фильтрации по з\п. Для её использования необходимо запустить программу.
