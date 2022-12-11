# ----------------------------------------------
# * import block :
import unittest
from appart_values import *


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
        # self.df = load_exel(gv_filename, sheet_name)
        import pandas as pd
        self.df = pd.read_excel(gv_filename,
                          sheet_name = sheet_name,
                          engine='openpyxl',
                          # index_col=0,
                          header=None,
                          )
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


# ** def test_get_next_appindex : 
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


# ** def test_is_starting_line : 
    def test_is_starting_line(self): 
        test = Appart_values(self.df, 2)
        # print(self.df.iloc[2, 0])
        self.assertTrue(test.is_starting_line(2))
        # print(self.df.iloc[14, 0])
        self.assertFalse(test.is_starting_line(14))


# ** def test_get_counters : 
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


# ** def test_gen_counters_adress : 
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


# ** def test_load_values : 
    def test_load_values(self): 
        test = Appart_values(self.df, 7)
        test.load_values()
        self.assertEqual(test.heating_area, 51.9)
        self.assertEqual(test.sum_area, 55.7)
        test = Appart_values(self.df, 6)
        test.load_values()
        self.assertEqual(test.heating_area, 52)
        self.assertEqual(test.sum_area, 56.70)
        test = Appart_values(self.df, 84)
        test.load_values()
        self.assertEqual(test.heating_area, 52.10)
        self.assertEqual(test.sum_area, 56.60)
        with self.assertRaises(NameError):
            test = Appart_values(self.df, 131)
            test.load_values()
            print(test.heating_area)
            print(test.sum_area)
            print("tupe is =", type(test.sum_area))
            print("tupe is =",type(test.heating_area))
        with self.assertRaises(NameError):
            test = Appart_values(self.df, 132)
            test.load_values()
            print(test.heating_area)
            print(test.sum_area)
            print("tupe is =", type(test.sum_area))
            print("tupe is =",type(test.heating_area))
        with self.assertRaises(NameError):
            test = Appart_values(self.df, 133)
            test.load_values()
            print(test.heating_area)
            print(test.sum_area)
            print("tupe is =", type(test.sum_area))
            print("tupe is =",type(test.heating_area))


# ** test_gen_E_used : 
    def test_gen_E_used(self):
        # сумарне споживання по квартирі, од.
        test = Appart_values(self.df, 7)
        self.assertEqual(test.gen_E_used(), 112)
        test = Appart_values(self.df, 84)
        self.assertEqual(test.gen_E_used(), 44)
        test = Appart_values(self.df, 69)
        self.assertEqual(test.gen_E_used(), 39)


# ** test_gen_E_used_k : 
    def test_gen_E_used_k(self):
        # сумарне споживання по квартирі, од.
        test = Appart_values(self.df, 7)
        self.assertEqual(float("{:.2f}".format(test.gen_E_used_k())), 201.61)
        test = Appart_values(self.df, 69)
        self.assertEqual(float("{:.2f}".format(test.gen_E_used_k())), 37.76)
        test = Appart_values(self.df, 84)
        self.assertEqual(float("{:.2f}".format(test.gen_E_used_k())), 66.73)


# ** test_gen_k_to_s : 
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


# ** test_gen_use_for_period : 
    def test_gen_use_for_period(self):
        # обсяг споживання за період, Гкал
        app = Appart_values(self.df, 7)
        q_pit_roz = 0.00299979010123
        test = app.gen_use_for_period(q_pit_roz)
        # self.assertEqual(float("{:.3f}".format(test)), 0.605)
        self.assertEqual(float("{:.9f}".format(test)), 0.6047922420)
        app = Appart_values(self.df, 69)
        test = app.gen_use_for_period(q_pit_roz)
        # self.assertEqual(float("{:.3f}".format(test)), 0.113)
        self.assertEqual(float("{:.10f}".format(test)), 0.1132716543)
        app = Appart_values(self.df, 84)
        test = app.gen_use_for_period(q_pit_roz)
        self.assertEqual(float("{:.9f}".format(test)), 0.200169394)


# ** test_gen_priv2S : 
    def test_gen_priv2S(self):
        # приведене до м2 площі, Гкал/м2
        app = Appart_values(self.df, 7)
        # q_pit_roz = 0.0030
        q_pit_roz = 0.00299979010123
        test = app.gen_priv2S(q_pit_roz)
        self.assertEqual(float("{:.9f}".format(test)), 0.01165303)
        app = Appart_values(self.df, 69)
        # print("gen_use_for_period(q_pit_roz)", app.gen_E_used_k())
        # print("heating_area ", app.heating_area)
        test = app.gen_priv2S(q_pit_roz)
        # self.assertEqual(float("{:.9f}".format(test)), 0.002165806)
        self.assertEqual(float("{:.9f}".format(test)), 0.002182498)
        app = Appart_values(self.df, 84)
        test = app.gen_priv2S(q_pit_roz)
        # print("gen_E_used_k()", app.gen_E_used_k())
        # print("gen_use_for_period(q_pit_roz)", app.gen_use_for_period(q_pit_roz))
        self.assertEqual(float("{:.9f}".format(test)), 0.003842023)


# ** test_gen_surcharge : 
    def test_gen_surcharge(self):
        # донарахування, Гкал
        app = Appart_values(self.df, 7)
        q_pit_roz = 0.0030
        q_op_min = 0.011696389
        self.assertIsNone(app.surcharge)
        test = app.gen_surcharge(q_pit_roz, q_op_min)
        self.assertEqual(float("{:.3f}".format(test)), 0.002)
        app = Appart_values(self.df, 69)
        self.assertIsNone(app.surcharge)
        test = app.gen_surcharge(q_pit_roz, q_op_min)
        self.assertEqual(float("{:.3f}".format(test)), 0.494)
        app = Appart_values(self.df, 84)
        self.assertIsNone(app.surcharge)
        test = app.gen_surcharge(q_pit_roz, q_op_min)
        self.assertEqual(float("{:.3f}".format(test)), 0.409)


# ** test_get_S_if_surcharge : 
    def test_get_S_if_surcharge(self):
        # донарахування, Гкал
        app = Appart_values(self.df, 7)
        q_pit_roz = 0.0030
        q_op_min = 0.011696389
        test = app.gen_surcharge(q_pit_roz, q_op_min)
        test = app.get_S_if_surcharge()
        self.assertEqual(float("{:.3f}".format(test)), 0)
        app = Appart_values(self.df, 11)
        q_pit_roz = 0.0030
        q_op_min = 0.011696389
        test = app.gen_surcharge(q_pit_roz, q_op_min)
        test = app.get_S_if_surcharge()
        self.assertEqual(float("{:.3f}".format(test)), 68.03)


# ** test_gen_specified_used_E : 
    def test_gen_specified_used_E(self):
        # донарахування, Гкал
        # app 7
        app = Appart_values(self.df, 7)
        q_pit_roz = 0.0030
        q_op_min = 0.011696389
        e_for_redistibut = 0.003998048
        test = app.gen_surcharge(q_pit_roz, q_op_min)
        self.assertEqual(float("{:.3f}".format(test)), 0.002)
        test = app.gen_specified_used_E(e_for_redistibut)
        # print(app.gen_specified_priv2S())
        # print(app.get_S_if_surcharge())
        self.assertEqual(float("{:.3f}".format(test)), 0.607)
        # print(app.specified_used_E)
        # print(app.heating_area)
        test = app.gen_specified_priv2S()
        self.assertEqual(float("{:.9f}".format(test)), 0.011696389)
        test = app.gen_specified_surcharge(q_op_min)
        # print(e_for_redistibut)
        # print(app.specified_used_E)
        self.assertEqual(float("{:.9f}".format(test)), 0)
        # second Total for app in row 7
        e_for_redistibut = 4.337E-04
        # print(app.surcharge) 
        test = app.gen_specified_used_E(e_for_redistibut)
        # print(app.surcharge) 
        self.assertEqual(float("{:.3f}".format(test)), 0.585)
        # print(e_for_redistibut)
        test = app.gen_specified_priv2S()
        self.assertEqual(float("{:.7f}".format(test)), 0.0112627)
        test = app.gen_specified_surcharge(q_op_min)
        # print(app.gen_specified_priv2S())
        # print(q_op_min)
        self.assertEqual(float("{:.3f}".format(test)), 0.023)
        # app 11
        e_for_redistibut = 0.003998048
        app = Appart_values(self.df, 11)
        test = app.gen_surcharge(q_pit_roz, q_op_min)
        test = app.gen_specified_used_E(e_for_redistibut)
        # self.assertEqual(float("{:.3f}".format(test)), 0.602)
        self.assertEqual(float("{:.4f}".format(test)), 0.6017)
        # print(app.heating_area)
        test = app.gen_specified_priv2S()
        self.assertEqual(float("{:.5f}".format(test)), 0.00884)
        test = app.gen_specified_surcharge(q_op_min)
        self.assertEqual(float("{:.3f}".format(test)), 0.194)
        test = app.get_S_if_surcharge()
        self.assertEqual(float("{:.3f}".format(test)), 0)
        # test = app.gen_specified_used_E(e_for_redistibut, q_pit_roz)
        # second Total for app in row 11
        e_for_redistibut = 4.337E-04
        # print(app.surcharge) 
        test = app.gen_specified_used_E(e_for_redistibut)
        # print(app.surcharge) 
        self.assertEqual(float("{:.3f}".format(test)), 0.796)
        # print(e_for_redistibut)
        test = app.gen_specified_surcharge(q_op_min)
        self.assertEqual(float("{:.3f}".format(test)), 0)



# ** test_gen_no_counter_e : 
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



# ** test_gen_total_fun_sys : 
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


# ** test_gen_total_Mkz : 
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


# ** test_gen_total_e : 
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
        app.gen_surcharge(q_pit_roz, q_op_min)
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
        app.gen_surcharge(q_pit_roz, q_op_min)
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
