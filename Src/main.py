# ----------------------------------------------
# * imports : 
# ----------------------------------------------
import sys
import pandas as pd
import global_values
import appart_values


# ----------------------------------------------
# * vars :
# ----------------------------------------------


# ----------------------------------------------
# * main :
# ----------------------------------------------
# ** def main(argv):
def main(argv):
    cmd_line_arg(argv)
    df = load_exel(filename, sheet_name)


# ** cmd_line_arg :
def cmd_line_arg(argv):
    return True


# ** def load_exel : 
def load_exel(filename, sheet_name): 
    # df = pd.read_excel(filename,
    #                   sheet_name = sheet_name,
    #                   engine='openpyxl',
    #                   # index_col=0,
    #                   header=None,
    #                   )
    df = 1
    # df = pd.read_excel(filename, sheet_name = "показники", engine='openpyxl')
    # df = pd.read_excel(filename,
    #                    sheet_name = "показники",
    #                    engine='openpyxl')
    # df = pd.read_excel(filename,
    #                    sheet_name = "показники",
    #                    engine='openpyxl',
    #                    index_col=0)
    return df
    # pass


# ----------------------------------------------
# * if __name__ : 
# ----------------------------------------------
if __name__ == "__main__": 
    import sys
    # sys.argv = ['', 'Test.testName']
    main(sys.argv)


# ----------------------------------------------
# * -------------------------------------------:
