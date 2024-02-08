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
        # sheet_name = "report"
        sheet_name = "Теплоенрго"
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
        self.assertEqual(self.df_report.iloc[1, 0], 1)
        self.assertIsNotNone( self.df_rules )
        self.assertEqual(self.df_rules.iloc[1, 0], "rule")
        with self.assertRaises(ValueError):
            test = load_exel(gv_filename, "error rules")
            self.assertIsNone(test)


# ** def test_postproc_test : 
    def test_postproc_test(self): 
        test_df, test = postproc_test (self.df_report, ["test", 2 ,3])


# ** def test_postproc_divider : 
    def test_postproc_divider(self): 
        self.assertIsNotNone( self.df_report )
        # print(self.df_report)
        # print(self.df_report.iloc[2, 3])
        self.assertEqual(self.df_report.shape[0], 41)
        # arg = [2, '"2b" "êâ.2b"', '0.50']
        arg =  [2, 5, '"2b" "ea.2b"', '0.50']
        self.assertEqual(self.df_report.iloc[2, 4], 2.04)
        test_df, test = postproc_divider(self.df_report, arg)
        self.assertEqual(test_df.shape[0], 42)
        self.assertEqual(test_df.iloc[2, 4], 1.02)
        # print(self.df_report.iloc[2, 1])
        # print(self.df_report.iloc[3, 1])
        self.assertEqual(test_df.iloc[3, 0], "2b")
        self.assertEqual(test_df.iloc[3, 4], 1.02)


# ** def test_rule_postproc_divider : 
    def test_rule_postproc_divider(self): 
        self.assertIsNotNone( self.df_report )
        self.assertEqual(self.df_report.shape[0], 41)
        rules_list = get_all_rules(self.df_rules)

        rule = rules_list[0]
        # print(rule)
        # 
        self.assertEqual(self.df_report.iloc[2, 4], 2.04)
        test_df, test = use_rule(df = self.df_report,
                                 index = rule[0],
                                 rule_name = rule[1],
                                 rule_params = rule[2],)
        # test_df, test = postproc_divider (self.df_report, ["test", 2 ,3])
        self.assertEqual(self.df_report.shape[0], 42)
        self.assertEqual(test_df.iloc[2, 4], 1.02)
        self.assertEqual(test_df.iloc[3, 0], "2b")
        self.assertEqual(test_df.iloc[3, 4], 1.02)
        # print (test_df)


# ** def test_get_all_rules : 
    def test_get_all_rules(self): 
        test = get_all_rules(self.df_rules)
        # print(test)
        self.assertIsNotNone(test)
        self.assertEqual(len(test), 3)
        self.assertEqual(test[0][0], 1)
        self.assertEqual(test[0][1], "post_divider")


# ** def test_use_rule : 
    def test_use_rule(self): 
        # test = use_rule(self.df_report, 0, "test", ("test",2,3), test=True)
        test_df, test = use_rule(df= self.df_report,
                                 index=0,
                                 rule_name= "test",
                                 rule_params= ("test",2,3),
                                 test=True)
        self.assertIsNotNone(test_df)
        self.assertEqual(test, ("test",2,3))
        test_df, test = use_rule(self.df_report, 0, "test_no", ("test",2,3), test=True)
        self.assertIsNotNone(test_df)
        self.assertIsNone(test)
        # with self.assertRaises(NameError):
        #     test = get_last_app_line(t1[:-1])
        #     self.assertEqual(test , 103)


# ** def test_postprocessing_df_with_rules_df : 
    def test_postprocessing_df_with_rules_df(self): 
        # test = use_rule(self.df_report, 0, "test", ("test",2,3), test=True)
        self.assertEqual(self.df_report.iloc[2, 4], 2.04)
        test_df = postprocessing_df_with_rules_df(self.df_report, self.df_rules)
        # test_df, test = use_rule(df= self.df_report,
        #                          index=0,
        #                          rule_name= "test",
        #                          rule_params= ("test",2,3),
        #                          test=True)
        self.assertIsNotNone(test_df)
        self.assertEqual(test_df.shape[0], 42)
        self.assertEqual(test_df.iloc[2, 4], 1.02)
        self.assertEqual(test_df.iloc[3, 0], "2b")
        self.assertEqual(test_df.iloc[3, 4], 1.02)
        # self.assertEqual(test, ("test",2,3))
        # test_df, test = use_rule(self.df_report, 0, "test_no", ("test",2,3), test=True)
        # self.assertIsNotNone(test_df)
        # self.assertIsNone(test)
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
