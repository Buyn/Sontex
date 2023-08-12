# ----------------------------------------------
# * import : 
# ----------------------------------------------
import pandas as pd
# from global_values import *

# ----------------------------------------------
# * vars : 
# ----------------------------------------------
# filename = "Data_files/test.rlv"
gv_rlv = "Data_files/test.rlv"
filename = gv_rlv
# gv_rlv_encoding = "cp1252"
gv_rlv_encoding = "1252"
gv_rlv_header   = 1
gv_rlv_index_col= 5
gv_rlv_sep      = "\t"
# gv_rlv_sep      = "	"
# gv_rlv_sep      = ""
gv_rlv_name_i   = 1
gv_rlv_name_date= "Historic date - "
gv_rlv_name_value="Historic value - "

# ----------------------------------------------
# * main :
# ----------------------------------------------
# import os
print("Start loading rlv")
df = pd.read_csv(filename ,
                encoding = "utf-16le",
                # encoding="latin1",
                # encoding = "RFC-4180",
                # encoding = "cp1252",
                # encoding = "utf-8",
                header = 1,
                # sep = ";",
                sep = "\t",
                # sep = "\x09\x00",
                # sep = " ",
                # engine="python",  # 
                # sep='\t', lineterminator = '\n', engine='c', keep_default_na=False
                 # engine = 'python-fwf',
                # lineterminator = os.linesep,
                # lineterminator='\r\n',
                # lineterminator='\x0D\x0A',
                # lineterminator='\x0A',
                # lineterminator='\n',
                index_col = 5
                 )
print("end rlv load")
# print("df = ", df)
# counter.value1 = int(df.loc[ser_id , name_value])
# name_value = gv_csv_name_value + str(gv_csv_name_i)
name_value = gv_rlv_name_value + str(gv_rlv_name_i)
# value1 = df.loc[1 , name_value]
# print(df.head())
# print(df.index)
# print (df[1])
# print(df.iloc[1, 1])
# print(df.iloc[:, 0])
# print(df.columns)
# print(df["Radio address"])
# value1 = df.loc[1 , 3]
# ser_id = counter.adress
# ----------------------------------------------
# * -------------------------------------------:
