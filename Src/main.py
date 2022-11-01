# ----------------------------------------------
# * imports : 
# ----------------------------------------------
import sys
import pandas as pd
from global_values import *
from appart_values import *


# ----------------------------------------------
# * vars :
# ----------------------------------------------


# ----------------------------------------------
# * def main(argv):
# ----------------------------------------------
def main(argv):
    cmd_line_arg(argv)
    df = load_exel(filename, sheet_name)
    app_list, couters_list = populate_apps(df) 
    end_app(0)


# ----------------------------------------------
# * main functions :
# ----------------------------------------------
# ** cmd_line_arg :
def cmd_line_arg(argv):
    # for arg in sys.argv[1:]:
    #     # print("arg = ", arg) 
    #     if arg.startswith("-"):
    #         if arg.find("f") != -1:
    #           print("mindmap set to True", arg) 
    #           mindmap = True
    #         if arg.find("r") != -1:
    #           print("rooting no using", arg) 
    #           root = True
    #         if arg.find("h") != -1:
    #           print(helptext) 
    #           sys.exit()
    #     else:
    #         if arg.find("\\") != -1:
    #             print("is windows path")
    #             arg = arg.replace("\\", "/")
    #         if not os.path.exists(arg):
    #             print("File not exists: ", arg)
    #             sys.exit()
    #         # print("file found")
    #         filename = arg
    return True


# ** def load_exel : 
def load_exel(filename, sheet_name): 
    df = pd.read_excel(filename,
                      sheet_name = sheet_name,
                      engine='openpyxl',
                      # index_col=0,
                      header=None,
                      )
    # df = pd.read_excel(filename, sheet_name = "показники", engine='openpyxl')
    # df = pd.read_excel(filename,
    #                    sheet_name = "показники",
    #                    engine='openpyxl')
    # df = pd.read_excel(filename,
    #                    sheet_name = "показники",
    #                    engine='openpyxl',
    #                    index_col=0)
    return df


# ** end_app(arg) : 
def end_app(arg):
    sys.exit(arg)

    
# ** def populate_apps : 
def populate_apps(df): 
    al =[]
    cl =[]
    app_line = gl_ferst_app_colmn
    while True:
        app = Appart_values(df, app_line)
        app_line = app.next_app_line
        al.append(app)
        cl.append(app.counters_list)
        if app.is_last:
            break
    return al, cl


# ** ------------------------------------------:
# * if __name__ : 
# ----------------------------------------------
if __name__ == "__main__": 
    import sys
    # sys.argv = ['', 'Test.testName']
    main(sys.argv)


# ----------------------------------------------
# * -------------------------------------------:
