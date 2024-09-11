# ----------------------------------------------
# * import block :
import unittest

from main import *

# filename = gv_filename
# sheet_name = gv_sheet_name 
# g_filename = gv_filename
# g_output = gv_output
# g_sheet_name = gv_sheet_name
# g_csv = gv_csv


# ----------------------------------------------
# * class Test_Init : 
# ** ------------------------------------------:
class Test_Init(unittest.TestCase):

# ----------------------------------------------
# ** def test_main : 
    def test_main(self):# {{{
        # print("Test tuner")
        with self.assertRaises(SystemExit) as cm:
            main(["main path", 
                  "--filename=Data_files/test.xlsx",
                  "--sheet_name=квартири, площі",
                  "--test"])
        self.assertEqual(cm.exception.code, 0)

        
# ----------------------------------------------

# ** def test_main Gui: 
    @unittest.skipIf(len(sys.argv) < 2  or sys.argv[1] != "test_main.Test_Init.test_main_gui", "not sigle test")
    def test_main_gui(self):
        # print(__name__)
        with self.assertRaises(SystemExit) as cm:
            main(["main path", 
                  "--filename=Data_files/test.xlsx",
                  "--sheet_name=квартири, площі",
                  ])
        self.assertEqual(cm.exception.code, 0)

        
# ----------------------------------------------
# ** def test_load_exel : 
    def test_load_exel(self):
        gv_filename = "Data_files/test.xlsx"
        # sheet_name = "показники"
        sheet_name = "квартири, площі"
        df = load_exel(gv_filename, sheet_name)
        self.assertEqual( df.iloc[104, 0], 37)
        self.assertEqual( df.iloc[107, 0], "end")
        self.assertEqual( df.iloc[105, 0], 38)
        self.assertEqual( df.iloc[105, 2], 9)
        self.assertEqual( df.iloc[105, 3], 1)
        # print(df.iloc[0:5, 0:2])
        # print(df.iloc[101, 0])
        # print(df.iloc[102, 0])
        # print(df.iloc[103, 0])
        # print(df.iloc[104, 0])
        # print("Test tuner")
        # self.assertIsNone(main(1))
        #view the first five rows: 
        # print (df.head())
        # print (df[1])
        # print (df["A"])
        # print(df.iloc[:, 0])
        # df.head()
        # print(df.index)
        # print(df["Radio address"])
        # print(df.index)
        # print(df.columns)

        # print(df.index[df.iloc[7] == 2].tolist())
        # print(df.index[df.iloc[:, 0] == 2].tolist())
        # print(df.index[df.iloc[:, 0] == 1])
        # print(df.index[df.iloc[:, 0] == 2])
        # print(df.index[df.iloc[:, 0] == 3])
        # print(df.index[df.iloc[:, 0] == 10])
        # print(df.loc["25482311.0", ["Radio address"]])
        # print(df.A)
        # print(df.loc[])
        # writer = pd.ExcelWriter('output.xlsx', engine='openpyxl')
        # df.to_excel(writer
        #             # , index=False
        #             )
        # workbook = writer.bookworksheet = writer.sheets['report']
        # header_fmt = workbook.add_format({'bold': True})
        # worksheet.set_row(0, None, header_fmt)
        # writer.save()


        # df.to_excel('output.xlsx')

        # print (df)


# ** def test_load_csv : 
    def test_load_csv(self):
        gv_filename = gv_csv
        df = load_csv(gv_filename)
        i = 1
        ser_id = 25482311
        name_text = "Historic date - " + str(i)
        name_value = "Historic value - " + str(i)
        self.assertEqual( df.loc[ser_id , name_text], "2021-04-16")
        self.assertEqual( df.loc[ser_id , name_value], 126)
        # self.assertEqual( df.iloc[107, 0], "end")
        # self.assertEqual( df.iloc[105, 0], 38)
        # self.assertEqual( df.iloc[105, 2], 9)
        # self.assertEqual( df.iloc[105, 3], 1)
        # print(df.iloc[0:5, 0:2])
        # print(df.iloc[101, 0])
        # print(df.iloc[102, 0])
        # print(df.iloc[103, 0])
        # print(df.iloc[104, 0])
        # print("Test tuner")
        # self.assertIsNone(main(1))
        #view the first five rows: 
        # print (df.head())
        # print (df[1])
        # print (df["A"])
        # print(df.iloc[:, 0])
        # df.head()
        # print(df.index)
        # print(df["Radio address"])
        # print(df.index)
        # print(df.columns)
        # print(df.index[df.iloc[7] == 2].tolist())
        # print(df.index[df.iloc[:, 0] == 2].tolist())
        # print(df.index[df.iloc[:, 0] == 1])
        # print(df.index[df.iloc[:, 0] == 2])
        # print(df.index[df.iloc[:, 0] == 3])
        # print(df.index[df.iloc[:, 0] == 10])
        # print(df.loc["25482311.0", ["Radio address"]])
        # print(df.A)
        # print(df.loc[])
        # print (df)


# ** def test_load_rlv : 
    def test_load_rlv(self):
        gv_filename = gv_rlv
        df = load_rlv(gv_filename)
        i = 1
        ser_id = 25482420
        name_text = "Historic date - " + str(i)
        name_value = "Historic value - " + str(i)
        self.assertEqual( df.loc[ser_id , name_text], "01.04.2023")
        self.assertEqual( df.loc[ser_id , name_value], 76)
        gv_filename = "Data_files/test2.csv.rlv"
        df = load_rlv(gv_filename)
        i = 1
        # print(df.index)
        ser_id = 25482599
        name_text = "Historic date - " + str(i)
        name_value = "Historic value - " + str(i)
        self.assertEqual( df.loc[ser_id , name_text], "01.04.2023")
        self.assertEqual( df.loc[ser_id , name_value], 0)
        # print(df.index)
        ser_id = 25482215
        name_text = "Historic date - " + str(i)
        name_value = "Historic value - " + str(i)
        self.assertEqual( df.loc[ser_id , name_text], "01.04.2023")
        self.assertEqual( df.loc[ser_id , name_value], 102)
        # self.assertEqual( df.iloc[107, 0], "end")
        # self.assertEqual( df.iloc[105, 0], 38)
        # self.assertEqual( df.iloc[105, 2], 9)
        # self.assertEqual( df.iloc[105, 3], 1)
        # print(df.iloc[0:5, 0:2])
        # print(df.iloc[101, 0])
        # print(df.iloc[102, 0])
        # print(df.iloc[103, 0])
        # print(df.iloc[104, 0])
        # print("Test tuner")
        # self.assertIsNone(main(1))
        #view the first five rows: 
        # print (df.head())
        # print (df[1])
        # print (df["A"])
        # print(df.iloc[:, 0])
        # df.head()
        # print(df.index)
        # print(df["Radio address"])
        # print(df.columns)
        # print(df.index[df.iloc[7] == 2].tolist())
        # print(df.index[df.iloc[:, 0] == 2].tolist())
        # print(df.index[df.iloc[:, 0] == 1])
        # print(df.index[df.iloc[:, 0] == 2])
        # print(df.index[df.iloc[:, 0] == 3])
        # print(df.index[df.iloc[:, 0] == 10])
        # print(df.loc["25482311.0", ["Radio address"]])
        # print(df.A)
        # print(df.loc[])
        # print (df)


# ** def test_load_db : 
    def test_load_db(self):
        # test =  ['Data_files/test.rlv', 'Data_files/test2.csv.rlv', 'Data_files/test.csv', '']
        test_path = gv_rlv+";"+"Data_files/test2.csv.rlv"+";"+ gv_csv +";"
        # print("test_path = ", test_path)
        # print("test_path = ", test_path.split(";"))
        path = test_path.split(";")[0]
        # print("path = ", path)
        gv_filename = path
        df = load_db(gv_filename)
        i = 1
        ser_id = 25482420
        name_text = "Historic date - " + str(i)
        name_value = "Historic value - " + str(i)
        self.assertEqual( df.loc[ser_id , name_text], "01.04.2023")
        self.assertEqual( df.loc[ser_id , name_value], 76)
         # ""
        path = test_path.split(";")[3]
        # print("path = ", path)
        gv_filename = path
        df = load_db(gv_filename)
        self.assertIsNone(df)
        #  for : 
        test_df = []
        for path_csv in test_path.split(";"):
            if path_csv=="":
                # print("path_csv ='' ",)
                continue
            r = load_db(path_csv)
            test_df.append(r)
        self.assertIsNotNone(test_df[0])
        self.assertIsNotNone(test_df[1])
        self.assertIsNotNone(test_df[2])
        # gv_filename = gv_rlv
        gv_filename = gv_rlv
        df = load_db(gv_filename)
        i = 1
        ser_id = 25482420
        name_text = "Historic date - " + str(i)
        name_value = "Historic value - " + str(i)
        self.assertEqual( df.loc[ser_id , name_text], "01.04.2023")
        self.assertEqual( df.loc[ser_id , name_value], 76)
        # gv_filename = "Data_files/test2.rlv"
        gv_filename = "Data_files/test2.csv.rlv"
        df = load_db(gv_filename)
        i = 1
        # print(df.index)
        ser_id = 25482599
        name_text = "Historic date - " + str(i)
        name_value = "Historic value - " + str(i)
        self.assertEqual( df.loc[ser_id , name_text], "01.04.2023")
        self.assertEqual( df.loc[ser_id , name_value], 0)
        # print(df.index)
        ser_id = 25482215
        name_text = "Historic date - " + str(i)
        name_value = "Historic value - " + str(i)
        self.assertEqual( df.loc[ser_id , name_text], "01.04.2023")
        self.assertEqual( df.loc[ser_id , name_value], 102)
        # gv_csv
        gv_filename = gv_csv
        df = load_db(gv_filename)
        i = 1
        ser_id = 25482311
        name_text = "Historic date - " + str(i)
        name_value = "Historic value - " + str(i)
        self.assertEqual( df.loc[ser_id , name_text], "2021-04-16")
        self.assertEqual( df.loc[ser_id , name_value], 126)
        # None test
        wm.gui_log.clear()
        gv_filename = "Data_files/test2.exel"
        df = load_db(gv_filename)
        self.assertIsNone(df)
        self.assertEqual( len(wm.gui_log), 1)
        gv_filename = "Data_files"
        df = load_db(gv_filename)
        self.assertIsNone(df)
        self.assertEqual( len(wm.gui_log), 2)
        gv_filename = None
        df = load_db(gv_filename)
        self.assertIsNone(df)
        self.assertEqual( len(wm.gui_log), 2)


# ** def test_cmd_line_arg : 
    def test_cmd_line_arg(self): 
        global g_filename, g_csv, g_output
        # self.assertEqual(filename, "Data_files/metod01.xlsx")
        self.assertEqual(g_filename, "Data_files/metod01.xlsx")
        argv = ["main path", 
                "--filename=Data_files/1.xlsx",
                "--csv=Data_files/2.xlsx",
                "--output=Data_files/3.xlsx",
                # "--filename=квартири, площі"
                ]
        filename, csv, output = cmd_line_arg(argv)
        self.assertEqual(filename, "Data_files/1.xlsx")
        self.assertEqual(csv, "Data_files/2.xlsx")
        self.assertEqual(output, "Data_files/3.xlsx")
        # self.assertEqual(g_filename, "Data_files/1.xlsx")
        # self.assertEqual(g_csv, "Data_files/2.xlsx")
        # self.assertEqual(g_output, "Data_files/3.xlsx")

# ----------------------------------------------
# * class setUp_Test : 
# ** ------------------------------------------:
class setUp_Test(unittest.TestCase):
# ** @classmethod #setUpClass#  : 
    @classmethod #setUpClass# {{{
    def setUpClass(self):
        # print("*"*33,"*"*33)
        gv_filename = "Data_files/test.xlsx"
        # sheet_name = "показники"
        sheet_name = "квартири, площі"
        self.df = load_exel(gv_filename, sheet_name)
        # self.mw = Main_Windows()
        # self.fk = FirstKivy()
    #     print ("file opened")
    #     print("*"*33,"*"*33)
    #     self.gs.sheet_main.update_acell('A1', 'Bingo!')


# ** @classmethod #tearDownClass# : 
    # @classmethod #tearDownClass# {{{
    # def tearDownClass(cls):
    #     print("*"*33,"*"*33)
    #     print("tear down module")
    #     print("*"*33,"*"*33)

# ** def test_init1 : 
    def test_init(self):# {{{
        self.assertEqual(self.df.iloc[104, 0], 37)
        self.assertEqual(self.df.iloc[107, 0], "end")
        self.assertEqual(self.df.iloc[105, 0], 38)
        self.assertEqual(self.df.iloc[105, 2], 9)
        self.assertEqual(self.df.iloc[105, 3], 1)
        # self.assertIsNotNone( mw.temp_A)
        # self.assertIsNotNone( mw.temp_B)


# ** def test_populate_apps : 
    def test_populate_apps(self): 
        t1, t2 = populate_apps(self.df)
        self.assertEqual(len(t1), 38)
        self.assertEqual(len(t2), 38)
        self.assertEqual(t1[0]._start_line, 1)
        self.assertEqual(t1[0].next_app_line, 2)
        self.assertEqual(t2[0], None)
        self.assertEqual(t1[37]._start_line, 105)
        self.assertEqual(t1[37].next_app_line, 107)
        self.assertEqual(t2[37], [
                                25482673,
                                25482672,])
        self.assertEqual(t1[35]._start_line, 100)
        self.assertEqual(t1[35].next_app_line, 104)
        self.assertEqual(t2[35], [25482671, 25482670, 25482669, 25482694,])
        # t1, t2 = populate_apps(self.df)
        t1, t2 = populate_apps(self.df)
        self.assertEqual(len(t1), 38)
        self.assertEqual(len(t2), 38)
        self.assertEqual(t1[0]._start_line, 1)
        self.assertEqual(t1[0].next_app_line, 2)
        self.assertEqual(t2[0], None)
        self.assertEqual(t1[37]._start_line, 105)
        self.assertEqual(t1[37].next_app_line, 107)
        self.assertEqual(t2[37], [
                                25482673,
                                25482672,])
        self.assertEqual(t1[35]._start_line, 100)
        self.assertEqual(t1[35].next_app_line, 104)
        self.assertEqual(t2[35], [25482671, 25482670, 25482669, 25482694,])


# ** def test_gen_OSBB_report : 
    def test_gen_OSBB_report(self): 
        app_list, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(app_list)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        sum_heated_area = gen_sum_heated_area(app_list)
        q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
        qfun_sys = gen_Qfun_sys(delta_value_home_counter)
        q_Mkz = gen_Qmzk(delta_value_home_counter)
        q_no_surge = gen_Q_no_surge(app_list,
                                    q_roz,)
        app_list = calc_no_counter_e( app_list,
                                      q_no_surge)
        total_no_counter_e = gen_total_no_counter_e(app_list)
        q_pit_roz = gen_Qpit_roz(delta_value_home_counter, qfun_sys, q_Mkz, total_no_counter_e)
        q_op_min = gen_Qop_min(q_roz)
        test = app_list[6].surcharge
        self.assertIsNone(test)
        e_for_redistibut = calc_surcharge(app_list, q_pit_roz, q_op_min)
        e_for_redistibut = recalc_surcharge(app_list,
                                            q_op_min,
                                            e_for_redistibut,
                                            times = 1
                                            # times = 200
                                            )
        e_for_redistibut = recalc_surcharge(app_list,
                                            q_op_min,
                                            e_for_redistibut,
                                            times = 1
                                            # times = 200
                                            )
        test = app_list[6].specified_used_E
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.922)
        calc_final_totals( app_list,
                           qfun_sys,
                           q_Mkz,
                           sum_heated_area)
        t = gen_OSBB_report(app_list)
        # print(t)
        # self.assertEqual(len(t1), 38)
        # self.assertEqual(len(t2), 38)
        # self.assertEqual(t1[0]._start_line, 1)
        # self.assertEqual(t1[0].next_app_line, 2)
        # self.assertEqual(t2[0], None)
        # self.assertEqual(t1[37]._start_line, 105)
        # self.assertEqual(t1[37].next_app_line, 107)
        # self.assertEqual(t2[37], [
        #                         25482673,
        #                         25482672,])
        # self.assertEqual(t1[35]._start_line, 100)
        # self.assertEqual(t1[35].next_app_line, 104)
        # self.assertEqual(t2[35], [25482671, 25482670, 25482669, 25482694,])


# ** def test_gen_TE_report : 
    def test_gen_TE_report(self): 
        app_list, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(app_list)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        sum_heated_area = gen_sum_heated_area(app_list)
        q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
        qfun_sys = gen_Qfun_sys(delta_value_home_counter)
        q_Mkz = gen_Qmzk(delta_value_home_counter)
        q_no_surge = gen_Q_no_surge(app_list,
                                    q_roz,)
        app_list = calc_no_counter_e( app_list,
                                      q_no_surge)
        total_no_counter_e = gen_total_no_counter_e(app_list)
        q_pit_roz = gen_Qpit_roz(delta_value_home_counter, qfun_sys, q_Mkz, total_no_counter_e)
        q_op_min = gen_Qop_min(q_roz)
        test = app_list[6].surcharge
        self.assertIsNone(test)
        e_for_redistibut = calc_surcharge(app_list, q_pit_roz, q_op_min)
        e_for_redistibut = recalc_surcharge(app_list,
                                            q_op_min,
                                            e_for_redistibut,
                                            times = 1
                                            # times = 200
                                            )
        e_for_redistibut = recalc_surcharge(app_list,
                                            q_op_min,
                                            e_for_redistibut,
                                            times = 1
                                            # times = 200
                                            )
        test = app_list[6].specified_used_E
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.922)
        calc_final_totals( app_list,
                           qfun_sys,
                           q_Mkz,
                           sum_heated_area)
        t = gen_TE_report(app_list)
        # print(t)
        # 1,4,

        # print(t.iloc[1,4])
        self.assertEqual(t.iloc[1,4], 2.326)
        # print(t.iloc[40,4])
        # print(str(t.iloc[40,4]))
        self.assertEqual(t.iloc[40,4], 63.720)
        # self.assertEqual(len(t2), 38)
        # self.assertEqual(t1[0]._start_line, 1)
        # self.assertEqual(t1[0].next_app_line, 2)
        # self.assertEqual(t2[0], None)
        # self.assertEqual(t1[37]._start_line, 105)
        # self.assertEqual(t1[37].next_app_line, 107)
        # self.assertEqual(t2[37], [
        #                         25482673,
        #                         25482672,])
        # self.assertEqual(t1[35]._start_line, 100)
        # self.assertEqual(t1[35].next_app_line, 104)
        # self.assertEqual(t2[35], [25482671, 25482670, 25482669, 25482694,])


# ** def test_update_counters : 
    def test_update_counters(self): 
        t1, t2 = populate_apps(self.df)
        self.assertEqual(t2[37],
                         [25482673,
                          25482672,])
        self.assertEqual(t2[35],
                         [25482671,
                          25482670,
                          25482669,
                          25482694,])
        app_list, couters_list = t1, t2
        # ------
        # gv_filename = gv_csv
        gv_filename = gv_csv
        df_csv = load_csv(gv_filename)
        self.assertEqual(app_list[37].counters_list[0].get_value1(), 875)
        # print(df_csv)
        r = update_counters(app_list, couters_list, df_csv) 
        # print("update result = ", r)      
        self.assertEqual(t2[37],
                         [25482673,
                          25482672,])
        self.assertEqual(app_list[37].counters_list[0].get_value1(), 178)
        # self.assertEqual(t1[37]., 100)
        # self.assertEqual(t1[35].next_app_line, 104)
        # self.assertEqual(t2[35],
        #                  [25482671,
        #                   25482670,
        #                   25482669,
        #                   25482694,])
        # ------
        # gv_filename = gv_rlv
        gv_filename = gv_rlv
        df_csv = load_rlv(gv_filename)
        # ------
        # from global_values import *
        # name_date = gv_csv_name_date + str(gv_csv_name_i)
        # name_value = gv_csv_name_value + str(gv_csv_name_i)
        # Historic date - 1
        # Historic value - 1
        # r = [] 
        # r.append(df.loc[ser_id , name_date])
        # print("r = ", r)
        # ------
        self.assertEqual(app_list[37].counters_list[0].get_value1(), 178)
        # print(df_csv)
        # with self.assertRaises(Exception):
        update_counters(app_list, couters_list, df_csv) 
        self.assertEqual(app_list[37].counters_list[0].get_value1(), 209)
        self.assertEqual(t2[37],
                         [25482673,
                          25482672,])
        # self.assertEqual(app_list[37].counters_list[0].get_value1(), 178)
        # ------
        gv_filename = "Data_files/test2.csv.rlv"
        df_csv = load_rlv(gv_filename)
        # print(df_csv)
        with self.assertRaises(Exception):
            update_counters(app_list, couters_list, df_csv) 
        # r = app_list[i].update_allvalues1_by_id(df_csv,  name_value, name_date)


