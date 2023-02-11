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
g_filename = gv_filename
g_output = gv_output
g_sheet_name = gv_sheet_name
g_csv = gv_csv


# ----------------------------------------------
# * def main(argv):
# ----------------------------------------------
def main(argv):
    filename, csv, sheet_name = cmd_line_arg(argv)
    sheet_name = g_sheet_name 
    filename = g_filename
    output = g_output
    csv = g_csv
    df = load_exel(filename, sheet_name)
    app_list, couters_list = populate_apps(df) 
    app_list = calc_all_values_in_apps( df, app_list)
    df_report = load_exel(filename, gv_sheet_report)
    df_report = set_to_report(df_report, app_list)
    save_data_frame(output, df, df_report)
    end_app(0)


# ----------------------------------------------
# * main functions :
# ----------------------------------------------
# ** cmd_line_arg :
def cmd_line_arg(argv):
    global g_filename, g_csv, g_output
    # print(argv)
    for arg in argv[1:]:
        if arg.startswith("--filename="):
            g_filename = arg.split("=")[1]
        if arg.startswith("--csv="):
            g_csv = arg.split("=")[1]
        if arg.startswith("--output="):
            g_output = arg.split("=")[1]
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
    return g_filename, g_csv, g_output


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
        cl.append(app.gen_counters_adress())
        if app.is_last:
            break
    return al, cl


# ** def gen_sum_heated_area :
def gen_sum_heated_area(apps): 
    # Площа опалювальна по КТЕ
    return sum([app.heating_area for app in apps])


# ** def gen_sum_area :
def gen_sum_area(apps): 
    # загальна площа будинку
    return sum([app.sum_area for app in apps])


# ** def sum_E_used_k :
def sum_E_used_k(apps): 
    #сумма сумарне приведене споживання по квартирі, од.
    return sum([app.gen_E_used_k() for app in apps])


# ** def gen_no_counter_sum_area :
def gen_no_counter_sum_area(apps): 
    # площа без розп
    # по Площа опалювальна по КТЕ
    return sum([app.heating_area for app in apps if not app.counters_list])


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
    # del_it
    r = [app.gen_k_to_s() for app in apps]
    # print(r) 
    # print(r.index(max(r)))
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
    # del_it
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
def gen_Qpit_roz(sum_home_e, qfun_sys, q_Mkz, sum_no_counter_e): 
    """
    питомий обсяг енергії спожитий одним розподілювачем
    Обсяг споживання тепла з розподілювачами
    """
    return sum_home_e - qfun_sys - q_Mkz - sum_no_counter_e

      
# ** def calc_surcharge : 
def calc_surcharge(app_list, q_pit_roz, q_op_min): 
    sum_e_k = sum_E_used_k(app_list)
    for i, app in enumerate(app_list):
        app_list[i].gen_surcharge(q_pit_roz, q_op_min, sum_e_k)
        # print("in ", app_list[i]._start_line )
        # print("index ", i)
        # print("value of ", app_list[i].surcharge)
    return gen_e_for_redistribute(app_list)


# ** def recalc_surcharge : 
def recalc_surcharge(app_list,
                     q_op_min,
                     e_for_redistibut,
                     times =gs_recalc_surcharge_times) : 
    start_times = times
    if gs_recalc_surcharge_print:
        print(start_times - times +1, ":e_for_redistibut = ", e_for_redistibut)
        print(start_times - times +1, ":suM surcharge = ", sum([app.surcharge for app in app_list]))
    # while times>=0 and e_for_redistibut >= 0:
    while times>0 and float("{:.5f}".format(sum([app.surcharge for app in app_list]))) != 0:
    # TODO chenge to compare with 0.000001 it help add this to setings
    # while times>0 and sum([app.surcharge for app in app_list]) != 0:
        for i, app in enumerate(app_list):
            # print("in ", app_list[i]._start_line )
            # print("index ", i)
            app_list[i].gen_specified_used_E (e_for_redistibut)
            app_list[i].gen_specified_surcharge(q_op_min)
            # print("value of 0 ", app_list[0].surcharge)
        # питомий обсяг енергій якій буде перерозподілено
        e_for_redistibut = gen_e_for_redistribute(app_list)
        times -=1
        if gs_recalc_surcharge_print:
            print(start_times - times +1, ":e_for_redistibut = ", e_for_redistibut)
            print(start_times - times +1, ":suM surcharge = ", sum([app.surcharge for app in app_list]))  # 
    if gs_recalc_surcharge_print_result:
        print("Zero recalculate surcharge found on step =", start_times - times +1)
    return e_for_redistibut


# ** def gen_e_for_redistribute : 
def gen_e_for_redistribute(app_list): 
    # обсяг енергій якій буде перерозподілено
    sum_E = sum([app.surcharge for app in app_list])
    # площа квартир якім буде повернуто об'єм донарахувань
    sum_S = sum([app.get_S_if_surcharge() for app in app_list])
    # питомий обсяг енергій якій буде перерозподілено
    return sum_E/sum_S



# ** def gen_total_counter_e : 
def gen_total_counter_e(apps): 
    """
    sum Ітого по распр., Гкал
    """
    return sum([app.specified_used_E for app in apps if app.counters_list])


# ** def gen_total_no_counter_e : 
def gen_total_no_counter_e(apps): 
    """
    sum Ітого по м2, Гкал
    """
    return sum([app.specified_used_E for app in apps if not app.counters_list])


# ** def gen_Q_Mkz : 
def gen_Q_Mkz(delta_e): 
    # обсяг тепла на опалення МЗК = 10% від
    return delta_e * gk_Qmzk


# ** def gen_Q_no_surge : 
def gen_Q_no_surge(app_list, q_roz): 
    """
    при цьому питомий обсяг споживання тепла приміщеннями без розподілювачів 
    """
    return ( gen_k_no_surge(app_list)
             * q_roz)


# ** def gen_k_no_surge : 
def gen_k_no_surge(apps): 
    return  qk_k_no_surge_if_less if gen_no_counter_sum_area(apps) / gen_sum_heated_area(apps) < qk_k_no_surge_proc else qk_k_no_surge_if_more 

    
# ** def calc_no_counter_e : 
def calc_no_counter_e( app_list,
                       q_no_surge): 
    """
    generate in app list
    by use metod of clas
    app_list[i].gen_no_counter_e(q_no_surge)
    Ітого по м2, Гкал
    """
    for i, app in enumerate(app_list):
        # print("in ", app_list[i]._start_line )
        # print("index ", i)
        if not app.counters_list:
          app_list[i].gen_no_counter_e (q_no_surge)
          # print(app_list[i].specified_used_E) 
    return app_list




# ** def calc_final_totals : 
def calc_final_totals(app_list,
                      qfun_sys,
                      q_Mkz,
                      sum_heated_area): 
    s_qfun_sys = qfun_sys / sum_heated_area
    # print(s_qfun_sys)
    s_q_Mkz = q_Mkz / sum_heated_area
    # print(s_q_Mkz)
    for i, app in enumerate(app_list):
        # print("in ", app_list[i]._start_line )
        # print("index ", i)
        # функціонування системи
        app_list[i].gen_total_fun_sys (s_qfun_sys)
        # МЗК
        app_list[i].gen_total_Mkz (s_q_Mkz)
        # ВСЬОГО, Гкал
        app_list[i].gen_total_e()
    return app_list




# ** def calc_all_values_in_apps : 
def calc_all_values_in_apps(df, app_list): 
    # загальна площа будинку
    sum_heated_area = gen_sum_heated_area(app_list)
    last_app_line = get_last_app_line(app_list)
    # по будинку за т/ліч
    delta_value_home_counter = gen_delta_value_home_counter(df, last_app_line)
    # найбільш показник розподілювачів серед приміщень приведена до 1 м2 площі
    index_most_heated_app = find_most_heated_app(app_list)
    # Питомий обсяг спожитої енергії на опалення усіх приміщень
    q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
    # обсяг тепла на опалення МЗК = 10% від
    q_Mkz = gen_Q_Mkz(delta_value_home_counter)
    # обсяг тепла на функц. системи = 5% якщо є погодне регулювання в ІТП або 15% якщо не має від
    qfun_sys = gen_Qfun_sys(delta_value_home_counter)
    # Обсяг споживання тепла приміщенням без розподілювачамиів
    q_no_surge = gen_Q_no_surge(app_list,
                                q_roz)
    # calculate column in app_list
    # Ітого по м2, Гкал
    app_list = calc_no_counter_e( app_list,
                       q_no_surge)
    # sum Ітого по м2, Гкал
    total_no_counter_e = gen_total_no_counter_e(app_list)
    # питомий обсяг енергії спожитий одним розподілювачем
    q_pit_roz = gen_Qpit_roz(delta_value_home_counter, qfun_sys, q_Mkz, total_no_counter_e)
    q_op_min = gen_Qop_min(q_roz)
    # донарахування, Гкал
    # in each counter
    # return 
    # питомий обсяг енергій якій буде перерозподілено
    e_for_redistibut = calc_surcharge(app_list,
                                      q_pit_roz,
                                      q_op_min)
    e_for_redistibut = recalc_surcharge(app_list,
                                        q_op_min,
                                        e_for_redistibut)
    # Ітого по распр., Гкал
    total_counter_e = gen_total_counter_e(app_list)
    # calculate columns in app_list
    # функціонування системи
    # МЗК
    # ВСЬОГО, Гкал
    calc_final_totals( app_list,
                       gen_Qfun_sys(delta_value_home_counter),
                       q_Mkz,
                       sum_heated_area)
    return app_list




# ** def set_to_report : 
def set_to_report(df, app_list): 
    # 0 № п/п	
    # 1 № квартири	
    for app in app_list:
        if app.counters_list:
            # 2 Ітого по распр., Гкал
            app.set_to_report(df, gl_total_couter_e_column, app.specified_used_E)
        else:    
            # 3 Ітого по м2, Гкал
            app.set_to_report(df, gl_total_no_couter_e_column, app.specified_used_E)
        # 4 функціонування системи
        app.set_to_report(df, gl_func_sys_column, app.total_fun_sys)
        # 5 МЗК
        app.set_to_report(df, gl_mzk_column, app.total_Mkz)
        # 6 ВСЬОГО, Гкал
        app.set_to_report(df, gl_total_e_column, app.total_e)
    return df


# ** def save_data_frame : 
def save_data_frame(output, df, df_report): 
  # writer = pd.ExcelWriter('output.xlsx', engine='openpyxl')
  # df = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])  
  # with pd.ExcelWriter("path_to_file.xlsx") as writer:
  #     df.to_excel(writer) 
  # df_report['new_column'] = [1, 2, 3, 4, 5]
  # Save the updated dataframe to the Excel file
  with pd.ExcelWriter(output,
                    # sheet_name='report',
                    engine='openpyxl',
                    # index_col=0,
                    # header=None,
                    # mode="a",
                    # if_sheet_exists="overlay"
                    # if_sheet_exists="replace"
                    # if_sheet_exists='append'
                      ) as writer:
    # df_report.to_excel(writer, sheet_name='report')
      # for report in reports:
      #   report.to_excel(writer, index=False)
    # df_report.to_excel(writer, index=False, startrow=writer.sheets['Sheet1'].max_row)
    df.to_excel(writer, index=False, sheet_name=gv_sheet_name)
    df_report.to_excel(writer, index=False, sheet_name=gv_sheet_report)
  # df.to_excel(writer, index=False, startrow=writer.sheets['Sheet1'].max_row)
  # df_report.to_excel("foo.xlsx", sheet_name='report')
  # df.to_excel(writer, sheet_name="Sheet1")
  # report = writer.bookworksheet = writer.sheets['report']
  # writer.save()
  # writer.close()






# ** ------------------------------------------:
# * if __name__ : 
# ----------------------------------------------
if __name__ == "__main__": 
    import sys
    # sys.argv = ['', 'Test.testName']
    main(sys.argv)


# ----------------------------------------------
# * -------------------------------------------:
