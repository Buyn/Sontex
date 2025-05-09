# ----------------------------------------------
import unittest

from rules import *

# * def load_exel:
def load_exel(filename, sheet_name): 
    df = pd.read_excel(filename,
                      sheet_name = sheet_name,
                      engine='openpyxl',
                      # index_col=0,
                      header=None,
                      )
    return df

class setUp_Test(unittest.TestCase):
# ** @classmethod setUpClass: 
    @classmethod #setUpClass#
    def setUpClass(self):
        gv_filename = "Data_files/test.xlsx"
        # sheet_name = "rules"
        sheet_name = gv.gr_rule_sheet_name
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
    def test_init(self):
        self.assertIsNotNone( self.df_report )
        self.assertEqual(self.df_report.iloc[1, 0], 1)
        self.assertIsNotNone( self.df_rules )
        self.assertEqual(self.df_rules.iloc[1, 0], "rule")
        with self.assertRaises(ValueError):
            test = load_exel(gv.gv_filename, "error rules")
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


# ** def test_postproc_divider_fix : 
    def test_postproc_divider_fix(self): 
        self.assertIsNotNone( self.df_report )
        # print(self.df_report)
        # print(self.df_report.iloc[2, 3])
        self.assertEqual(self.df_report.shape[0], 41)
        # arg = [2, '"2b" "êâ.2b"', '0.50']
        # arg =  [2, 5, '"2b" "ea.2b"', '0.50']
        # rule  post_divider  4 3300145734  5 "3300145735" "3300145734 вулиця Скрипника, 7 кв.2b" 0.50
        # print(arg[0])
        # print(df[df[0]==arg[0]])
        # target_index = int(df[df[0]==arg[0]].index.values)
        # self.assertEqual(self.df_report.iloc[73, 0], 3300145734)
        df = self.df_report
        # print(df[df[0]==3300145734])
        #  Reset the index
        # df.loc[27 + 0.5] = ["3300145735", "3300145734 вулиця Скрипника, 7 кв.2b", " ", " ", '0.50']
        # df.loc[27 + 0.5] = [3300145735, "3300145734 вулиця Скрипника, 7 кв.2b", " ", " ", '0.50']
        # df = df.sort_index().reset_index(drop=True)
        # print(df)
        arg =  [3300145734, 5, '"3300145735" "3300145735 вулиця Скрипника, 7 кв.2b"', '0.50']
        self.assertEqual(self.df_report.iloc[28, 4], 1.8)
        test_df, test = postproc_divider(self.df_report, arg)
        test_df = test_df.sort_index().reset_index(drop=True)
        # print(test_df)
        self.assertEqual(test_df.shape[0], 42)
        self.assertEqual(test_df.iloc[28, 4], 0.9)
        # print(self.df_report.iloc[2, 1])
        # print(self.df_report.iloc[3, 1])
        # print(test_df.iloc[29, 0])
        # print(test_df.iloc[29, 1])
        self.assertEqual(test_df.iloc[29, 0], "3300145735")
        self.assertEqual(test_df.iloc[29, 4], 0.9)


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
        # self.assertEqual(test_df.iloc[29, 0], "3300145735")
        # self.assertEqual(test_df.iloc[29, 0], 3300145735)
        # self.assertEqual(test_df.iloc[30, 0], 3300145735)
        # self.assertEqual(test_df.iloc[29, 4], 0.9)
        # print (test_df)


# ** def test_get_all_rules : 
    def test_get_all_rules(self): 
        test = get_all_rules(self.df_rules)
        # print(test)
        self.assertIsNotNone(test)
        self.assertEqual(len(test), 4)
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


# ** def test_postprocessing_df_with_rules_df:
    def test_postprocessing_df_with_rules_df(self): 
        # test = use_rule(self.df_report, 0, "test", ("test",2,3), test=True)
        self.assertEqual(self.df_report.iloc[2, 4], 2.04)
        self.assertEqual(self.df_report.shape[0], 41)
        test_df = postprocessing_df_with_rules_df(self.df_report, self.df_rules)
        # test_df, test = use_rule(df= self.df_report,
        #                          index=0,
        #                          rule_name= "test",
        #                          rule_params= ("test",2,3),
        #                          test=True)
        self.assertIsNotNone(test_df)
        # print(test_df.shape)
        self.assertEqual(test_df.shape[0], 43)
        self.assertEqual(test_df.iloc[2, 4], 1.02)
        self.assertEqual(test_df.iloc[3, 0], "2b")
        self.assertEqual(test_df.iloc[3, 4], 1.02)
        # self.assertEqual(test, ("test",2,3))
        # test_df, test = use_rule(self.df_report, 0, "test_no", ("test",2,3), test=True)
        self.assertEqual(test_df.iloc[29, 0], 3300145734)
        self.assertEqual(test_df.iloc[29, 4], 0.9)
        self.assertEqual(test_df.iloc[30, 0], "3300145735")
        self.assertEqual(test_df.iloc[30, 1], "3300145734 вулиця Скрипника, 7 кв.2b")
        self.assertEqual(test_df.iloc[30, 2], "3300145735")
        # self.assertIsNotNone(test_df)
        # self.assertIsNone(test)
        # with self.assertRaises(NameError):
        #     test = get_last_app_line(t1[:-1])
        #     self.assertEqual(test , 103)

if __name__ == "__main__":
    unittest.main()
