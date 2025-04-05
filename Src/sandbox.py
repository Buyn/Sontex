import pandas as pd
from global_values import *

# print("test hi!")
# filename = "/home/buyn/Dev/Python/Sontex/Src/Data_files/test.rlv"
filename = "Data_files/test.rlv"
# colmname1 = "Readout date"
# gv_rlv_name_date
# gv_rlv_Readout_date = "Readout date"
gv_rlv_name_start = 1
gv_rlv_name_end = 100
# gv_rlv_name_date_list = [gv_rlv_name_date + str(x)
#                               for x in range(
#                                   gv_rlv_name_start,
#                                   gv_rlv_name_end)]
# gv_rlv_colmus_list = [gv_rlv_Readout_date].append(gv_rlv_name_date_list)
gv_rlv_colums_name_dates_list = ["Readout date"] + [gv_rlv_name_date + str(x)
                              for x in range(gv_rlv_name_start, gv_rlv_name_end)]
gv_rlv_colums_name_values_list = ["Heating units totalizer"] + [gv_rlv_name_value + str(x)
                              for x in range(gv_rlv_name_start, gv_rlv_name_end)]

df = pd.read_csv(filename ,
                encoding = gv_rlv_encoding,
                header = gv_rlv_header,
                sep = gv_rlv_sep,
                index_col = gv_rlv_index_col)

def get_dates_from_colums_list(df, colist):
  retlist = []
  for i, name in enumerate(colist):
      try:
          colnum = df.columns.get_loc(name)
      except Exception as e:
          print ("on name=", name, " is Exception=", str(e))
          print("Possible reason - file does not contain the expected columns")
          break
      value = df.iloc[0, colnum]
      if pd.isnull(value): break
      retlist.append(value)
  return retlist


print(get_dates_from_colums_list(df, gv_rlv_colums_name_dates_list))

def get_df_from_filename_string(string):
  rdf=[]
  for path_csv in string.split(";"):
    if path_csv=="": continue
    # wm.print_to_log("завантажуємо файл: "+path_csv)
    rdf.append(load_db(path_csv))
  return rdf

df_list = get_df_from_filename_string(filename)
if not len(df_list)==0:
  print(get_dates_from_colums_list(df_list[0], gv_rlv_colums_name_dates_list))

# print(r)
# print(df.iloc[1, 0])
# print(df.iloc[0, 0])

# print(df.iloc[1, 1])
# print(df.iloc[0, 1])
# print(df.iloc[0, 2])
# print(df.iloc[0])
# print(df)
