import sys
import pandas as pd
from global_values import *
from appart_values import *
from rules import *
import datetime

gui_log =[]
g_filename = gv_filename
g_output = gv_output
g_sheet_name = gv_sheet_name
g_csv = gv_csv

def cli(argv): 
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

def end_app(arg):
    sys.exit(arg)

def main(argv):
    if gg_GUI and not is_test(argv):
        print("run winmain.py")
        # gui(argv) 
    else:
        cli(argv) 
    end_app(0)

def gui_calc(_filename, _csv, _output, _home_count = None): 
# *** set values and params :
    sheet_name = g_sheet_name 
    filename = g_sheet_name if not _filename or _filename == "" else _filename
    output =  _output if _output or _output != "" else g_output
# *** loading a dataframe from Excel :
    df = load_exel(filename, sheet_name)
    csv = ";" if not _csv or _csv == "" else _csv
    app_list, couters_list = populate_apps(df) 
    if _home_count:
        last_app_line = get_last_app_line(app_list)
        r = set_home_counter(df, last_app_line, _home_count)
        print(r)
        print_to_log("Ці клітини загальнобудинкового лічильника використовуються, ігноруючи показники з клітини файлу Excel")
        print_to_log("використання значення = "+ str(_home_count))
        print_to_log(r)
# *** loading date frame from CSV or RLV file:
    udate_data = set()
    for path_csv in csv.split(";"):
        if path_csv=="":
            continue
        print_to_log("завантажуємо значення з файлу: "+path_csv)
        udate_data.add(update_counters(app_list,
                                       couters_list,
                                       load_db(path_csv)))
    #  замена имени столбца
    df.iloc[gl_ferst_app_row - 1, gl_column_home_counter_value1] = "показники на " + ";".join(udate_data)
    # TODO: remove duble populate_apps
    app_list, couters_list = populate_apps(df) 

# *** product of calculations:
    app_list = calc_all_values_in_apps( df, app_list)
    # df_report = load_exel(filename, gv_sheet_report)
    # df_report = set_to_report(df_report, app_list)
# *** generating reports:
    df_report = None
    if gv_enable_full_report:
        df_report = gen_OSBB_report(app_list)
    df_TE_report = gen_TE_report(app_list)
# *** postprocessing block:
    # df_rules = load_exel(filename, gr_rule_sheet_name)
    try:
          df_rules = load_exel(filename, gr_rule_sheet_name)
          df_TE_report = postprocessing_df_with_rules_df(df_TE_report, df_rules)
    except Exception:
          df_rules = None
          print("Error in load rules sheet = ", gr_rule_sheet_name ," from file =", filename)
          print_to_log("Помилка під час завантаження аркуша правил = "+ gr_rule_sheet_name + " з файлу =" + filename)
    if not gr_rule_sheet_enable_in_report:
        df_rules = None
# *** save block:
    save_data_frame(output, df,
                    df_report,
                    df_rules = df_rules,
                    df_TE_report = df_TE_report)

def print_to_log(string):
    gui_log.append(datetime.datetime.now().strftime("%H:%M:%S.%f")+": "+ string)

def cmd_line_arg(argv):
    global g_filename, g_csv, g_output
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

def is_test(argv): 
    for arg in argv[1:]:
        if arg.startswith("--test"):
            return True
    return False

def get_value_from_param_by_key(params, key): 
    for arg in argv[1:]:
        if arg.startswith("--test"):
            return True
    return False

def gen_sum_heated_area(apps): 
    # Площа опалювальна по КТЕ
    return sum([app.heating_area for app in apps])

def sum_E_used_k(apps): 
    #сумма сумарне приведене споживання по квартирі, од.
    return sum([app.gen_E_used_k() for app in apps])

def gen_no_counter_sum_area(apps): 
    # площа без розп
    # по Площа опалювальна по КТЕ
    return sum([app.heating_area for app in apps if not app.counters_list])

def get_last_app_line(apps): 
    if apps[-1].is_last :
      return apps[-1].next_app_line
    else:
      print_to_log('Помилка у вхідному файлі Excel get_last_line не в останній квартирі ' + str(len(apps)))
      raise NameError(
          'get_last_line in not last appart ' + str(len(apps)))

def get_home_value(df, line, column):
    # r =  float(df.iloc[line, column])
    r =  df.iloc[line, column]
    # print("value = ", r)
    if not isinstance(r, float) and not isinstance(r, int):
        print_to_log('Помилка у вхідному Excel файлі: не числовий формат показника у клітини in get_home_value not int or float on line = ' + str(line + gl_exl_shift_rows) + ', for column ' + str(column))
        raise NameError('in get_home_value not int or float on line = ' + str(line + gl_exl_shift_rows) + ', for column ' + str(column))
    if pd.isna(r):
        print_to_log('Помилка у вхідному Excel файлі: у клітини відсутнє значення no value on line = ' + str(line + gl_exl_shift_rows) + ', for column ' + str(column))
        raise NameError('no value on line = ' + str(line + gl_exl_shift_rows) + ', for column ' + str(column))
    return r

def set_home_counter(df, g_line, values): 
    if not values or values[0] == "" and values[1] == "":
        return "значення загальнобудинкового лічильника використані з Excel"
    if values[0] != "":
      df.iloc[g_line + gl_shift_home_counter_value1, gl_column_home_counter_value1] = float(values[0])
    if values[1] != "":
      df.iloc[g_line + gl_shift_home_counter_value2, gl_column_home_counter_value2] = float(values[1])
    return "значення загальнобудинкового лічильника в екселі оновлено" + str(values[0]) + " ; " + str(values[0])

def gen_delta_value_home_counter(df, g_line): 
    return get_home_value(df,
                g_line + gl_shift_home_counter_value1,
                gl_column_home_counter_value1) - get_home_value(df,
                    g_line + gl_shift_home_counter_value2,
                    gl_column_home_counter_value2)

def gen_Qfun_sys(delta_value_home_counter): 
    # обсяг тепла на функц. системи = 5% якщо є погодне регулювання в ІТП або 15% якщо не має від
    return delta_value_home_counter * gk_Qfun_sys

def gen_Qmzk(delta_value_home_counter): 
    # обсяг тепла на опалення МЗК = 10% від
    return delta_value_home_counter * gk_Qmzk

def gen_Qroz(delta_value_home_counter, sum_heated_area): 
    # Питомий обсяг спожитої енергії на опалення усіх приміщень
    return (delta_value_home_counter
            - gen_Qfun_sys(delta_value_home_counter)
            - gen_Qmzk(delta_value_home_counter)) / sum_heated_area

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

def gen_Qpit_roz(sum_home_e, qfun_sys, q_Mkz, sum_no_counter_e): 
    """
    питомий обсяг енергії спожитий одним розподілювачем
    Обсяг споживання тепла з розподілювачами
    """
    return sum_home_e - qfun_sys - q_Mkz - sum_no_counter_e

def calc_surcharge(app_list, q_pit_roz, q_op_min): 
    sum_e_k = sum_E_used_k(app_list)
    if sum_e_k == 0:
      print_to_log('Помилка: сумарне використання енергії 0, нема нічого для обчислення no Energi use in any appartament (exempl colmn R = colmn S)')
      raise ValueError('no Energi use in any appartament (exempl colmn R = colmn S)')
    for i, app in enumerate(app_list):
        app_list[i].gen_surcharge(q_pit_roz, q_op_min, sum_e_k)
        # print("in ", app_list[i]._start_line )
        # print("index ", i)
        # print("value of ", app_list[i].surcharge)
    return gen_e_for_redistribute(app_list)

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

def gen_e_for_redistribute(app_list): 
    # обсяг енергій якій буде перерозподілено
    sum_E = sum([app.surcharge for app in app_list])
    # площа квартир якім буде повернуто об'єм донарахувань
    sum_S = sum([app.get_S_if_surcharge() for app in app_list])
    # питомий обсяг енергій якій буде перерозподілено
    return sum_E/sum_S

def gen_total_counter_e(apps): 
    """
    sum Ітого по распр., Гкал
    """
    return sum([app.specified_used_E for app in apps if app.counters_list])

def gen_total_no_counter_e(apps): 
    """
    sum Ітого по м2, Гкал
    """
    return sum([app.specified_used_E for app in apps if not app.counters_list])

def gen_Q_no_surge(app_list, q_roz): 
    """
    при цьому питомий обсяг споживання тепла приміщеннями без розподілювачів 
    """
    return ( gen_k_no_surge(app_list)
             * q_roz)

def gen_k_no_surge(apps): 
    return  qk_k_no_surge_if_less if gen_no_counter_sum_area(apps) / gen_sum_heated_area(apps) < qk_k_no_surge_proc else qk_k_no_surge_if_more

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

def calc_all_values_in_apps(df, app_list): 
    # загальна площа будинку
    sum_heated_area = gen_sum_heated_area(app_list)
    last_app_line = get_last_app_line(app_list)
    # по будинку за т/ліч
    delta_value_home_counter = gen_delta_value_home_counter(df, last_app_line)
    # Питомий обсяг спожитої енергії на опалення усіх приміщень
    q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
    # обсяг тепла на опалення МЗК = 10% від
    q_Mzk = gen_Qmzk(delta_value_home_counter)
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
    q_pit_roz = gen_Qpit_roz(delta_value_home_counter, qfun_sys, q_Mzk, total_no_counter_e)
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
    # total_counter_e = gen_total_counter_e(app_list)
    # calculate columns in app_list
    # функціонування системи
    # МЗК
    # ВСЬОГО, Гкал
    calc_final_totals( app_list,
                       gen_Qfun_sys(delta_value_home_counter),
                       q_Mzk,
                       sum_heated_area)
    return app_list

def load_exel(filename, sheet_name): 
    df = pd.read_excel(filename,
                      sheet_name = sheet_name,
                      engine='openpyxl',
                      # index_col=0,
                      header=None,
                      )
    return df

def load_csv(filename): 
    if not filename:
        return None
    print_to_log("Завантажуємо файл csv")
    df = pd.read_csv(filename ,
                    encoding = gv_csv_encoding,
                    header = gv_csv_header,
                    sep = gv_csv_sep,
                     index_col = gv_csv_index_col)
    print_to_log("Файл csv завантажений")
    return df

def load_rlv(filename): 
    if not filename:
        return None
    print_to_log("Завантажуємо файл rlv")
    df = pd.read_csv(filename ,
                    encoding = gv_rlv_encoding,
                    header = gv_rlv_header,
                    sep = gv_rlv_sep,
                     index_col = gv_rlv_index_col)
    print_to_log("файл rlv завантажений")
    return df

def load_db(filename): 
    if not filename:
        return None
    extesion = (filename.split("."))[-1]
    if extesion == "rlv":
      return load_rlv(filename)
    elif extesion == "csv":
      return load_csv(filename)
    print_to_log("Неприпустиме розширення файлу для оновлення. очікується .rlv або .csv. Файл проігноровано = "+ filename)
    return None

def get_df_list_from_filename_string(string):
  r=[]
  for path_csv in string.split(";"):
    if path_csv=="" or path_csv==" ": continue
    r.append(load_db(path_csv.strip()))
  return r

def get_dates_from_colums_list(df, colist):
  r = []
  for i, name in enumerate(colist):
      try:
          colnum = df.columns.get_loc(name)
      except Exception as e:
          print ("on name=", name, " is Exception=", str(e))
          print("Possible reason - file does not contain the expected columns")
          print_to_log("файл не містить очікуваних стовпців "+ str(e))
          break
      value = df.iloc[0, colnum]
      if pd.isnull(value): break
      r.append(value)
  return r

def get_colms_names_from_dates(dates, dateslist):
  r = []
  for date in dates:
    try:
      r.append(gv_rlv_colums_name_values_list[dateslist.index(date)])
    except Exception:
      r.append(None)
  text= [ "використання колонки S вхідного файлу звіту ексель",
          "використання колонки R вхідного файлу звіту ексель"]
  for i in [0,1]:
    if r[i]:
      print_to_log("використання колонки DB файлу - " + r[i])
    else:
      print_to_log(text[i])
  return r

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

def gen_OSBB_report(app_list): 
    df = [[gn_num_column,
           gn_app_num_column,
           gn_total_couter_e_column, 
           gn_total_no_couter_e_column,
           gn_func_sys_column ,
           gn_mzk_column ,
           gn_total_e_column ]]
    for app in app_list:
        # 0 № п/п 
        # 1 № квартири  
        row =[app.num_name, app.app_num_name,]
        if app.counters_list:
            # 2 Ітого по распр., Гкал
            row.append(app.specified_used_E)
            row.append(0)
        else:    
            # 3 Ітого по м2, Гкал
            row.append(0)
            row.append(app.specified_used_E)
        # 4 функціонування системи
        row.append(app.total_fun_sys)
        # 5 МЗК
        row.append(app.total_Mkz)
        # 6 ВСЬОГО, Гкал
        row.append(app.total_e)
        df.append(row)
    return pd.DataFrame(df)

def gen_TE_report(app_list): 
    df = [[
        # 0 Особовий рахунок  
        gn_TE_num_column,
        # 1 № Адреса  
        gn_TE_adders_column ,
        # 2 № віртуального ліч-ка
        gn_TE_num_virt_column ,
        # 3 Період
        gn_TE_period ,
        # 4 Обсяг споживання,  Гкал
        gn_TE_total_e_column ]]
    sum_total = 0
    for app in app_list:
        row =[
            # 0 № п/п 
            app.num_name,
            # 1 № квартири  
            app.app_num_name,
            # 2 № віртуального ліч-ка
            app.num_name]
        # 3 Період
        row.append("")
        # 4 Обсяг споживання,  Гкал
        # row.append(app.total_e)
        # row.append(float(gv_TE_report_formar_len.format(app.total_e)))
        row.append(float(gv_TE_report_formar_len(app.total_e)))
        df.append(row)
        sum_total += app.total_e
    df.append([])
    df.append([
        "", "", "","Всього:",
        (float(gv_TE_report_formar_len(sum_total)))
        # sum_total
    ])
    return pd.DataFrame(df)

def save_data_frame(output, df, df_report, df_rules=None, df_TE_report=None): 
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
    df.to_excel(writer, index=False, header=False, sheet_name=gv_sheet_name)
    if df_rules is not None:
        df_rules.to_excel(writer, index=False, header=False, sheet_name=gr_rule_sheet_name)
    if df_report is not None:
        df_report.to_excel(writer, index=False, header=False, sheet_name=gv_osbb_report)
    if df_TE_report is not None:
        df_TE_report.to_excel(writer, index=False, header=False, sheet_name=gv_TE_report)
    print_to_log("output report path "+ output)

def populate_apps(df): 
    al =[]
    cl =[]
    app_line = gl_ferst_app_row
    while True:
        app = Appart_values(df, app_line)
        app_line = app.next_app_line
        # print("app_line = ", app_line)
        al.append(app)
        cl.append(app.gen_counters_adress())
        if app.is_last:
            break
    return al, cl

def update_counters(app_list, counters_list, df_csv, data_i = 1): 
    if df_csv is None:
        return None
    name_date = gv_csv_name_date + str(gv_csv_name_i)
    # print(name_date)
    name_value = gv_csv_name_value + str(gv_csv_name_i)
    # print(name_value)
    data_list =set()
    id_list =set()
    for i, adress_list in enumerate(counters_list):
        if counters_list[i]:
            r = app_list[i].update_allvalues1_by_id(df_csv,  name_value, name_date)
            if r:
                data_list.update(r)
            else:
                id_list.update(app_list[i].not_found_ids)
                app_list[i].not_found_ids.clear()
            # print("data_ r = ", r) 
            # print("data_list = ", data_list) 
    # print("values", len(data_list))
    if len(data_list)==0:
        print_to_log("помилка даних csv. Файл не містить жодного ID з exel")
        # print("ошибка даных csv. фаил не содержит не одного ID из exel ")
        print_to_log("csv зіпсований. Обробку зупинено")
        raise NameError("csv corupt. no id exels in csv file ", "len(data_list) = ", len(data_list) )
    if len(data_list)!=1:
        for data in data_list:
          print_to_log("помилка даних csv. Більше однієї дати у стовпці "+ name_date+ " = "+ data)
          print("помилка даних csv. Більше однієї дати у стовпці "+ name_date+ " = "+ data)
        # print_to_log("csv uспорчен. Обработка остановлена")
        print_to_log("csv зіпсований. Обробку не зупинено")
        data_list = data_list.pop();
        print_to_log("назва стовбчика змінено на = " + str(data_list))
        # raise NameError("csv corupt. more then one date in csv column ", name_date, "len(data_list) = ", len(data_list) )
    # print("values from csv add on dates = ", data_list)
    if len(id_list)>0:
        print_to_log("Ці ID вказані у файлі, але відсутні у Excel" + str(id_list))
    print_to_log("Показники csv зафіксовані на дату"+ str(data_list))
    return str(data_list)

if __name__ == "__main__": 
    import sys
    # sys.argv = ['', 'Test.testName']
    main(sys.argv)
