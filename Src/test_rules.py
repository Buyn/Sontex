# ----------------------------------------------
# * import block :
import unittest

from rules import *
# ----------------------------------------------
# * functions : 
# ----------------------------------------------
# * def load_exel : 
def load_exel(filename, sheet_name): 
    df = pd.read_excel(filename,
                      sheet_name = sheet_name,
                      engine='openpyxl',
                      # index_col=0,
                      header=None,
                      )
    return df


# ----------------------------------------------
# * class setUp_Test : 
# ** ------------------------------------------:
class setUp_Test(unittest.TestCase):
# ** @classmethod setUpClass: 
    @classmethod #setUpClass#
    def setUpClass(self):
        gv_filename = "Data_files/test.xlsx"
        sheet_name = "rules"
        self._df_rules = load_exel(gv_filename, sheet_name)
        sheet_name = "квартири, площі"
        self._df_report = load_exel(gv_filename, sheet_name)


# ** @classmethod setUp: 
    # @classmethod #setUp#
    @classmethod #setUp#
    def setUp(self):
        self.df_rules = self._df_rules.copy()
        self.df_report = self._df_report.copy()


# ** @classmethod tearDown: 
    # @classmethod #tearDown#
    @classmethod #tearDown#
    def tearDown(self):
        self.df_rules = None
        self.df_report = None


# ** def test_init1 : 
    def test_init(self):# {{{
        self.assertIsNotNone( self.df_report )
        self.assertEqual(self.df_report.iloc[107, 0], "end")
        self.assertIsNotNone( self.df_rules )
        self.assertEqual(self.df_rules.iloc[1, 0], "rule")


# ** def test_populate_apps : 
    def test_postproc_test(self): 
        test = postproc_test (self.df_report, ["test", 2 ,3])


# ** def test_get_all_rules_index : 
    def test_get_all_rules_index(self): 
        test = get_all_rules_index(self.df_rules)
        self.assertIsNotNone(test)
        self.assertEqual(len(test), 3)
        self.assertEqual(test[0][0], 1)
        self.assertEqual(test[0][1], "post_divider")


# ** def test_use_rule : 
    def test_use_rule(self): 
        test = use_rule(self.df_report, 0, "test", ("test",2,3), test=True)
        self.assertEqual(test, ("test",2,3))
        test = use_rule(self.df_report, 0, "test_no", ("test",2,3), test=True)
        self.assertIsNone(test)
        # with self.assertRaises(NameError):
        #     test = get_last_app_line(t1[:-1])
        #     self.assertEqual(test , 103)


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
