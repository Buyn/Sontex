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
    filename = gv_filename
    sheet_name = gv_sheet_name 
    filename, sheet_name = cmd_line_arg(argv, filename, sheet_name)
    df = load_exel(filename, sheet_name)
    app_list, couters_list = populate_apps(df) 
    # загальна площа будинку
    sum_heated_area = gen_sum_heated_area(app_list)
    last_app_line = get_last_app_line(app_list)
    # по будинку за т/ліч
    delta_value_home_counter = gen_delta_value_home_counter(df, last_app_line)
    # найбільш показник розподілювачів серед приміщень приведена до 1 м2 площі
    index_most_heated_app = find_most_heated_app(app_list)
    # Питомий обсяг спожитої енергії на опалення усіх приміщень
    q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
    # питомий обсяг енергії спожитий одним розподілювачем
    q_pit_roz = gen_Qpit_roz(app_list, q_roz, index_most_heated_app)
    q_op_min = gen_Qop_min(q_roz)
    calc_on_globals_for_couters(app_list, q_pit_roz, q_op_min)
    end_app(0)


# ----------------------------------------------
# * main functions :
# ----------------------------------------------
# ** cmd_line_arg :
def cmd_line_arg(argv, filename, sheet_name):
    # global filename, sheet_name
    # print(argv)
    for arg in argv[1:]:
        if arg.startswith("--filename="):
            filename = arg.split("=")[1]
        if arg.startswith("--sheet_name="):
            sheet_name = arg.split("=")[1]
        # else:
        #     if arg.find("\\") != -1:
        #         print("is windows path")
        #         arg = arg.replace("\\", "/")
        #     if not os.path.exists(arg):
        #         print("File not exists: ", arg)
        #         sys.exit()
        #     # print("file found")
        #     gv_filename = arg
    return filename, sheet_name


# ** def load_exel : 
def load_exel(filename, sheet_name): 
    df = pd.read_excel(filename,
                      sheet_name = sheet_name,
                      engine='openpyxl',
                      # index_col=0,
                      header=None,
                      )
    # df = pd.read_excel(gv_filename, gv_sheet_name = "показники", engine='openpyxl')
    # df = pd.read_excel(gv_filename,
    #                    gv_sheet_name = "показники",
    #                    engine='openpyxl')
    # df = pd.read_excel(gv_filename,
    #                    gv_sheet_name = "показники",
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
    app_line = gl_ferst_app_row
    while True:
        app = Appart_values(df, app_line)
        app_line = app.next_app_line
        al.append(app)
        # cl.append(app.counters_list)
        cl.append(app.gen_counters_adress())
        if app.is_last:
            break
    return al, cl


# ** def gen_sum_heated_area :
def gen_sum_heated_area(apps): 
    # загальна площа будинку
    return sum([app.heating_area for app in apps])


# ** def gen_sum_area :
def gen_sum_area(apps): 
    # загальна площа будинку
    return sum([app.sum_area for app in apps])


# ** def get_last_app_line : 
def get_last_app_line(apps): 
    if apps[-1].is_last :
      return apps[-1].next_app_line
    else:
      raise NameError(
          'get_last_line in not last appart ' + str(len(apps)))


# ** def get_home_value : 
def get_home_value(df, line, column):
    # r =  float(df.iloc[line, column])
    r =  df.iloc[line, column]
    # print("value = ", r)
    if not isinstance(r, float) and not isinstance(r, int):
        raise NameError('in get_home_value not int or float on line = ' + str(line + gl_exl_shift_rows) + ', for column ' + str(column))
    if pd.isna(r):
        raise NameError('no value on line = ' + str(line + gl_exl_shift_rows) + ', for column ' + str(column))
    return r
    

# ** def gen_delta_value_home_counter : 
def gen_delta_value_home_counter(df, g_line): 
    return get_home_value(df,
                g_line + gl_shift_home_counter_value1,
                gl_column_home_counter_value1) - get_home_value(df,
                    g_line + gl_shift_home_counter_value2,
                    gl_column_home_counter_value2)
    

# ** def find_most_heated_app : 
def find_most_heated_app(apps): 
    # найбільш показник розподілювачів серед приміщень приведена до 1 м2 площі
    r = [app.gen_k_to_s() for app in apps]
    return r.index(max(r))




# ** def gen_Qfun_sys : 
def gen_Qfun_sys(delta_value_home_counter): 
    # обсяг тепла на функц. системи = 5% якщо є погодне регулювання в ІТП або 15% якщо не має від
    return delta_value_home_counter * gk_Qfun_sys


# ** def gen_Qmzk : 
def gen_Qmzk(delta_value_home_counter): 
    # обсяг тепла на опалення МЗК = 10% від
    return delta_value_home_counter * gk_Qmzk


# ** def gen_Qroz : 
def gen_Qroz(delta_value_home_counter, sum_heated_area): 
    # Питомий обсяг спожитої енергії на опалення усіх приміщень
    return (delta_value_home_counter
            - gen_Qfun_sys(delta_value_home_counter)
            - gen_Qmzk(delta_value_home_counter)) / sum_heated_area


# ** def gen_Qmax_roz : 
def gen_Qmax_roz(app_list, q_roz, index_most_heated_app): 
    # Обсяг споживання тепла з найбільшим показником по розподілювачам
    return q_roz * app_list[index_most_heated_app].heating_area


# ** def gen_Qop_min : 
def gen_Qop_min(q_roz): 
    # Мінімальна частка середнього питомого споживання
    # gk_Qop_min_after_point
    # количество знаков после запятой для этой переменой
    # при повышение точности в этой переменой разница силльно растёт
    # False для максимальной точности
    # True для
    # 3 значения соответствуюшее екселю
    r = gk_Qop_min * q_roz
    if gk_Qop_min_after_point:
        r = float("{:.3f}".format(r))
    return r

# ** def gen_Qpit_roz : 
def gen_Qpit_roz(app_list, q_roz, index_most_heated_app): 
    return gen_Qmax_roz(app_list, q_roz, index_most_heated_app) / app_list[index_most_heated_app].gen_E_used_k()

      
# ** def calc_on_globals_for_couters : 
def calc_on_globals_for_couters(app_list, q_pit_roz, q_op_min): 
    for i, app in enumerate(app_list):
        # if app.counters_list:
        # print("in ", app_list[i]._start_line )
        # print("index ", i)
        app_list[i].gen_surcharge(q_pit_roz, q_op_min)
        # print("value of 0 ", app_list[0].surcharge)
    return app_list


# ** ------------------------------------------:
# * if __name__ : 
# ----------------------------------------------
if __name__ == "__main__": 
    import sys
    # sys.argv = ['', 'Test.testName']
    main(sys.argv)


# ----------------------------------------------
# * -------------------------------------------:
