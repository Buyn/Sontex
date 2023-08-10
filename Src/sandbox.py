# ----------------------------------------------
# * import : 
# ----------------------------------------------
from random import randint  
import pandas as pd
# from global_values import *

# ----------------------------------------------
# * vars : 
# ----------------------------------------------


# ----------------------------------------------
# * main :
# ----------------------------------------------
# Creating the first Dataframe using dictionary
# df1 = df = pd.DataFrame({"a":[1, 2, 3, 4],
#                          "b":[5, 6, 7, 8]})
# df1 = [[1,2,3],
#        [11,22,33]
#        ] 
df1 = []
df1.append([1,2,3])
df1.append([11,22,33])
# Creating the Second Dataframe using dictionary
# df2 = pd.DataFrame({"a":[1, 2, 3],
#                     "b":[5, 6, 7]})

# list_row = ["Hyperion", 27000, "60days", 2000]
# df2.loc[len(df)] = list_row
  
# Print df1
print(df1, "\n")
df2 = pd.DataFrame(df1)

  
# Print df2
# df2
print(df2, "\n")
# # df2.concat(pd.DataFrame([11, 12, 13]))
# df2.loc[len(df2)] = [11, 12, 13]
# print(df2, "\n")
# ----------------------------------------------
# * -------------------------------------------:
