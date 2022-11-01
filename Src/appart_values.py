# ----------------------------------------------
# * imports : 
# ----------------------------------------------
import pandas as pd
from global_values import *
from counter_values import *


# ----------------------------------------------
# * class Appart_values :
# ** ------------------------------------------:
class Appart_values:
# ** def __init__ : 
#  --------------------------------------------:
    def __init__(self, df, start_line): 
        self._df = df
        if not self.is_starting_line(start_line):
          raise NameError('no appart start on line = ' + start)
        self._start_line = start_line
        self.next_app_line, self.is_last = self.get_next_appindex(self._start_line)
        self.counters_list = self.get_counters_list(
                                    self._start_line,
                                    self.next_app_line)  

        
# ** def get_counters_list : 
    def get_counters_list(self, start, end): 
        r = []
        # Count to end-1,
        # but end it start of next app
        # as resul too getits end of this app
        # it = end-1 => we use =end
        for i in range(start, end):
            value = self.get_counter(i)
            # print("value=", value)
            # if not isinstance(value, int):
            if not value.is_valid():
                if not r ==[]:
                    raise NameError('not int in counter cell on line ' + str(i) + ', in app start = ' + str(start))
                return None
            r.append(value) 
        return r
            
 
# ** def get_counter : 
    def get_counter(self, line): 
        return Counter_values(self._df, line)
        # return self._df.iloc[line, gl_counters_row]


# ** def is_starting_line : 
    def is_starting_line(self, line): 
        return isinstance(self._df.iloc[line, 0], int)


# ** get_next_appindex : 
    def get_next_appindex(self, last):
        for i in range(last + 1, last + 10):
            # print("i = ", i)
            value_i = self._df.iloc[i, 0]
            if value_i == "end":
                # print("found end of list = ", i)
                # print("value of i = ", self._df.iloc[i, 0])
                return i, True
            if not pd.isna(value_i):
                # print("found i = ", i)
                # print("value of i = ", self._df.iloc[i, 0])
                return i, False
            # print("nan continur ... ")
            continue
        return -1,None


#  ----------------------------------------------:
#  ----------------------------------------------:




# ** def gen_counters_adres : 
    def gen_counters_adress(self): 
        return [x.adress for x in self.counters_list] if self.counters_list else None


# ** def load_values : 
    def load_values(self): 
        pass


# * -------------------------------------------:
