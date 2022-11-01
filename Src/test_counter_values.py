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
        test = Counter_values(self.df, 7) 
        self.assertEqual(test._line, 7)
        # self.assertEqual(test._df, self.df)
        self.assertIsNotNone( test._df)
        test = Counter_values(self.df, 7)
        self.assertEqual(test.get_value1(), 217)
        self.assertEqual(test.get_value2(), 146)
        self.assertEqual(test.get_adress(), 25482311)
        test = Counter_values(self.df, 8)
        self.assertEqual(test.get_value1(), 182)
        self.assertEqual(test.get_value2(), 120)
        self.assertEqual(test.get_adress(), 25482312)
        test = Counter_values(self.df, 102)
        self.assertEqual(test.get_value2(), 18)
        self.assertEqual(test.get_value1(), 63)
        self.assertEqual(test.get_adress(), 25482672)


# ** def test_get_adress : 
    def test_get_adress(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(test.get_adress(), 25482311)
        test = Counter_values(self.df, 8)
        self.assertEqual(test.get_adress(), 25482312)
        test = Counter_values(self.df, 102)
        self.assertEqual(test.get_adress(), 25482672)


# ** def test_get_value1 : 
    def test_get_value1(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(test.get_value1(), 217)
        test = Counter_values(self.df, 8)
        self.assertEqual(test.get_value1(), 182)
        test = Counter_values(self.df, 102)
        self.assertEqual(test.get_value1(), 63)
        test = Counter_values(self.df, 100)
        self.assertEqual(test.get_value1(), 0)


# ** def test_get_value2 : 
    def test_get_value2(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(test.get_value2(), 146)
        test = Counter_values(self.df, 8)
        self.assertEqual(test.get_value2(), 120)
        test = Counter_values(self.df, 102)
        self.assertEqual(test.get_value2(), 18)
        test = Counter_values(self.df, 100)
        self.assertEqual(test.get_value2(), 0)


# ** def test_is_valid : 
    def test_is_valid(self): 
        test = Counter_values(self.df, 7)
        self.assertTrue(test.is_valid())
        test = Counter_values(self.df, 8)
        self.assertTrue(test.is_valid())
        test = Counter_values(self.df, 102)
        self.assertTrue(test.is_valid())
        test = Counter_values(self.df, 1)
        self.assertFalse(test.is_valid())
        test = Counter_values(self.df, 6)
        self.assertFalse(test.is_valid())
        test = Counter_values(self.df, 100)
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
