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
        filename = "Data_files/test.xlsx"
        # sheet_name = "показники"
        sheet_name = "квартири, площі"
        # self.df = load_exel(filename, sheet_name)
        import pandas as pd
        self.df = pd.read_excel(filename,
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
        r1,r2 = test.get_next_appindex(101)
        self.assertEqual(r1, 103)
        self.assertTrue(r2)
        r1,r2 = test.get_next_appindex(103)
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
        self.assertEqual([x.adress for x in test.get_counters_list(96,100)]
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
        test = Appart_values(self.df, 96)
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
