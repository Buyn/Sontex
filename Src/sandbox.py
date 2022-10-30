# ----------------------------------------------
# * import : 
# ----------------------------------------------
# import pandas as pd
# import math
import sys


# ----------------------------------------------
# * vars : 
# ----------------------------------------------


# ----------------------------------------------
# * main :
# ----------------------------------------------

import sys
import pandas as pd
from global_values import *
from appart_values import *
df = pd.read_excel(filename,
                  sheet_name = sheet_name,
                  engine='openpyxl',
                  # index_col=0,
                  header=None,
                  )
al = cl =[]
print(al)
app = Appart_values(df, 1)
al.append(app)
print(al)
app = Appart_values(df, 2)
al.append(app)
print(al)


# ----------------------------------------------
# * -------------------------------------------:
