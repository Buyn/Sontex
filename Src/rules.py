# ----------------------------------------------
# * imports : 
# ----------------------------------------------
import pandas as pd
from global_values import *


# ----------------------------------------------
# * Postprocessing functions :
# ----------------------------------------------
# **  def postproc_test:
def postproc_test(df, arg):
    if arg[0]!="test":
        print(arg)
    return arg


# **  def postproc_divider:
def postproc_divider(df, arg):
    if arg[0]!="test":
        print(arg)
    return arg


# ** ------------------------------------------:
# * vars :
# ----------------------------------------------
rules_dic = {
    "test" : postproc_test,
    "post_divider" : postproc_divider,
}


# ----------------------------------------------
# * functions :
# ----------------------------------------------
# **  get_all_rules_index:
def get_all_rules_index(df):
    r = []
    for i in range(0, df.shape[0]):
        # print("i = ", i)
        value_i = df.iloc[i, 0]
        if df.iloc[i, 0] == "rule":
            # print("rule found on index = ", i)
            # print("value of i = ", df.iloc[i, 0])
            ruls_name = df.iloc[i, 1]
            ruls_params = df.iloc[i, 2]
            ruls_params_list =[df.iloc[i, p] for p in range(3, 3 + ruls_params)]
            r.append((i, ruls_name, ruls_params_list))
    return r


# **  use_rule:
def use_rule(df, index, rule_name, rule_params, test = False):
    try:
        return rules_dic[rule_name](df, rule_params)
    except Exception:
        if not test:
            print("no such rule in dictionary from row=",index, " ", rule_name)
        return None


# ** ------------------------------------------:
# * -------------------------------------------:
