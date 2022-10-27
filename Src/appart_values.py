# ----------------------------------------------
# * imports : 
# ----------------------------------------------


# ----------------------------------------------
# * vars :
# ----------------------------------------------


# ----------------------------------------------
# * class Appart_values :
# ** -------------------------------------------:
class Appart_values:
# ** def __init__ : 
#  --------------------------------------------:
    def __init__(self, df, stat_line): 
        self._df = df
        self._stat_line = stat_line


# ** get_next_appindex : 
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


#  ----------------------------------------------:
#  ----------------------------------------------:



# * -------------------------------------------:
