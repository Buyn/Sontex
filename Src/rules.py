import pandas as pd
from global_values import *

# **  def postproc_test:
def postproc_test(df, arg):
    if arg[0]!="test":
        print(arg)
    return df, arg


# **  def postproc_divider:
def postproc_divider(df:pd.DataFrame, arg):
    # print("arg = ", arg)
    # print("arg = ", arg[2])
    strarg = arg[2].split("\"")
    # print("strarg = ", strarg)
    newrow = [i for i in strarg if i and i != " "]
    # print("newrow = ", newrow)
    # print(df.shape)
    if df.shape[1] > len(newrow):
        for col in range(df.shape[1] - len(newrow)):
            newrow.append("")
    # print(arg[0])
    # print(df[df[0]==arg[0]])
    target_index = int((df[df[0]==arg[0]].index.values)[0])
    # tmp_int = df[df[0]==arg[0]].index.values
    # print("tmp_int =", tmp_int)
    # print("(int(tmp_int)) = ", int(tmp_int))
    # target_index = int(tmp_int)
    # print("index.values = ", target_index)
    target_value = df.iloc[target_index, arg[1]-1]
    # print("target_value = ", target_value)
    value_k = arg[3]
    # print("value_k = ", value_k)
    new_value = float(target_value) * float(value_k)
    df.iloc[target_index, arg[1]-1] = float( gv_TE_report_formar_len( target_value - new_value))
    # print(df.iloc[target_index, arg[1]-1])
    newrow[arg[1]-1] = float( gv_TE_report_formar_len( new_value))
    newrow[2] = newrow[0]
    # newrow[arg[1]-3] = 
    # print(arg)
    # print(arg[3])
    # print(arg[5])
    # print(newrow[arg[1]-4])
    # print(len(newrow))
    # print(newrow)
    # print(newrow[2])
    # print(len(newrow))
    # print(df)
    #  Inserting the new row
    # Inserting a Row at a Specific Index
    df.loc[target_index + 0.5] = newrow
    # print(target_index + 0.5)
    #  Reset the index
    df = df.sort_index().reset_index(drop=True)
    # print(df)
    return df, newrow


# ** ------------------------------------------:
# * vars:
# ----------------------------------------------
rules_dic = {
    "test" : postproc_test,
    "post_divider" : postproc_divider,
}

# **  get_all_rules:
def get_all_rules(df):
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
            print("no such rule in dictionary from row=",index+1, " ", rule_name)
            # wm.print_to_log("немає такого правила у словнику з row="+ index+1+ " "+ rule_name)
        return df, None

# **  postprocessing_df_with_rules_df:
def postprocessing_df_with_rules_df(df, df_rules):
    rules_list = get_all_rules(df_rules)
    if not rules_list: return df
    for rule in rules_list: 
        df, args = use_rule(df = df,
                            index = rule[0],
                            rule_name = rule[1],
                            rule_params = rule[2],)
    return df
