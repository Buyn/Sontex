import unittest

from counter_values import *

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

    def test_init1(self):
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

    def test_get_adress(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(test.get_adress(), 25482311)
        test = Counter_values(self.df, 8)
        self.assertEqual(test.get_adress(), 25482312)
        test = Counter_values(self.df, 106)
        self.assertEqual(test.get_adress(), 25482672)

    def test_get_value1(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(test.get_value1(), 653)
        test = Counter_values(self.df, 8)
        self.assertEqual(test.get_value1(), 552)
        test = Counter_values(self.df, 106)
        self.assertEqual(test.get_value1(), 878)
        test = Counter_values(self.df, 69)
        self.assertEqual(test.get_value1(), 310)
        test = Counter_values(self.df, 70)
        self.assertEqual(test.get_value1(), 734)
        test = Counter_values(self.df, 71)
        self.assertEqual(test.get_value1(), 527)
        with self.assertRaises(NameError):
            # test = Counter_values(self.df, 100)
            # self.assertEqual(test.get_value2(), 0)
            test = Counter_values(self.df, 104)
            test.get_value1()

    def test_set_value1(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(test.get_value1(), 653)
        test.set_value1(100)
        self.assertEqual(test.get_value1(), 100)
        test.set_value1(653)
        test = Counter_values(self.df, 8)
        self.assertEqual(test.get_value1(), 552)
        test.set_value1(0)
        self.assertEqual(test.get_value1(), 0)
        test.set_value1(552)
        test = Counter_values(self.df, 106)
        test.set_value1(0.01)
        self.assertEqual(test.get_value1(), 0.01)
        test.set_value1(106)

    def test_set_value2(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(test.get_value2(), 603)
        test.set_value2(100)
        self.assertEqual(test.get_value2(), 100)
        test.set_value2(653)
        test = Counter_values(self.df, 8)
        self.assertEqual(test.get_value2(), 552)
        test.set_value2(0)
        self.assertEqual(test.get_value2(), 0)
        test.set_value2(552)
        test = Counter_values(self.df, 106)
        test.set_value2(0.01)
        self.assertEqual(test.get_value2(), 0.01)
        test.set_value2(106)

    def test_get_value2(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(test.get_value2(), 603)
        test = Counter_values(self.df, 8)
        self.assertEqual(test.get_value2(), 552)
        test = Counter_values(self.df, 106)
        self.assertEqual(test.get_value2(), 831)
        test = Counter_values(self.df, 69)
        self.assertEqual(test.get_value2(), 310)
        test = Counter_values(self.df, 70)
        self.assertEqual(test.get_value2(), 717)
        test = Counter_values(self.df, 71)
        self.assertEqual(test.get_value2(), 505)
        with self.assertRaises(NameError):
            test = Counter_values(self.df, 104)
            test.get_value2()

    def test_gen_delta(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(test.gen_delta(), 50)
        test = Counter_values(self.df, 84)
        self.assertEqual(test.gen_delta(), 24)
        test = Counter_values(self.df, 85)
        self.assertEqual(test.gen_delta(), 4)
        test = Counter_values(self.df, 86)
        self.assertEqual(test.gen_delta(), 16)
        with self.assertRaises(AttributeError):
            test = Counter_values(self.df, 104)
            test.gen_delta()

    def test_gen_delta_k(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(float("{:.2f}".format(test.gen_delta_k())), 95.90)
        test = Counter_values(self.df, 84)
        self.assertEqual(float("{:.2f}".format(test.gen_delta_k())), 44.86)
        test = Counter_values(self.df, 85)
        self.assertEqual(float("{:.2f}".format(test.gen_delta_k())), 8.22)
        test = Counter_values(self.df, 86)
        self.assertEqual(float("{:.2f}".format(test.gen_delta_k())), 13.64)
        with self.assertRaises(AttributeError):
            test = Counter_values(self.df, 104)
            test.gen_delta()

    def test_get_k_priv(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(test.get_k_priv(), 1.91808)
        test = Counter_values(self.df, 8)
        self.assertEqual(test.get_k_priv(), 2.34432)
        test = Counter_values(self.df, 106)
        self.assertEqual(test.get_k_priv(), 0.93465)
        with self.assertRaises(NameError):
            test = Counter_values(self.df, 104)
            test.get_k_priv()

    def test_get_value(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(
            test.get_value(
                gv.gl_counters_k_priv_column,
                "gl_counters_k_priv_column"),
            1.91808)
        self.assertEqual(
            test.get_value(
                gv.gl_counters_value1_column,
                "gl_counters_value1_column"),
            653)
        test = Counter_values(self.df, 8)
        self.assertEqual(
            test.get_value(
                gv.gl_counters_k_priv_column,
                "gl_counters_k_priv_column"),
            2.34432)
        with self.assertRaises(NameError):
            test = Counter_values(self.df, 104)
            test.get_value(
                gv.gl_counters_k_priv_column,
                "gl_counters_k_priv_column"),

    def test_set_value(self): 
        test = Counter_values(self.df, 7)
        self.assertEqual(
            test.get_value(
                gv.gl_counters_k_priv_column,
                "gl_counters_k_priv_column"),
            1.91808)
        self.assertEqual(
            test.get_value(
                gv.gl_counters_value1_column,
                "gl_counters_value1_column"),
            653)
        r = test.set_value(
                gv.gl_counters_k_priv_column,
                "gl_counters_k_priv_column", 1.9180800000000009)
        # print(r)
        self.assertEqual(
            test.get_value(
                gv.gl_counters_k_priv_column,
                "gl_counters_k_priv_column"),
                    1.9180800000000009)
        r = test.set_value(
                gv.gl_counters_k_priv_column,
                "gl_counters_k_priv_column", 1.9180800000000002)
        r = test.set_value(
                gv.gl_counters_value1_column,
                "gl_counters_value1_column",
                153)
        self.assertEqual(
            test.get_value(
                gv.gl_counters_value1_column,
                "gl_counters_value1_column"),
            153)
        r = test.set_value(
                gv.gl_counters_value1_column,
                "gl_counters_value1_column",
                653)

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

if __name__ == "__main__":
    unittest.main()
