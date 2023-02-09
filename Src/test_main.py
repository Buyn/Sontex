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
                "--sheet_name=квартири, площі"])
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


# ** def test_gen_sum_heated_area : 
    def test_gen_sum_heated_area(self): 
        t1, t2 = populate_apps(self.df)
        test = gen_sum_heated_area(t1)
        self.assertEqual(float("{:.3f}".format(test)) , 2315.33)


# ** def test_gen_sum_area : 
    def test_gen_sum_area(self): 
        t1, t2 = populate_apps(self.df)
        test = gen_sum_area(t1)
        self.assertEqual(float("{:.3f}".format(test)) , 2412.77)


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


# ** test_get_find_most_heated_app : 
    def test_get_find_most_heated_app(self):
        t1, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(t1)
        test = find_most_heated_app(t1)
        self.assertEqual(test, 24)
        with self.assertRaises(NameError):
            test = get_delta_value_home_counter(self.df , last_app_line + 1)


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


# ** def test_gen_Qmax_roz : 
    def test_gen_Qmax_roz(self): 
        # Обсяг споживання тепла з найбільшим показником по розподілювачам
        app_list, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(app_list)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        sum_heated_area = gen_sum_heated_area(app_list)
        q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
        index_most_heated_app = find_most_heated_app(app_list)
        test = gen_Qmax_roz(app_list, q_roz, index_most_heated_app)
        self.assertEqual(float("{:.4f}".format(test)), 1.5914)


# ** def test_gen_Qpit_roz : 
    def test_gen_Qpit_roz(self): 
        # питомий обсяг енергії спожитий одним розподілювачем
        app_list, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(app_list)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        sum_heated_area = gen_sum_heated_area(app_list)
        q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
        index_most_heated_app = find_most_heated_app(app_list)
        test = gen_Qpit_roz(app_list, q_roz, index_most_heated_app)
        # self.assertEqual(float("{:.4f}".format(test)), 0.0030)
        self.assertEqual(float("{:.4f}".format(test)), 25.962591298000700)


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
        # q_Mkz = gen_Q_Mkz(delta_value_home_counter)
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
        index_most_heated_app = find_most_heated_app(app_list)
        q_pit_roz = gen_Qpit_roz(app_list, q_roz, index_most_heated_app)
        q_op_min = gen_Qop_min(q_roz)
        test = app_list[6].surcharge
        self.assertIsNone(test)
        test1 = calc_surcharge(app_list, q_pit_roz, q_op_min)
        # row 7
        test = app_list[6].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.0)
        # row 84
        test = app_list[31].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.003916362)
        # row 69
        test = app_list[26].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.00689428)
        # row 106
        test = app_list[37].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        # row 93
        test = app_list[34].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        # row 0
        test = app_list[0].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        test = app_list[36].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        # площа квартир якім буде повернуто об'єм донарахувань
        test = sum([app.get_S_if_surcharge() for app in app_list])
        self.assertEqual(float("{:.8f}".format(test)), 1390.40)
        # обсяг енергій якій буде перерозподілено
        test = sum([app.surcharge for app in app_list])
        self.assertEqual(float("{:.9f}".format(test)), 5.558885361)
        # питомий обсяг енергій якій буде перерозподілено
        self.assertEqual(float("{:.9f}".format(test1)), 0.003998048)


# ** def test_recalc_surcharge : 
    def test_recalc_surcharge(self): 
        app_list, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(app_list)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        sum_heated_area = gen_sum_heated_area(app_list)
        q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
        index_most_heated_app = find_most_heated_app(app_list)
        q_pit_roz = gen_Qpit_roz(app_list, q_roz, index_most_heated_app)
        q_op_min = gen_Qop_min(q_roz)
        test = app_list[6].surcharge
        self.assertIsNone(test)
        e_for_redistibut = calc_surcharge(app_list, q_pit_roz, q_op_min)
        test = app_list[6].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.002)
        test = app_list[37].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.199)
        # row 92
        test = app_list[34].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.470)
        # row 0
        test = app_list[0].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0)
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
        self.assertEqual(float("{:.3f}".format(test)), 0.607)
        # row 11
        test = app_list[8].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.194)
        test = app_list[8].specified_used_E
        self.assertEqual(float("{:.9f}".format(test)), 0.601662513)
        # row 105
        test = app_list[37].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.000)
        test = app_list[37].specified_used_E
        self.assertEqual(float("{:.3f}".format(test)), 0.460)
        # row 92
        test = app_list[34].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.000)
        test = app_list[34].specified_used_E
        self.assertEqual(float("{:.3f}".format(test)), 1.496)
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
        self.assertEqual(float("{:.3f}".format(test)), 0.607)
        # row 11
        test = app_list[8].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        test = app_list[8].specified_used_E
        self.assertEqual(float("{:.3f}".format(test)), 0.796)
        # row 105
        test = app_list[37].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.000)
        test = app_list[37].specified_used_E
        self.assertEqual(float("{:.3f}".format(test)), 0.460)
        # row 92
        test = app_list[34].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.000)
        test = app_list[34].specified_used_E
        self.assertEqual(float("{:.3f}".format(test)), 1.496)
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
        index_most_heated_app = find_most_heated_app(app_list)
        q_pit_roz = gen_Qpit_roz(app_list, q_roz, index_most_heated_app)
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
        self.assertEqual(float("{:.3f}".format(test)), 17.681)


# ** def test_gen_total_no_counter_e : 
    def test_gen_total_no_counter_e(self): 
        app_list, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(app_list)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        sum_heated_area = gen_sum_heated_area(app_list)
        q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
        q_no_surge = gen_Q_no_surge(app_list,
                                    q_roz,)
        index_most_heated_app = find_most_heated_app(app_list)
        q_pit_roz = gen_Qpit_roz(app_list, q_roz, index_most_heated_app)
        # q_op_min = gen_Qop_min(q_roz)
        # Ітого по распр., Гкал
        # test = app_list[1].specified_used_E
        # self.assertIsNone(test)
        calc_no_counter_e(app_list,
                          q_no_surge)
        test = app_list[1].specified_used_E
        self.assertIsNotNone(test)
        test = gen_total_no_counter_e(app_list)
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 28.199)


# ** def test_calc_no_counter_e : 
    def test_calc_no_counter_e(self): 
        app_list, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(app_list)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        sum_heated_area = gen_sum_heated_area(app_list)
        q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
        index_most_heated_app = find_most_heated_app(app_list)
        q_pit_roz = gen_Qpit_roz(app_list, q_roz, index_most_heated_app)
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
        # Ітого по м2, Гкал
        q_no_surge = 0.044960013
        calc_no_counter_e(app_list,
                          q_no_surge)
        # row 2
        test = app_list[0].specified_used_E
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 2.666)
        # test total
        test = app_list[0].specified_used_E
        test = sum([app.specified_used_E for app in app_list if not app.counters_list])
        self.assertEqual(float("{:.3f}".format(test)), 36.132)


# ** def test_calc_final_totals : 
    def test_calc_final_totals(self): 
        app_list, t2 = populate_apps(self.df)
        last_app_line = get_last_app_line(app_list)
        delta_value_home_counter = gen_delta_value_home_counter(self.df, last_app_line)
        sum_heated_area = gen_sum_heated_area(app_list)
        q_roz = gen_Qroz(delta_value_home_counter, sum_heated_area)
        index_most_heated_app = find_most_heated_app(app_list)
        q_pit_roz = gen_Qpit_roz(app_list, q_roz, index_most_heated_app)
        q_op_min = gen_Qop_min(q_roz)
        test = app_list[6].surcharge
        self.assertIsNone(test)
        # print(e_for_redistibut)
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
        e_for_redistibut = 4.337E-04
        e_for_redistibut = recalc_surcharge(app_list,
                                            q_op_min,
                                            e_for_redistibut,
                                            times = 1
                                            # times = 200
                                            )
        # print(e_for_redistibut)
        test = app_list[6].specified_used_E
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.585)
        # qfun_sys = 3.186
        qfun_sys = gen_Qfun_sys(delta_value_home_counter)
        # print(qfun_sys)
        # q_Mkz = 6.372
        q_Mkz = gen_Qmzk(delta_value_home_counter)
        # print(q_Mkz)
        total_counter_e = 18.030
        # total_counter_e = gen_total_counter_e(app_list)
        # print(total_counter_e)
        q_no_surge = 0.044960013
        # q_no_surge = gen_Q_no_surge(total_counter_e,
        #                             q_Mkz,
        #                             delta_value_home_counter,
        #                             gen_no_counter_sum_area(app_list))
        # print(q_no_surge)
        calc_no_counter_e(app_list,
                          q_no_surge)
        # calculate columns in app_list
        # функціонування системи
        # МЗК
        # ВСЬОГО, Гкал
        app_list[13].specified_used_E = 0.573
        calc_final_totals( app_list,
                           qfun_sys,
                           q_Mkz,
                           sum_heated_area)
        # row 2
        test = app_list[0].specified_used_E
        self.assertEqual(float("{:.3f}".format(test)), 2.666)
        # функціонування системи
        test = app_list[0].total_fun_sys
        self.assertEqual(float("{:.3f}".format(test)), 0.082)
        # МЗК
        test = app_list[0].total_Mkz
        self.assertEqual(float("{:.3f}".format(test)), 0.163)
        # ВСЬОГО, Гкал
        test = app_list[0].total_e
        self.assertEqual(float("{:.3f}".format(test)), 2.911)
        # row 26
        test = app_list[13].specified_used_E
        self.assertEqual(float("{:.3f}".format(test)), 0.573)
        # функціонування системи
        test = app_list[13].total_fun_sys
        self.assertEqual(float("{:.3f}".format(test)), 0.070)
        # МЗК
        test = app_list[13].total_Mkz
        self.assertEqual(float("{:.3f}".format(test)), 0.140)
        # ВСЬОГО, Гкал
        test = app_list[13].total_e
        self.assertEqual(float("{:.3f}".format(test)), 0.783)
        # test total
        test = sum([app.specified_used_E for app in app_list if not app.counters_list])
        self.assertEqual(float("{:.3f}".format(test)), 36.132)
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
