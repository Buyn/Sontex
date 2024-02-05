import pandas as pd

def load_exel(filename, sheet_name): 
    df = pd.read_excel(filename,
                      sheet_name = sheet_name,
                      engine='openpyxl',
                      # index_col=0,
                      header=None,
                      )
    return df

gv_filename = "Data_files/test.xlsx"
sheet_name = "rules"

df = load_exel(gv_filename, sheet_name)
print(df)

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


# print (get_all_rules_index(df))

def postproc_test(arg):
    print(arg)

# postproc_test ([1, 2 ,3])

rules_dic = {
    "test" : postproc_test
}

def use_rule(index, rule_name, rule_params):
    try:
        # print(rules_dic[rule_name])
        rules_dic[rule_name](rule_params)
    except Exception:
        print("no such rule in dictionary from row=",index, " ", rule_name)


use_rule(1, "test", (1,2,3))
use_rule(2, "test_no", (1,2,3))

        


