import pandas as pd
from global_values import *

class Counter_values:

    def __init__(self, df, line): 
        self._df = df
        self._line = line
        self.adress = self.get_adress()
        if not self.is_valid(): return 
        self.value1 = self.get_value1()
        self.value2 = self.get_value2()
        self.k_priv = self.get_k_priv()

    def get_adress(self): 
        return self._df.iloc[self._line, gl_counters_column]

    def get_value1(self): 
        return self.get_value(gl_counters_value1_column, "gl_counters_value1_column")

    def set_value1(self, value): 
        return self.set_value(gl_counters_value1_column, "gl_counters_value1_column", value)

    def set_value2(self, value): 
        return self.set_value(gl_counters_value2_column, "gl_counters_value2_column", value)

    def get_value2(self): 
        return self.get_value(gl_counters_value2_column, "gl_counters_value2_column")

    def get_k_priv(self): 
        return self.get_value(gl_counters_k_priv_column, "gl_counters_k_priv_column")

    def gen_delta(self): 
        # споживання за період
        return  self.value1 - self.value2

    def gen_delta_k(self): 
        # споживання за період приведене
        return  self.gen_delta() * self.k_priv

    def get_value(self, row, name): 
        r = self._df.iloc[self._line, row]
        if not isinstance(r, float) and not isinstance(r, int):
            raise NameError('not int or float on line = ' + str(self._line + gl_exl_shift_rows) + ', for column ' + name)
        if pd.isna(r):
            raise NameError('no value on line = ' + str(self._line + gl_exl_shift_rows) + ', for column ' + name)
        return r

    def set_value(self, row, name, value): 
        r = self._df.iloc[self._line, row,] = value
        return r

    def is_valid(self): 
        return  isinstance(self.adress, int)
