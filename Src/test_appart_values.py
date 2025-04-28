import unittest
from appart_values import *

class setUp_Test(unittest.TestCase):

    @classmethod #setUpClass# {{{
    def setUpClass(self):
        # print("*"*33,"*"*33)
        gv_filename = "Data_files/test.xlsx"
        # sheet_name = "показники"
        sheet_name = "квартири, площі"
        # self.df = load_exel(gv_filename, sheet_name)
        import pandas as pd
        self.df = pd.read_excel(gv_filename,
                          sheet_name = sheet_name,
                          engine='openpyxl',
                          # index_col=0,
                          header=None,
                          )

    def test_init1(self):# {{{
        # self.assertIsNone( test._df)
        test = Appart_values(self.df, 2) 
        self.assertEqual(test._start_line, 2)
        # self.assertEqual(test._df, self.df)
        self.assertIsNotNone( test._df)
        test = Appart_values(self.df, 11) 
        self.assertEqual(test._start_line, 11)
        self.assertEqual(test.next_app_line, 15)
        self.assertEqual([x.adress for x in test.counters_list],
                         [25482324, 25482310, 25482309, 25482325,])
        test = Appart_values(self.df, 7) 
        self.assertEqual(test._start_line, 7)
        self.assertEqual(test.next_app_line, 10)
        self.assertEqual([x.adress for x in test.counters_list],
                         [25482311, 25482312, 25482313,])

    def test_get_next_appindex(self): 
        test = Appart_values(self.df, 2)
        r1,r2 = test.get_next_appindex(2)
        self.assertEqual(r1, 3)
        self.assertFalse(r2)
        r1,r2 = test.get_next_appindex(63)
        self.assertEqual(r1, 68)
        self.assertFalse(r2)
        r1,r2 = test.get_next_appindex(106)
        self.assertEqual(r1, 107)
        self.assertTrue(r2)
        r1,r2 = test.get_next_appindex(111)
        self.assertEqual(r1, -1)
        self.assertIsNone(r2)

    def test_is_starting_line(self): 
        test = Appart_values(self.df, 2)
        # print(self.df.iloc[2, 0])
        self.assertTrue(test.is_starting_line(2))
        # print(self.df.iloc[14, 0])
        self.assertFalse(test.is_starting_line(14))
        self.assertFalse(test.is_starting_line(107))

    def test_get_counters(self): 
        test = Appart_values(self.df, 2)
        self.assertEqual([x.adress for x in test.get_counters_list(100,104)]
                         , [25482671,
                             25482670,
                             25482669,
                             25482694,])
        self.assertEqual(test.get_counters_list(2,3)
                         , None)
        self.assertEqual(test.get_counters_list(87,88)
                         , None)
        self.assertEqual([x.adress for x in test.get_counters_list(7,10)]
                         , [ 25482311,
                             25482312,
                             25482313,
                            ])
        with self.assertRaises(NameError):
            test.get_counters_list(20,25)
            # test.get_counters_list(87,88)

    def test_gen_counters_adress(self): 
        test = Appart_values(self.df, 100)
        self.assertEqual(test.gen_counters_adress()
                         , [25482671,
                             25482670,
                             25482669,
                             25482694,])
        test = Appart_values(self.df, 7)
        self.assertEqual(test.gen_counters_adress()
                         , [ 25482311,
                             25482312,
                             25482313,
                            ])

    def test_load_values(self): 
        test = Appart_values(self.df, 7)
        test.load_values()
        self.assertEqual(test.heating_area, 51.9)
        # self.assertEqual(test.sum_area, 55.7)
        test = Appart_values(self.df, 6)
        test.load_values()
        self.assertEqual(test.heating_area, 52)
        # self.assertEqual(test.sum_area, 56.70)
        test = Appart_values(self.df, 84)
        test.load_values()
        self.assertEqual(test.heating_area, 52.10)
        # self.assertEqual(test.sum_area, 56.60)
        with self.assertRaises(NameError):
            test = Appart_values(self.df, 131)
            test.load_values()
            print(test.heating_area)
            # print(test.sum_area)
            print("tupe is =", type(test.sum_area))
            print("tupe is =",type(test.heating_area))
        with self.assertRaises(NameError):
            test = Appart_values(self.df, 132)
            test.load_values()
            print(test.heating_area)
            # print(test.sum_area)
            print("tupe is =", type(test.sum_area))
            print("tupe is =",type(test.heating_area))
        with self.assertRaises(NameError):
            test = Appart_values(self.df, 133)
            test.load_values()
            print(test.heating_area)
            # print(test.sum_area)
            print("tupe is =", type(test.sum_area))
            print("tupe is =",type(test.heating_area))

    def test_load_value(self): 
        test = Appart_values(self.df, 7)
        # row =  [ gl_app_sum_area_column,
        #           gl_app_heating_area_column]
        # text = [ "gl_app_sum_area_column",
        #           "gl_app_heating_area_column"]
        t = test.load_value(gl_app_heating_area_column, "gl_app_heating_area_column")
        self.assertEqual(t, 51.9)
        self.assertEqual(test.heating_area, 51.9)
        test = Appart_values(self.df, 6)
        t = test.load_value(gl_app_heating_area_column, "gl_app_heating_area_column")
        self.assertEqual(t, 52)
        self.assertEqual(test.heating_area, 52)
        # self.assertEqual(test.sum_area, 56.70)
        test = Appart_values(self.df, 84)
        t = test.load_value(gl_app_heating_area_column, "gl_app_heating_area_column")
        self.assertEqual(t, 52.10)
        self.assertEqual(test.heating_area, 52.10)
        # self.assertEqual(test.sum_area, 56.60)
        with self.assertRaises(NameError):
            test = Appart_values(self.df, 131)
            t = test.load_value(gl_app_heating_area_column, "gl_app_heating_area_column")
            print(test.heating_area)
            # print(test.sum_area)
            print("tupe is =", type(test.sum_area))
            print("tupe is =",type(test.heating_area))
        with self.assertRaises(NameError):
            test = Appart_values(self.df, 132)
            t = test.load_value(gl_app_heating_area_column, "gl_app_heating_area_column")
            print(test.heating_area)
            # print(test.sum_area)
            print("tupe is =", type(test.sum_area))
            print("tupe is =",type(test.heating_area))
        with self.assertRaises(NameError):
            test = Appart_values(self.df, 133)
            t = test.load_value(gl_app_heating_area_column, "gl_app_heating_area_column")
            print(test.heating_area)
            # print(test.sum_area)
            print("tupe is =", type(test.sum_area))
            print("tupe is =",type(test.heating_area))

    def test_load_name(self): 
        # print("p = ", self.df.iloc[2, gl_num_column])    
        test = Appart_values(self.df, 7)
        t = test.load_name(gl_num_column, "gn_num_column")
        self.assertEqual(t, 7)
        t = test.load_name(gl_app_num_column, "gn_app_num_column")
        self.assertEqual(t, "кв.7")
        test = Appart_values(self.df, 6)
        t = test.load_name(gl_num_column, "gn_num_column")
        self.assertEqual(t, 6)
        t = test.load_name(gl_app_num_column, "gn_app_num_column")
        self.assertEqual(t, "кв.6")
        # self.assertEqual(test.sum_area, 56.70)
        test = Appart_values(self.df, 84)
        t = test.load_name(gl_num_column, "gn_num_column")
        self.assertEqual(t, 32)
        t = test.load_name(gl_app_num_column, "gn_app_num_column")
        self.assertEqual(t, "кв.32")
        # self.assertEqual(test.sum_area, 56.60)

    def test_update_allvalues1_by_id(self): 
        gv_filename = gv_csv
        # df_csv = load_csv(gv_filename)
        df_csv = pd.read_csv(gv_csv ,
                              encoding = gv_csv_encoding,
                              header = gv_csv_header,
                              sep = gv_csv_sep,
                              index_col = gv_csv_index_col)
        name_date = gv_csv_name_date + str(gv_csv_name_i)
        name_value = gv_csv_name_value + str(gv_csv_name_i)
        test = Appart_values(self.df, 7)
        self.assertEqual(test.counters_list[0].value1, 653)
        test.update_allvalues1_by_id(df_csv,  name_value, name_date)
        self.assertEqual(test.counters_list[0].value1, 126)
        self.assertEqual(test.counters_list[0].get_value1(), 126)
        # rlv
        gv_filename = gv_rlv
        df_csv = pd.read_csv(gv_filename ,
                              encoding = gv_rlv_encoding,
                              header = gv_rlv_header,
                              sep = gv_rlv_sep,
                              index_col = gv_rlv_index_col)
        # df = pd.read_csv(filename ,
                        # encoding = gv_rlv_encoding,
                        # header = gv_rlv_header,
                        # sep = gv_rlv_sep,
                        # index_col = gv_rlv_index_col)
        # df_csv = load_rlv(gv_filename)
        name_date = gv_csv_name_date + str(gv_csv_name_i)
        name_value = gv_csv_name_value + str(gv_csv_name_i)
        # name_date = gv_rlv_name_date + str(gv_rlv_name_i)
        # name_value = gv_rlv_name_value + str(gv_rlv_name_i)
        test = Appart_values(self.df, 7)
        # print(test.counters_list[0])
        self.assertEqual(test.counters_list[0].value1, 126)
        test.update_allvalues1_by_id(df_csv,  name_value, name_date)
        self.assertEqual(test.counters_list[0].value1, 126)
        self.assertEqual(test.counters_list[0].get_value1(), 126)

    def test_update_allvalues2_by_id(self): 
        gv_filename = gv_csv
        # df_csv = load_csv(gv_filename)
        df_csv = pd.read_csv(gv_csv ,
                              encoding = gv_csv_encoding,
                              header = gv_csv_header,
                              sep = gv_csv_sep,
                              index_col = gv_csv_index_col)
        name_date = gv_csv_name_date + str(gv_csv_name_i)
        name_value = gv_csv_name_value + str(gv_csv_name_i)
        # name_value = gv_csv_name_value + str(2)
        test = Appart_values(self.df, 7)
        self.assertEqual(test.counters_list[0].value2, 603)
        test.update_allvalues2_by_id(df_csv,  name_value, name_date)
        self.assertEqual(test.counters_list[0].value2, 126)
        self.assertEqual(test.counters_list[0].get_value2(), 126)
        # rlv
        gv_filename = gv_rlv
        df_csv = pd.read_csv(gv_filename ,
                              encoding = gv_rlv_encoding,
                              header = gv_rlv_header,
                              sep = gv_rlv_sep,
                              index_col = gv_rlv_index_col)
        # df = pd.read_csv(filename ,
                        # encoding = gv_rlv_encoding,
                        # header = gv_rlv_header,
                        # sep = gv_rlv_sep,
                        # index_col = gv_rlv_index_col)
        # df_csv = load_rlv(gv_filename)
        name_date = gv_csv_name_date + str(gv_csv_name_i)
        name_value = gv_csv_name_value + str(gv_csv_name_i)
        # name_value = gv_csv_name_value + "3"
        # name_date = gv_rlv_name_date + str(gv_rlv_name_i)
        # name_value = gv_rlv_name_value + str(gv_rlv_name_i)
        test = Appart_values(self.df, 7)
        # print(test.counters_list[0])
        self.assertEqual(test.counters_list[0].value2, 126)
        test.update_allvalues2_by_id(df_csv,  name_value, name_date)
        self.assertEqual(test.counters_list[0].value2, 126)
        self.assertEqual(test.counters_list[0].get_value2(), 126)

    def test_gen_E_used(self):
        # сумарне споживання по квартирі, од.
        test = Appart_values(self.df, 7)
        self.assertEqual(test.gen_E_used(), 112)
        test = Appart_values(self.df, 84)
        self.assertEqual(test.gen_E_used(), 44)
        test = Appart_values(self.df, 69)
        self.assertEqual(test.gen_E_used(), 39)

    def test_gen_E_used_k(self):
        # сумарне споживання по квартирі, од.
        test = Appart_values(self.df, 7)
        self.assertEqual(float("{:.2f}".format(test.gen_E_used_k())), 201.61)
        test = Appart_values(self.df, 69)
        self.assertEqual(float("{:.2f}".format(test.gen_E_used_k())), 37.76)
        test = Appart_values(self.df, 84)
        self.assertEqual(float("{:.2f}".format(test.gen_E_used_k())), 66.73)

    def test_gen_k_to_s(self):
        # приведене до м2 площі, од/м2
        app = Appart_values(self.df, 7)
        test = app.gen_k_to_s()
        # self.assertEqual(float("{:.3f}".format(test.gen_k_to_s())), 3.885)
        self.assertEqual(float("{:.3f}".format(test)), 3.885)
        app = Appart_values(self.df, 69)
        # print("gen_use_for_period(q_pit_roz)", app.gen_E_used_k())
        # print("heating_area ", app.heating_area)
        test = app.gen_k_to_s()
        self.assertEqual(float("{:.3f}".format(test)), 0.728)
        app = Appart_values(self.df, 84)
        test = app.gen_k_to_s()
        self.assertEqual(float("{:.3f}".format(test)), 1.281)

    def test_gen_use_for_period(self):
        # обсяг споживання за період, Гкал
        app = Appart_values(self.df, 7)
        # q_pit_roz = 0.00299979010123
        q_pit_roz = 25.962591298
        sum_e_used_k = 4823.121
        test = app.gen_use_for_period(q_pit_roz, sum_e_used_k)
        # self.assertEqual(float("{:.3f}".format(test)), 0.605)
        # 1.085
        # self.assertEqual(float("{:.9f}".format(test)), 1.085)
        self.assertEqual(float("{:.3f}".format(test)), 1.085)
        app = Appart_values(self.df, 69)
        test = app.gen_use_for_period(q_pit_roz, sum_e_used_k)
        # self.assertEqual(float("{:.3f}".format(test)), 0.113)
        # 0.203
        # self.assertEqual(float("{:.10f}".format(test)), 0.203)
        self.assertEqual(float("{:.3f}".format(test)), 0.203)
        app = Appart_values(self.df, 84)
        test = app.gen_use_for_period(q_pit_roz, sum_e_used_k)
        # 0.359
        self.assertEqual(float("{:.3f}".format(test)), 0.359)

    def test_gen_priv2S(self):
        # приведене до м2 площі, Гкал/м2
        app = Appart_values(self.df, 7)
        # q_pit_roz = 0.00299979010123
        q_pit_roz = 25.962591298000700
        sum_e_used_k = 4823.121
        test = app.gen_priv2S(q_pit_roz, sum_e_used_k)
        self.assertEqual(float("{:.9f}".format(test)), 0.020910666)
        app = Appart_values(self.df, 69)
        # print("gen_use_for_period(q_pit_roz)", app.gen_E_used_k())
        # print("heating_area ", app.heating_area)
        test = app.gen_priv2S(q_pit_roz, sum_e_used_k)
        self.assertEqual(float("{:.9f}".format(test)), 0.003916363)
        app = Appart_values(self.df, 84)
        test = app.gen_priv2S(q_pit_roz, sum_e_used_k)
        # print("gen_E_used_k()", app.gen_E_used_k())
        # print("gen_use_for_period(q_pit_roz)", app.gen_use_for_period(q_pit_roz))
        self.assertEqual(float("{:.8f}".format(test)), 0.00689428)

    def test_gen_surcharge(self):
        # донарахування, Гкал
        app = Appart_values(self.df, 7)
        # q_pit_roz = 0.0030
        # q_pit_roz = 25.962591298000700
        q_pit_roz = 25.962591298000700
        q_op_min = 0.011696388851697
        sum_e_used_k = 4823.121
        self.assertIsNone(app.surcharge)
        test = app.gen_surcharge(q_pit_roz, q_op_min, sum_e_used_k)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        app = Appart_values(self.df, 69)
        self.assertIsNone(app.surcharge)
        test = app.gen_surcharge(q_pit_roz, q_op_min, sum_e_used_k)
        self.assertEqual(float("{:.3f}".format(test)), 0.404)
        app = Appart_values(self.df, 84)
        self.assertIsNone(app.surcharge)
        test = app.gen_surcharge(q_pit_roz, q_op_min, sum_e_used_k)
        self.assertEqual(float("{:.3f}".format(test)), 0.250)

    def test_get_S_if_surcharge(self):
        # донарахування, Гкал
        app = Appart_values(self.df, 7)
        q_pit_roz = 25.962591298000700
        q_op_min = 0.011696389
        sum_e_used_k = 4823.121
        test = app.gen_surcharge(q_pit_roz, q_op_min, sum_e_used_k)
        # print(test)
        test = app.get_S_if_surcharge()
        self.assertEqual(float("{:.3f}".format(test)), 51.90)
        app = Appart_values(self.df, 11)
        test = app.gen_surcharge(q_pit_roz, q_op_min, sum_e_used_k)
        test = app.get_S_if_surcharge()
        self.assertEqual(float("{:.3f}".format(test)), 68.03)
        app = Appart_values(self.df, 19)
        test = app.gen_surcharge(q_pit_roz, q_op_min, sum_e_used_k)
        test = app.get_S_if_surcharge()
        self.assertEqual(float("{:.3f}".format(test)), 0.00)

    def test_gen_specified_used_E(self):
        # донарахування, Гкал
        # app 7
        app = Appart_values(self.df, 7)
        q_pit_roz = 25.962591298000700
        q_op_min = 0.011696388851697
        sum_e_used_k = 4823.121
        e_for_redistibut = 0.002931951
        test = app.gen_surcharge(q_pit_roz, q_op_min, sum_e_used_k)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        test = app.gen_specified_used_E(e_for_redistibut)
        # print(app.gen_specified_priv2S())
        # print(app.get_S_if_surcharge())
        self.assertEqual(float("{:.3f}".format(test)), 0.933)
        # print(app.specified_used_E)
        # print(app.heating_area)
        test = app.gen_specified_priv2S()
        self.assertEqual(float("{:.9f}".format(test)), 0.017978715)
        test = app.gen_specified_surcharge(q_op_min)
        # print(e_for_redistibut)
        # print(app.specified_used_E)
        self.assertEqual(float("{:.9f}".format(test)), 0)
        # second Total for app in row 7
        e_for_redistibut = 1.981E-04
        # print(app.surcharge) 
        test = app.gen_specified_used_E(e_for_redistibut)
        # print(app.surcharge) 
        self.assertEqual(float("{:.3f}".format(test)), 0.923)
        # print(e_for_redistibut)
        test = app.gen_specified_priv2S()
        self.assertEqual(float("{:.7f}".format(test)), 0.0177806)
        test = app.gen_specified_surcharge(q_op_min)
        # print(app.gen_specified_priv2S())
        # print(q_op_min)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        # app 11
        e_for_redistibut = 0.002931951
        app = Appart_values(self.df, 11)
        sum_e_used_k = 4823.121
        test = app.gen_surcharge(q_pit_roz, q_op_min, sum_e_used_k)
        test = app.gen_specified_used_E(e_for_redistibut)
        # self.assertEqual(float("{:.3f}".format(test)), 0.602)
        self.assertEqual(float("{:.3f}".format(test)), 1.368)
        # print(app.heating_area)
        test = app.gen_specified_priv2S()
        self.assertEqual(float("{:.8f}".format(test)), 0.02011247)
        test = app.gen_specified_surcharge(q_op_min)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        test = app.get_S_if_surcharge()
        self.assertEqual(float("{:.3f}".format(test)), 68.03)
        # test = app.gen_specified_used_E(e_for_redistibut, q_pit_roz)
        # second Total for app in row 11
        e_for_redistibut = 1.981E-04
        # print(app.surcharge) 
        test = app.gen_specified_used_E(e_for_redistibut)
        # print(app.surcharge) 
        self.assertEqual(float("{:.3f}".format(test)), 1.355)
        # print(e_for_redistibut)
        test = app.gen_specified_surcharge(q_op_min)
        self.assertEqual(float("{:.3f}".format(test)), 0)

    def test_gen_no_counter_e(self):
        q_no_surge = 0.044960013
        # донарахування, Гкал
        # app 1
        app = Appart_values(self.df, 1)
        test = app.gen_no_counter_e(q_no_surge)
        self.assertEqual(float("{:.3f}".format(test)), 2.666)
        # app 37
        app = Appart_values(self.df, 104)
        test = app.gen_no_counter_e(q_no_surge)
        self.assertEqual(float("{:.3f}".format(test)), 0)
        # app 87
        app = Appart_values(self.df, 87)
        test = app.gen_no_counter_e(q_no_surge)
        self.assertEqual(float("{:.3f}".format(test)), 2.536)

    def test_gen_total_fun_sys(self):
        arg = 0.001376046
        # функціонування системи
        # row 2
        app = Appart_values(self.df, 1)
        test = app.gen_total_fun_sys(arg)
        self.assertEqual(float("{:.3f}".format(test)), 0.082)
        # row 8
        app = Appart_values(self.df, 7)
        test = app.gen_total_fun_sys(arg)
        self.assertEqual(float("{:.3f}".format(test)), 0.071)

    def test_gen_total_Mkz(self):
        arg = 0.002752091
        # МЗК
        # row 2
        app = Appart_values(self.df, 1)
        test = app.gen_total_Mkz(arg)
        self.assertEqual(float("{:.3f}".format(test)), 0.163)
        # row 8
        app = Appart_values(self.df, 7)
        test = app.gen_total_Mkz(arg)
        self.assertEqual(float("{:.3f}".format(test)), 0.143)

    def test_gen_total_e(self):
        # ВСЬОГО, Гкал
        # row 2
        app = Appart_values(self.df, 1)
        arg = 0.002752091
        test = app.gen_total_Mkz(arg)
        arg = 0.001376046
        test = app.gen_total_fun_sys(arg)
        q_no_surge = 0.044960013
        test = app.gen_no_counter_e(q_no_surge)
        test = app.gen_total_e()
        self.assertEqual(float("{:.3f}".format(test)), 2.911)
        # row 8
        app = Appart_values(self.df, 7)
        arg = 0.002752091
        app.gen_total_Mkz(arg)
        arg = 0.001376046
        app.gen_total_fun_sys(arg)
        q_pit_roz = 0.0030
        q_op_min = 0.011696389
        e_for_redistibut = 0.003998048
        sum_e_used_k = 4823.121
        app.gen_surcharge(q_pit_roz, q_op_min, sum_e_used_k)
        app.gen_specified_used_E(e_for_redistibut)
        app.gen_specified_priv2S()
        app.gen_specified_surcharge(q_op_min)
        app.get_S_if_surcharge()
        # print(app.total_fun_sys)
        # print(app.total_s_q_Mkz)
        # print(app.specified_used_E)
        app.specified_used_E = 0.585
        test = app.gen_total_e()
        self.assertEqual(float("{:.3f}".format(test)), 0.799)
        # row 26
        app = Appart_values(self.df, 25)
        arg = 0.002752091
        app.gen_total_Mkz(arg)
        arg = 0.001376046
        app.gen_total_fun_sys(arg)
        q_pit_roz = 0.0030
        q_op_min = 0.011696389
        e_for_redistibut = 0.003998048
        sum_e_used_k = 4823.121
        app.gen_surcharge(q_pit_roz, q_op_min, sum_e_used_k)
        app.gen_specified_used_E(e_for_redistibut)
        app.gen_specified_priv2S()
        app.gen_specified_surcharge(q_op_min)
        app.get_S_if_surcharge()
        # print(app.total_fun_sys)
        # print(app.total_s_q_Mkz)
        # print(app.specified_used_E)
        app.specified_used_E = 0.573
        test = app.gen_total_e()
        self.assertEqual(float("{:.3f}".format(test)), 0.783)

if __name__ == "__main__":
    unittest.main()
