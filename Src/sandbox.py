# * import : 
import pandas as pd
# import math

# * vars : 
# ** one liner:
filename = "Data_files/metod01.xlsx"
# sheet_name = "показники"
sheet_name = "квартири, площі"
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
# * read_excel : 
# df = pd.read_excel(filename, sheet_name = "показники", engine='openpyxl')
# df = pd.read_excel(filename,
#                    sheet_name = "показники",
#                    engine='openpyxl')
# df = pd.read_excel(filename,
#                    sheet_name = "показники",
#                    engine='openpyxl',
#                    index_col=0)
df = pd.read_excel(filename,
                   sheet_name = sheet_name,
                   engine='openpyxl',
                   # index_col=0,
                   header=None,
                   )
# * print : 
#view the first five rows: 
# print (df.head())
# print (df[1])
# print (df["A"])
# print(df.iloc[:, 0])
# df.head()
# print(df.index)
# print(df["Radio address"])
# print(df.iloc[0:5, 0:2])
print(df.iloc[101, 0])
print(df.iloc[102, 0])
print(df.iloc[103, 0])
print(df.iloc[104, 0])
# print(df.index)
# print(df.columns)

# print(df.index[df.iloc[7] == 2].tolist())
# print(df.index[df.iloc[:, 0] == 2].tolist())
# print(df.index[df.iloc[:, 0] == 1])
# print(df.index[df.iloc[:, 0] == 2])
# print(df.index[df.iloc[:, 0] == 3])
# print(df.index[df.iloc[:, 0] == 10])
# print(df.loc["25482311.0", ["Radio address"]])
# print(df.A)
# print(df.loc[])
# writer = pd.ExcelWriter('output.xlsx', engine='openpyxl')
# df.to_excel(writer
#             # , index=False
#             )
# workbook = writer.bookworksheet = writer.sheets['report']
# header_fmt = workbook.add_format({'bold': True})
# worksheet.set_row(0, None, header_fmt)
# writer.save()


# df.to_excel('output.xlsx')

# print (df)
# * get_next_appindex : 
def get_next_appindex(last):
    for i in range(last + 1, last + 10):
        # print("i = ", i)
        value_i = df.iloc[i, 0]
        if value_i == "end":
          print("found end of list = ", i)
          print("valut of i = ", df.iloc[i, 0])
          return i, True
        if not pd.isna(value_i):
          print("found i = ", i)
          print("valut of i = ", df.iloc[i, 0])
          return i, False
        # print("nan continur ... ")
        continue
    return False 

# last_app = 101
last_app = 100
next_app, end_app = get_next_appindex(last_app)
print("next is = ", next_app)
print("next value", df.iloc[next_app, 0])
print("naber of counters = ", next_app - last_app)
if end_app:
    print("end of list")
#  ----------------------------------------------:
# * class Appart :
class Appart:
# ** def __init__ : 
#  ----------------------------------------------:
    def __init__(self, app_num, num_of_counters): 
        self.app_num = app_num
        self.num_of_counters = num_of_counters


#  ----------------------------------------------:



