# ----------------------------------------------
# * imports : 
# ----------------------------------------------


# ----------------------------------------------
# * vars :
# ----------------------------------------------
# ** one liner:
# gv_filename = "Data_files/metod01.xlsx"
gv_filename = "Data_files/metod01.xlsx"
gv_output = "Data_files/output.xlsx"
# sheet_name = "показники"
gv_sheet_name = "квартири, площі"
gv_sheet_report = "report"
# ** Kooficeints:
# обсяг тепла на функц. системи = 5% якщо є погодне регулювання в ІТП або 15% якщо не має від
gk_Qfun_sys = 0.05
# gk_Qfun_sys = 0
# обсяг тепла на опалення МЗК = 10% від
gk_Qmzk = 0.1
# gk_Qmzk = 0
# Мінімальна частка середнього питомого споживання
gk_Qop_min = 0.5
# ** setings:
# количество знаков после запятой для gk_Qop_min переменой
# при повышение точности в этой переменой разница силльно растёт
# False для максимальной точности
# True для
# 3 значения соответствуюшее екселю
gk_Qop_min_after_point = False
# максимальное количество повторений поика нуля
# (повторения циклов распределения)
# 2 для значений близких к exel
gs_recalc_surcharge_times = 200
# печатать шаг на котором найден ноль
gs_recalc_surcharge_print_result = False
gs_recalc_surcharge_print = False
# ** exel coordinats:
# *** "квартири, площі":
gl_app_sum_area_column = 4 # номер колонки (Площа загальна по даним КТЕ)
gl_app_heating_area_column = 5 # номер колонки (Площа опалювальна по КТЕ)
gl_counters_column = 6 # номер колонки (№ розподілювача)
gl_counters_k_priv_column = 15 # номер колонки (К приведене)
gl_counters_value1_column = 17 # номер колонки (показники на 01.12)
gl_counters_value2_column = 18 # номер колонки (показники на 01.11)
gl_ferst_app_row = 1 # номер ряда первого апартамента
gl_exl_shift_rows = 1 # количество рядов сдвига адреса в экселе от дата фрема в выдачи ошибки
# сдвиг строки от значения end для : по будинку за т/ліч
gl_shift_home_counter_value1 = 2
gl_shift_home_counter_value2 = 2
# колонки : по будинку за т/ліч
gl_column_home_counter_value1 = 17
gl_column_home_counter_value2 = 18
# *** report sheet:
# 0 № п/п	
# 1 № квартири	
# 2 Ітого по распр., Гкал
gl_total_couter_e_column = 2
# 3 Ітого по м2, Гкал
gl_total_no_couter_e_column = 3
# 4 функціонування системи
gl_func_sys_column = 4
# 5 МЗК
gl_mzk_column = 5
# 6 ВСЬОГО, Гкал
gl_total_e_column = 6
# ** title_list : 
title_list = [
    "№ п/п",
    "№ квартири",
    "поверх",
    "кіл-ть",
    "кімнат",
    "Площа загальна по даним КТЕ",
    "Площа опалювальна по КТЕ",
    "№ розподілювача ",
    "розташування",
    "тип радіатора",
    "кіл-ть секцій",
    "розмір д/в/г см",
    "Q радіатора, Вт",
    "Kq",
    "Kc",
    "Ккв",
    "К приведене",
    "показники   на 01.12",
    "показники   на 01.11",
    "споживання за період",
    "споживання за період приведене",
    "сумарне споживання по квартирі, од.",
    "сумарне приведене споживання по квартирі, од.",
    "приведене до м2 площі, од/м2",
    "обсяг споживання за період, Гкал",
    "приведене до м2 площі, Гкал/м2",
    "донарахування, Гкал",
    "логіка, не міняти! (площа повернення)",
    "повернення у звязку з уточненням, Гкал",
    "Ітого, Гкал",
    "уточнене приведене до м2 площі, Гкал/м2",
    "уточнене донарахування, Гкал",
    "Ітого, Гкал",
    "логіка, не міняти! (площа повернення)",
    "2-ге повернення у звязку з уточненням, Гкал",
    "Ітого по распр., Гкал",
    "2-ге уточнене приведене до м2 площі, Гкал/м2",
    "Кінцева перевірка",
    "Ітого по м2, Гкал",
    "функціонування системи",
    "МЗК",
    "ВСЬОГО, Гкал",]
# print("tile 1 =", title_list[1])


# ----------------------------------------------
# * -------------------------------------------:
