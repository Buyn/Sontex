# ----------------------------------------------
# * imports : 
# ----------------------------------------------


# ----------------------------------------------
# * vars :
# ----------------------------------------------
# ** GUI:
# *** main window:
# gg_eel_mode = 'electron'
# gg_eel_mode = 'chrome'
# gg_eel_mode = None
# gg_eel_mode = 'edge'
gg_eel_mode = 'chrome'
gg_GUI = True
# gg_GUI = False
# ** .xlsx:
# gv_filename = "Data_files/metod01.xlsx"
gv_output = "Data_files/output.xlsx"
gv_filename = "Data_files/metod01.xlsx"
# sheet_name = "показники"
gv_sheet_name = "квартири, площі"
gv_sheet_report = "report"

# ** .csv:
gv_csv = "Data_files/test.csv"
# кодировка файла
gv_csv_encoding = "cp1252"
# строки с которых начинается имена колонок
gv_csv_header   = 1
# номер колонки от 0 в котором указаны индефикаторы устройств 
gv_csv_index_col= 5
# символ раздилитель используюшийся в файле
gv_csv_sep      = ";"
gv_csv_name_i   = 1
gv_csv_name_date= "Historic date - "
gv_csv_name_value="Historic value - "
# name_text = "Historic date - " + str(gv_csv_name_i)
# name_value = "Historic value - " + str(gv_csv_name_i)

# ** .rlv:
gv_rlv = "Data_files/test.rlv"
# gv_rlv = "Data_files/test.rlv"
# кодировка файла
gv_rlv_encoding = "utf-16le"
# строки с которых начинается имена колонок
gv_rlv_header   = 0
# номер колонки от 0 в котором указаны индефикаторы устройств 
gv_rlv_index_col= 5
# символ раздилитель используюшийся в файле
# gv_rlv_sep      = ";"
gv_rlv_sep      = "\t"
# gv_rlv_sep      = "	"
# gv_rlv_sep      = ""
gv_rlv_name_i   = 1
gv_rlv_name_date= "Historic date - "
gv_rlv_name_value="Historic value - "
# name_text = "Historic date - " + str(gv_rlv_name_i)
# name_value = "Historic value - " + str(gv_rlv_name_i)
# ** Kooficeints:
# обсяг тепла на функц. системи = 5% якщо є погодне регулювання в ІТП або 15% якщо не має від
# при значение 0 переменая не используется
gk_Qfun_sys = 0.05
# gk_Qfun_sys = 0
# обсяг тепла на опалення МЗК = 10% від
# при значение 0 переменая не используется
gk_Qmzk = 0.1
# gk_Qmzk = 0
# Мінімальна частка середнього питомого споживання
gk_Qop_min = 0.5
# Обсяг споживання тепла приміщенням без розподілювачів
# k = 2, якщо площа необладнаних приміщень менще 25% та 1,5 якщо більше
qk_k_no_surge_proc    = 0.25
qk_k_no_surge_if_more = 1.5
qk_k_no_surge_if_less = 2
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
# gs_recalc_surcharge_print_result = True
gs_recalc_surcharge_print = False
# gs_recalc_surcharge_print = True
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
gl_num_column = 0
# 1 № квартири	
gl_app_num_column = 1
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
# ** report names:
gv_osbb_report = "ОСББ"
# ** osbb report setings:
gv_osbb_report = "ОСББ"
gv_enable_full_report = False
# gv_enable_full_report = True
# 0 № п/п	
gn_num_column = "№ п/п"
# 1 № квартири	
gn_app_num_column = "№ квартири"
# 2 Ітого по распр., Гкал
gn_total_couter_e_column = "Ітого по распр., Гкал"
# 3 Ітого по м2, Гкал
gn_total_no_couter_e_column = "Ітого по м2, Гкал"
# 4 функціонування системи
gn_func_sys_column = "функціонування системи"
# 5 МЗК
gn_mzk_column = "МЗК"
# 6 ВСЬОГО, Гкал
gn_total_e_column = "ВСЬОГО, Гкал"
# ** Теплоенрго report setings:
gv_TE_report_formar_len = 3
gv_TE_report = "Теплоенрго"
# 0 Особовий рахунок	
gn_TE_num_column = "Особовий рахунок"
# 1 № Адреса	
gn_TE_adders_column = "Адреса"
# 2 № віртуального ліч-ка
gn_TE_num_virt_column = "№ віртуального ліч-ка"
# 3 Період
gn_TE_period = "Період"
# 4 Обсяг споживання,  Гкал
gn_TE_total_e_column = "Обсяг споживання,  Гкал"
# ** Rules list:
gr_rule_sheet_name = "rules"
gr_rule_sheet_enable_in_report = False
gr_rule_tag = "rule"
gr_rule_name_col = 1
gr_rule_len_col = 2
gr_rule_params_start_col = 3
# * -------------------------------------------:
