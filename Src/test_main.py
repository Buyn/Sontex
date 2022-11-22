# ----------------------------------------------
# * import block :
import unittest

from main import *

# filename = gv_filename
# sheet_name = gv_sheet_name 


# ----------------------------------------------
# * class Test_Init : 
# ** ------------------------------------------:
class Test_Init(unittest.TestCase):

# ----------------------------------------------
# ** def test_main : 
    def test_main(self):# {{{
        # print("Test tuner")
        # self.assertIsNone(main(1))
        # global gv_filename, sheet_name
        # gv_filename = "Data_files/test.xlsx"
        # # sheet_name = "показники"
        # sheet_name = "квартири, площі"
        # df = load_exel(gv_filename, sheet_name)
        # app_list, couters_list = populate_apps(df) 
        # # загальна площа будинку
        # sum_heated_area = gen_sum_heated_area(app_list)
        # last_app_line = get_last_app_line(app_list)
        # # по будинку за т/ліч
        # delta_value_home_counter = get_delta_value_home_counter(df, last_app_line)
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
        filename = gv_filename
        sheet_name = gv_sheet_name 
        # self.assertEqual(filename, "Data_files/metod01.xlsx")
        argv = ["main path", 
                "--filename=Data_files/test.xlsx",
                "--sheet_name=квартири, площі"]
        filename, sheet_name = cmd_line_arg(argv, filename, sheet_name)
        self.assertEqual(filename, "Data_files/test.xlsx")
        self.assertEqual(sheet_name, "квартири, площі")

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
        self.assertEqual(float("{:.4f}".format(test)), 0.0030)


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


# ** def test_calc_on_globals_for_couters : 
    def test_calc_on_globals_for_couters(self): 
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
        app_list_t = calc_on_globals_for_couters(app_list, q_pit_roz, q_op_min)
        # app_list[7].gen_surcharge(q_pit_roz, q_op_min)
        # self.assertIsNotNone(test)
        # row 7
        test = app_list[6].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.002)
        test = app_list_t[6].surcharge
        self.assertIsNotNone(test)
        self.assertEqual(float("{:.3f}".format(test)), 0.002)
        # row 105
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
