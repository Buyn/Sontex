# ----------------------------------------------
# * imports : 
# ----------------------------------------------
import pandas as pd
from global_values import *


# ----------------------------------------------
# * class Counter_values :
# ** ------------------------------------------:
class Counter_values:


# ** def __init__ : 
    def __init__(self, df, line): 
        self._df = df
        self._line = line
        self.adress = self.get_adress()
        self.value1 = self.get_value1()
        self.value2 = self.get_value2()

        
# ** def get_adress : 
    def get_adress(self): 
        return self._df.iloc[self._line, gl_counters_row]


# ** def get_value1 : 
    def get_value1(self): 
        return self._df.iloc[self._line, gl_counters_value1_raw]


# ** def get_value2 : 
    def get_value2(self): 
        return self._df.iloc[self._line, gl_counters_value2_raw]


# ** def is_valid : 
    def is_valid(self): 
        return  isinstance(self.adress, int)


# * -------------------------------------------:
