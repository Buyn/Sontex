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
        self.sum_area, self.heating_area = self.load_values()
        self.surcharge = None

        
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
        # return self._df.iloc[line, gl_counters_column]


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




# ** def gen_counters_adress : 
    def gen_counters_adress(self): 
        return [x.adress for x in self.counters_list] if self.counters_list else None


# ** def load_values : 
    def load_values(self): 
        rows =  [ gl_app_sum_area_column,
                  gl_app_heating_area_column]
        names = [ "gl_app_sum_area_column",
                  "gl_app_heating_area_column"]
        sr=[]
        for i, row in enumerate(rows):
            r = self._df.iloc[self._start_line, row]
            if not isinstance(r, float) and not isinstance(r, int):
                raise NameError('not int or float on line = ' + str(self._start_line) + ', for rows ' + names[i])
            if pd.isna(r):
                raise NameError('no value on line = ' + str(self._start_line) + ', for rows ' + names[i])
            sr.append(r)
        return tuple(sr)


# ** def gen_E_used : 
    def gen_E_used(self): 
        # сумарне споживання по квартирі, од.
        if not self.counters_list: return 0
        return  sum([x.gen_delta() for x in self.counters_list])


# ** def gen_E_used_k :
    def gen_E_used_k(self): 
        # сумарне приведене споживання по квартирі, од.
        if not self.counters_list: return 0
        return sum([x.gen_delta_k() for x in self.counters_list])


# ** def gen_k_to_s :
    def gen_k_to_s(self): 
        # приведене до м2 площі, од/м2
        if not self.counters_list: return 0
        return self.gen_E_used_k() / self.heating_area


# ** def gen_use_for_period : 
    def gen_use_for_period(self, q_pit_roz): 
        # обсяг споживання за період, Гкал
        self.specified_used_E = q_pit_roz * self.gen_E_used_k()
        return self.specified_used_E


# ** def gen_priv2S : 
    def gen_priv2S(self, q_pit_roz): 
        # приведене до м2 площі, Гкал/м2
        return self.gen_use_for_period(q_pit_roz) / self.heating_area


# ** def gen_surcharge : 
    def gen_surcharge(self, q_pit_roz, q_op_min): 
        # донарахування, Гкал
        self.surcharge = 0
        if not self.counters_list: return self.surcharge
        priv2S = self.gen_priv2S(q_pit_roz)
        if priv2S < q_op_min:
            self.surcharge = (q_op_min - priv2S) * self.heating_area
        return self.surcharge


# ** def get_S_if_surcharge : 
    def get_S_if_surcharge(self): 
        # логіка, не міняти! (площа повернення)
        return self.heating_area if self.surcharge == 0 else 0


# ** def gen_specified_used_E: 
    def gen_specified_used_E(self, e_for_redistibut): 
        # Ітого по распр., Гкал
        if not self.counters_list: return 0
        # self.specified_used_E = self.surcharge + self.gen_use_for_period(q_pit_roz) - self.get_S_if_surcharge() * e_for_redistibut
        self.specified_used_E = self.surcharge + self.specified_used_E - self.get_S_if_surcharge() * e_for_redistibut
        return self.specified_used_E


# ** def gen_specified_priv2S : 
    def gen_specified_priv2S(self): 
        # уточнене приведене до м2 площі, Гкал/м2
        if not self.counters_list: return 0
        return self.specified_used_E / self.heating_area


# ** def gen_specified_surcharge : 
    def gen_specified_surcharge(self, q_op_min): 
        # уточнене донарахування, Гкал
        self.surcharge = 0
        if not self.counters_list: return self.surcharge
        priv2S = self.gen_specified_priv2S()
        if priv2S < q_op_min:
            # print("priv2S in = ", priv2S)
            # print("q_op_min in =", q_op_min)
            self.surcharge = (q_op_min - priv2S) * self.heating_area
        return self.surcharge


# ** def gen_no_counter_e : 
    def gen_no_counter_e(self, q_no_surge): 
        self.specified_used_E = q_no_surge * self.heating_area
        return self.specified_used_E


# ** def gen_total_qfun_sys : 
    def gen_total_fun_sys(self, s_qfun_sys): 
        # функціонування системи
        self.total_fun_sys = s_qfun_sys * self.heating_area
        return self.total_fun_sys


# ** def gen_total_Mkz : 
    def gen_total_Mkz(self, s_q_Mkz): 
        # МЗК
        self.total_Mkz = s_q_Mkz * self.heating_area
        return self.total_Mkz


# ** def gen_total_e : 
    def gen_total_e(self): 
        # ВСЬОГО, Гкал
        self.total_e = self.specified_used_E + self.total_fun_sys + self.total_Mkz
        return self.total_e


# * -------------------------------------------:
