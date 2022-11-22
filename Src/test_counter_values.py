# ----------------------------------------------
# * import block :
import unittest

from counter_values import *


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
        test = Counter_values(self.df, 7) 
        self.assertEqual(test._line, 7)
        # self.assertEqual(test._df, self.df)
        self.assertIsNotNone( test._df)
        test = Counter_values(self.df, 7)
        self.assertEqual(test.get_value1(), 653)
        self.assertEqual(test.get_value2(), 603)
        self.assertEqual(test.get_adress(), 25482311)
        test = Counter_values(self.df, 8)
        self.assertEqual(test.get_value1(), 552)
        self.assertEqual(test.get_value2(), 552)
        self.assertEqual(test.get_adress(), 25482312)
        test = Counter_values(self.df, 106)
        self.assertEqual(test.get_value1(), 878)
        self.assertEqual(test.get_value2(), 831)
        self.assertEqual(test.get_adress(), 25482672)


# ** def test_get_adress : 
    def test_get_adress(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(test.get_adress(), 25482311)
        test = Counter_values(self.df, 8)
        self.assertEqual(test.get_adress(), 25482312)
        test = Counter_values(self.df, 106)
        self.assertEqual(test.get_adress(), 25482672)


# ** def test_get_value1 : 
    def test_get_value1(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(test.get_value1(), 653)
        test = Counter_values(self.df, 8)
        self.assertEqual(test.get_value1(), 552)
        test = Counter_values(self.df, 106)
        self.assertEqual(test.get_value1(), 878)
        with self.assertRaises(NameError):
            # test = Counter_values(self.df, 100)
            # self.assertEqual(test.get_value2(), 0)
            test = Counter_values(self.df, 104)
            test.get_value1()
        # test = Counter_values(self.df, 100)
        # self.assertEqual(test.get_value1(), 0)


# ** def test_get_value2 : 
    def test_get_value2(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(test.get_value2(), 603)
        test = Counter_values(self.df, 8)
        self.assertEqual(test.get_value2(), 552)
        test = Counter_values(self.df, 106)
        self.assertEqual(test.get_value2(), 831)
        with self.assertRaises(NameError):
            # test = Counter_values(self.df, 100)
            # self.assertEqual(test.get_value2(), 0)
            test = Counter_values(self.df, 104)
            test.get_value2()
            # print(test.heating_area)
            # print(test.sum_area)
            # print("tupe is =", type(test.sum_area))
            # print("tupe is =",type(test.heating_area))


# ** def test_gen_delta : 
    def test_gen_delta(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(test.gen_delta(), 50)
        with self.assertRaises(AttributeError):
            # test = Counter_values(self.df, 100)
            # self.assertEqual(test.get_value2(), 0)
            test = Counter_values(self.df, 104)
            test.gen_delta()
            # print(test.heating_area)
            # print(test.sum_area)
            # print("tupe is =", type(test.sum_area))
            # print("tupe is =",type(test.heating_area))


# ** def test_gen_delta_k : 
    def test_gen_delta_k(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(float("{:.2f}".format(test.gen_delta_k())), 95.90)
        with self.assertRaises(AttributeError):
            test = Counter_values(self.df, 104)
            test.gen_delta()


# ** def test_get_k_priv : 
    def test_get_k_priv(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(test.get_k_priv(), 1.9180800000000002)
        test = Counter_values(self.df, 8)
        self.assertEqual(test.get_k_priv(), 2.3443200000000006)
        test = Counter_values(self.df, 106)
        self.assertEqual(test.get_k_priv(), 0.9346500000000002)
        with self.assertRaises(NameError):
            # test = Counter_values(self.df, 100)
            # self.assertEqual(test.get_value2(), 0)
            test = Counter_values(self.df, 104)
            test.get_k_priv()
            # print(test.heating_area)
            # print(test.sum_area)
            # print("tupe is =", type(test.sum_area))
            # print("tupe is =",type(test.heating_area))


# ** def test_get_value : 
    def test_get_value(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(
            test.get_value(
                gl_counters_k_priv_column,
                "gl_counters_k_priv_column"),
            1.9180800000000002)
        self.assertEqual(
            test.get_value(
                gl_counters_value1_column,
                "gl_counters_value1_column"),
            653)
        test = Counter_values(self.df, 8)
        self.assertEqual(
            test.get_value(
                gl_counters_k_priv_column,
                "gl_counters_k_priv_column"),
            2.3443200000000006)
        with self.assertRaises(NameError):
            test = Counter_values(self.df, 104)
            test.get_value(
                gl_counters_k_priv_column,
                "gl_counters_k_priv_column"),
            # print(test.heating_area)
            # print(test.sum_area)
            # print("tupe is =", type(test.sum_area))
            # print("tupe is =",type(test.heating_area))
        # self.assertEqual(test.get_value(), 120)
        # test = Counter_values(self.df, 102)
        # self.assertEqual(test.get_value(), 18)
        # test = Counter_values(self.df, 100)
        # self.assertEqual(test.get_value(), 0)


# ** def test_is_valid : 
    def test_is_valid(self): 
        test = Counter_values(self.df, 7)
        self.assertTrue(test.is_valid())
        test = Counter_values(self.df, 8)
        self.assertTrue(test.is_valid())
        test = Counter_values(self.df, 106)
        self.assertTrue(test.is_valid())
        test = Counter_values(self.df, 1)
        self.assertFalse(test.is_valid())
        test = Counter_values(self.df, 6)
        self.assertFalse(test.is_valid())
        test = Counter_values(self.df, 104)
        self.assertFalse(test.is_valid())


# ** ------------------------------------------:
# * Test runer : 
# ** ------------------------------------------:
# (compile " D:/Development/version-control/GitHub/Vadim/Tochil/main_test.py -k init")
# (compile " python -m unittest D:/Development/version-control/GitHub/Vadim/Tochil/main_test.py ")
# (compile "python -m unittest") run all est in dir
# ** if __main__: 
if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(suite_Init())
    unittest.main()


# ----------------------------------------------
# * -------------------------------------------:
