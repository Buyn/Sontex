# ----------------------------------------------
# * imports : 
# ----------------------------------------------


# ----------------------------------------------
# * vars :
# ----------------------------------------------
# ** one liner:
filename = "Data_files/metod01.xlsx"
# sheet_name = "показники"
sheet_name = "квартири, площі"
# ** exel coordinats:
gl_counters_row = 6 # номер колонки (№ розподілювача)
gl_counters_value1_raw = 17 # номер колонки (показники на 01.12)
gl_counters_value2_raw = 18 # номер колонки (показники на 01.11)
gl_ferst_app_colmn = 1 # номер ряда первого апартамента
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