# ** def test_gen_sum_heated_area : 
    def test_gen_sum_heated_area(self): 
        t1, t2 = populate_apps(self.df)
        test = gen_sum_heated_area(t1)
        self.assertEqual(float("{:.3f}".format(test)) , 2315.33)


# ** def test_sum_E_used_k : 
    def test_sum_E_used_k(self): 
        t1, t2 = populate_apps(self.df)
        test = sum_E_used_k(t1)
        self.assertEqual(float("{:.3f}".format(test)) , 4823.121)


# ** def test_gen_no_counter_sum_area : 
    def test_gen_no_counter_sum_area(self): 
        t1, t2 = populate_apps(self.df)
        test = gen_no_counter_sum_area(t1)
        # for app in [app.sum_area for app in apps if not app.counters_list] :
        self.assertEqual(float("{:.3f}".format(test)) , 803.65)


# ** def test_get_last_app_line : 
    def test_get_last_app_line(self): 
        t1, t2 = populate_apps(self.df)
        test = get_last_app_line(t1)
        self.assertEqual(test , 107)
        with self.assertRaises(NameError):
            test = get_last_app_line(t1[:-1])
            self.assertEqual(test , 103)


# ** test_get_home_value : 
    def test_get_home_value(self):
        t1, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(t1)
        test = get_home_value(self.df , last_app_line +
                                        gl_shift_home_counter_value1,
                                        gl_column_home_counter_value1)
        self.assertEqual(test, 1613.72)
        test = get_home_value(self.df , last_app_line +
                                        gl_shift_home_counter_value2,
                                        gl_column_home_counter_value2)
        self.assertEqual(test, 1550.00)
        with self.assertRaises(NameError):
            test = get_home_value(self.df , 
                                  gl_shift_home_counter_value2,
                                  gl_column_home_counter_value2)


# ** test_gen_delta_value_home_counter : 
    def test_gen_delta_value_home_counter(self):
        t1, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(t1)
        test = gen_delta_value_home_counter(self.df , last_app_line)
        self.assertEqual(float("{:.3f}".format(test)) , 63.72)
        with self.assertRaises(NameError):
            test = gen_delta_value_home_counter(self.df , last_app_line + 1)


# ** test_set_home_counter : 
    def test_set_home_counter(self):
        t1, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(t1)
        test = gen_delta_value_home_counter(self.df , last_app_line)
        self.assertEqual(float("{:.3f}".format(test)) , 63.72)
        test = get_home_value(self.df , last_app_line +
                                        gl_shift_home_counter_value1,
                                        gl_column_home_counter_value1)
        self.assertEqual(test, 1613.72)
        test = get_home_value(self.df , last_app_line +
                                        gl_shift_home_counter_value2,
                                        gl_column_home_counter_value2)
        self.assertEqual(test, 1550.00)
        # start set_home_counter : 
        set_home_counter(self.df , last_app_line, [300.111, 200.222])
        # end set_home_counter : 
        test = gen_delta_value_home_counter(self.df , last_app_line)
        self.assertEqual(float("{:.3f}".format(test)) , 99.889)
        test = get_home_value(self.df , last_app_line +
                                        gl_shift_home_counter_value1,
                                        gl_column_home_counter_value1)
        self.assertEqual(test, 300.111)
        test = get_home_value(self.df , last_app_line +
                                        gl_shift_home_counter_value2,
                                        gl_column_home_counter_value2)
        self.assertEqual(test, 200.222)
        # with self.assertRaises(NameError):
        #     test = gen_delta_value_home_counter(self.df , last_app_line + 1)


# ** def test_gen_Qfun_sys : 
    def test_gen_Qfun_sys(self): 
        t1, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(t1)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        test = gen_Qfun_sys(delta_value_home_counter)
        self.assertEqual(float("{:.3f}".format(test)), 3.186)


# ** def test_gen_Qmzk : 
    def test_gen_Qmzk(self): 
        t1, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(t1)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        test = gen_Qmzk(delta_value_home_counter)
        self.assertEqual(float("{:.3f}".format(test)), 6.372)


# ** def test_gen_Qroz : 
    def test_gen_Qroz(self): 
        # Питомий обсяг спожитої енергії на опалення усіх приміщень
        t1, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(t1)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        sum_heated_area = gen_sum_heated_area(t1)
        test = gen_Qroz(delta_value_home_counter, sum_heated_area)
        self.assertEqual(float("{:.4f}".format(test)), 0.0234)


# ** def test_gen_Qpit_roz : 
    def test_gen_Qpit_roz(self): 
        # питомий обсяг енергії спожитий одним розподілювачем
        # Обсяг споживання тепла з розподілювачами
        app_list, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(app_list)
        sum_heated_area = gen_sum_heated_area(app_list)
        # print("sum_heated_area=", sum_heated_area)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        # print("delta_value_home_counter=", delta_value_home_counter)
        q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
        qfun_sys = gen_Qfun_sys(delta_value_home_counter)
        # print("q_roz=", q_roz)
        q_Mkz = gen_Qmzk(delta_value_home_counter)
        # print("q_Mkz=", q_Mkz)
        q_no_surge = gen_Q_no_surge(app_list,
                                    q_roz,)
        # print("q_no_surge =", q_no_surge)
        app_list = calc_no_counter_e( app_list,
                                      q_no_surge)
        total_no_counter_e = gen_total_no_counter_e(app_list)
        test = gen_Qpit_roz(delta_value_home_counter, qfun_sys, q_Mkz, total_no_counter_e)
        # self.assertEqual(float("{:.4f}".format(test)), 0.0030)
        self.assertEqual(float("{:.13f}".format(test)), 25.962591298000700)


# ** def test_gen_Qop_min : 
    def test_gen_Qop_min(self): 
        # Мінімальна частка середнього питомого споживання
        app_list, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(app_list)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        sum_heated_area = gen_sum_heated_area(app_list)
        q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
        # print(q_roz)
        test = gen_Qop_min(q_roz)
        # self.assertEqual(test, 0.012)
        test = float("{:.9f}".format(test))
        self.assertEqual(test, 0.011696389)


# ** def test_gen_Q_no_surge : 
    def test_gen_Q_no_surge(self): 
        # Обсяг споживання тепла приміщенням без розподілювачамиів
        app_list, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(app_list)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        sum_heated_area = gen_sum_heated_area(app_list)
        q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
        # total_surge = 18.030
        test = gen_Q_no_surge(app_list,
                              q_roz,)
        test = float("{:.13f}".format(test))
        self.assertEqual(test, 0.0350891665551)


# ** def test_gen_k_no_surge : 
    def test_gen_k_no_surge(self): 
        # Обсяг споживання тепла приміщенням без розподілювачамиів
        # k = 2, якщо площа необладнаних приміщень менще 25% та 1,5 якщо більше
        app_list, t2 = populate_apps(self.df)
        test = gen_k_no_surge(app_list)
        test = float("{:.3f}".format(test))
        self.assertEqual(test, 1.5)


# ** def test_calc_surcharge : 
    def test_calc_surcharge(self): 
        app_list, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(app_list)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        sum_heated_area = gen_sum_heated_area(app_list)
        q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
        qfun_sys = gen_Qfun_sys(delta_value_home_counter)
        # print("q_roz=", q_roz)
        q_Mkz = gen_Qmzk(delta_value_home_counter)
        # print("q_Mkz=", q_Mkz)
        q_no_surge = gen_Q_no_surge(app_list,
                                    q_roz,)
        # print("q_no_surge =", q_no_surge)
        app_list = calc_no_counter_e( app_list,
                                      q_no_surge)
        total_no_counter_e = gen_total_no_counter_e(app_list)

        q_pit_roz = gen_Qpit_roz(delta_value_home_counter, qfun_sys, q_Mkz, total_no_counter_e)
        q_op_min = gen_Qop_min(q_roz)
        test = app_list[6].surcharge
        self.assertIsNone(test)
        test1 = calc_surcharge(app_list, q_pit_roz, q_op_min)
        # row 0
        test = app_list[0].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        # row 7
        test = app_list[6].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.0)
        # row 69
        test = app_list[26].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.404)
        # row 84
        test = app_list[31].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.250)
        # row 93
        test = app_list[34].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        # row 105
        test = app_list[36].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        # row 106
        test = app_list[37].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        # площа квартир якім буде повернуто об'єм донарахувань
        test = sum([app.get_S_if_surcharge() for app in app_list if app.counters_list])
        self.assertEqual(float("{:.8f}".format(test)), 1052.35)
        # обсяг енергій якій буде перерозподілено
        test = sum([app.surcharge for app in app_list])
        self.assertEqual(float("{:.3f}".format(test)), 3.085)
        # питомий обсяг енергій якій буде перерозподілено
        self.assertEqual(float("{:.9f}".format(test1)), 0.002931951)


# ** def test_recalc_surcharge : 
    def test_recalc_surcharge(self): 
        app_list, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(app_list)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        sum_heated_area = gen_sum_heated_area(app_list)
        q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
        q_no_surge = gen_Q_no_surge(app_list,
                                    q_roz,)
        app_list = calc_no_counter_e( app_list,
                                      q_no_surge)
        test = app_list[1].specified_used_E
        self.assertIsNotNone(test)
        total_no_counter_e = gen_total_no_counter_e(app_list)
        qfun_sys = gen_Qfun_sys(delta_value_home_counter)
        q_Mkz = gen_Qmzk(delta_value_home_counter)
        q_pit_roz = gen_Qpit_roz(delta_value_home_counter, qfun_sys, q_Mkz, total_no_counter_e)
        q_op_min = gen_Qop_min(q_roz)
        # row 0
        test = app_list[0].surcharge
        self.assertIsNone(test)
        e_for_redistibut = calc_surcharge(app_list, q_pit_roz, q_op_min)
        test = app_list[0].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        # row 7
        test = app_list[6].surcharge
        # self.assertIsNotNone(test)
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        # row 11
        test = app_list[8].surcharge
        self.assertIsNotNone(test)
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        # row 92
        test = app_list[34].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        # row 105
        test = app_list[37].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        # row 
        test = app_list[36].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        e_for_redistibut = recalc_surcharge(app_list,
                                            q_op_min,
                                            e_for_redistibut,
                                            times = 1
                                            # times = 200
                                            )
        # app_list[7].gen_surcharge(q_pit_roz, q_op_min)
        # self.assertIsNotNone(test)
        # row 7
        test = app_list[6].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.000)
        test = app_list[6].specified_used_E
        self.assertEqual(float("{:.3f}".format(test)), 0.933)
        # row 11
        test = app_list[8].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        test = app_list[8].specified_used_E
        self.assertEqual(float("{:.3f}".format(test)), 1.368)
        # row 92
        test = app_list[34].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.030)
        test = app_list[34].specified_used_E
        self.assertEqual(float("{:.3f}".format(test)), 1.466)
        # row 105
        test = app_list[37].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.107)
        test = app_list[37].specified_used_E
        self.assertEqual(float("{:.3f}".format(test)), 0.353)
        # row 0
        test = app_list[0].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.000)
        e_for_redistibut = recalc_surcharge(app_list,
                                            q_op_min,
                                            e_for_redistibut,
                                            # times = 1
                                            )
        self.assertEqual(float("{:.5f}".format(e_for_redistibut)) , 0)
        # row 7
        test = app_list[6].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.000)
        test = app_list[6].specified_used_E
        self.assertEqual(float("{:.3f}".format(test)), 0.917)
        # row 11
        test = app_list[8].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        test = app_list[8].specified_used_E
        self.assertEqual(float("{:.3f}".format(test)), 1.347)
        # row 92
        test = app_list[34].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.000)
        test = app_list[34].specified_used_E
        self.assertEqual(float("{:.3f}".format(test)), 1.496)
        # row 105
        test = app_list[37].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.000)
        test = app_list[37].specified_used_E
        self.assertEqual(float("{:.3f}".format(test)), 0.460)
        # row 0
        test = app_list[0].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.000)


# ** def test_gen_total_counter_e : 
    def test_gen_total_counter_e(self): 
        app_list, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(app_list)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        sum_heated_area = gen_sum_heated_area(app_list)
        q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
        qfun_sys = gen_Qfun_sys(delta_value_home_counter)
        q_Mkz = gen_Qmzk(delta_value_home_counter)
        q_no_surge = gen_Q_no_surge(app_list,
                                    q_roz,)
        app_list = calc_no_counter_e( app_list,
                                      q_no_surge)
        total_no_counter_e = gen_total_no_counter_e(app_list)

        q_pit_roz = gen_Qpit_roz(delta_value_home_counter, qfun_sys, q_Mkz, total_no_counter_e)
        q_op_min = gen_Qop_min(q_roz)
        test = app_list[6].surcharge
        self.assertIsNone(test)
        e_for_redistibut = calc_surcharge(app_list, q_pit_roz, q_op_min)
        e_for_redistibut = recalc_surcharge(app_list,
                                            q_op_min,
                                            e_for_redistibut,
                                            times = 1
                                            # times = 200
                                            )
        # Ітого по распр., Гкал
        test = gen_total_counter_e(app_list)
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 25.963)


# ** def test_gen_total_no_counter_e : 
    def test_gen_total_no_counter_e(self): 
        app_list, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(app_list)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        sum_heated_area = gen_sum_heated_area(app_list)
        q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
        q_no_surge = gen_Q_no_surge(app_list,
                                    q_roz,)
        # Ітого по распр., Гкал
        # test = app_list[1].specified_used_E
        # self.assertIsNone(test)
        app_list = calc_no_counter_e( app_list,
                                      q_no_surge)
        test = app_list[1].specified_used_E
        self.assertIsNotNone(test)
        test = gen_total_no_counter_e(app_list)
        self.assertEqual(float("{:.3f}".format(test)), 28.199)


# ** def test_calc_no_counter_e : 
    def test_calc_no_counter_e(self): 
        app_list, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(app_list)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        sum_heated_area = gen_sum_heated_area(app_list)
        q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
        # Ітого по м2, Гкал
        # q_no_surge = 0.044960013
        q_no_surge = gen_Q_no_surge(app_list,
                                    q_roz,)
        app_list = calc_no_counter_e( app_list,
                                      q_no_surge)
        # row 2
        test = app_list[0].specified_used_E
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 2.081)
        # test total
        test = app_list[0].specified_used_E
        test = sum([app.specified_used_E for app in app_list if not app.counters_list])
        self.assertEqual(float("{:.3f}".format(test)), 28.199)


# ** def test_calc_final_totals : 
    def test_calc_final_totals(self): 
        app_list, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(app_list)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        sum_heated_area = gen_sum_heated_area(app_list)
        q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
        qfun_sys = gen_Qfun_sys(delta_value_home_counter)
        # print("q_roz=", q_roz)
        q_Mkz = gen_Qmzk(delta_value_home_counter)
        # print("q_Mkz=", q_Mkz)
        q_no_surge = gen_Q_no_surge(app_list,
                                    q_roz,)
        # print("q_no_surge =", q_no_surge)
        app_list = calc_no_counter_e( app_list,
                                      q_no_surge)
        total_no_counter_e = gen_total_no_counter_e(app_list)

        q_pit_roz = gen_Qpit_roz(delta_value_home_counter, qfun_sys, q_Mkz, total_no_counter_e)
        q_op_min = gen_Qop_min(q_roz)
        test = app_list[6].surcharge
        self.assertIsNone(test)
        e_for_redistibut = calc_surcharge(app_list, q_pit_roz, q_op_min)
        # print(q_op_min)
        # print(e_for_redistibut)
        # e_for_redistibut = 0.003998048
        e_for_redistibut = recalc_surcharge(app_list,
                                            q_op_min,
                                            e_for_redistibut,
                                            times = 1
                                            # times = 200
                                            )
        # print(e_for_redistibut)
        # e_for_redistibut = 0.242
        e_for_redistibut = recalc_surcharge(app_list,
                                            q_op_min,
                                            e_for_redistibut,
                                            times = 1
                                            # times = 200
                                            )
        # print(e_for_redistibut)
        test = app_list[6].specified_used_E
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.922)
        # qfun_sys = 3.186
        # qfun_sys = gen_Qfun_sys(delta_value_home_counter)
        # print(qfun_sys)
        # q_Mkz = 6.372
        # q_Mkz = gen_Qmzk(delta_value_home_counter)
        # print(q_Mkz)
        # total_counter_e = 18.030
        # total_counter_e = gen_total_counter_e(app_list)
        # print(total_counter_e)
        # q_no_surge = 0.044960013
        # q_no_surge = gen_Q_no_surge(total_counter_e,
        #                             q_Mkz,
        #                             delta_value_home_counter,
        #                             gen_no_counter_sum_area(app_list))
        # print(q_no_surge)
        # calc_no_counter_e(app_list,
        #                   q_no_surge)
        # calculate columns in app_list
        # функціонування системи
        # МЗК
        # ВСЬОГО, Гкал
        # app_list[13].specified_used_E = 0.573
        calc_final_totals( app_list,
                           qfun_sys,
                           q_Mkz,
                           sum_heated_area)
        # row 2
        test = app_list[0].specified_used_E
        self.assertEqual(float("{:.3f}".format(test)), 2.081)
        # функціонування системи
        test = app_list[0].total_fun_sys
        self.assertEqual(float("{:.3f}".format(test)), 0.082)
        # МЗК
        test = app_list[0].total_Mkz
        self.assertEqual(float("{:.3f}".format(test)), 0.163)
        # ВСЬОГО, Гкал
        test = app_list[0].total_e
        self.assertEqual(float("{:.3f}".format(test)), 2.326)
        # row 26
        test = app_list[13].specified_used_E
        self.assertEqual(float("{:.3f}".format(test)), 0.595)
        # функціонування системи
        test = app_list[13].total_fun_sys
        self.assertEqual(float("{:.3f}".format(test)), 0.070)
        # МЗК
        test = app_list[13].total_Mkz
        self.assertEqual(float("{:.3f}".format(test)), 0.140)
        # ВСЬОГО, Гкал
        test = app_list[13].total_e
        self.assertEqual(float("{:.3f}".format(test)), 0.805)
        # test total
        test = sum([app.specified_used_E for app in app_list if not app.counters_list])
        self.assertEqual(float("{:.3f}".format(test)), 28.199)
        # функціонування системи
        test = sum([app.total_fun_sys for app in app_list])
        self.assertEqual(float("{:.3f}".format(test)), 3.186)
        # МЗК
        test = sum([app.total_Mkz for app in app_list])
        self.assertEqual(float("{:.3f}".format(test)), 	6.372)
        # ВСЬОГО, Гкал
        test = sum([app.total_e for app in app_list])
        # print([app.total_e for app in app_list])
        self.assertEqual(float("{:.3f}".format(test)), 	63.720)


# ** ------------------------------------------:
# * Test runer : 
# ** ------------------------------------------:
# (compile " D:/Development/version-control/GitHub/Vadim/Tochil/main_test.py -k init")
# (compile " python -m unittest D:/Development/version-control/GitHub/Vadim/Tochil/main_test.py ")
# ** if __main__: 
if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(suite_Init())
    unittest.main()


# ----------------------------------------------
# * -------------------------------------------:
