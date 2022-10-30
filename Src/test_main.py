# ----------------------------------------------
# * import block :
import unittest

from main import *


# ----------------------------------------------
# * class Test_Init : 
# ** ------------------------------------------:
class Test_Init(unittest.TestCase):

# ----------------------------------------------
# ** def test_init1 : 
    def test_init1(self):# {{{
        print("Init Test")
        # self.assertIsNone(main(1))


# ** def test_main : 
    def test_main(self):# {{{
        # print("Test tuner")
        # self.assertIsNone(main(1))
        with self.assertRaises(SystemExit) as cm:
            main(1)
        self.assertEqual(cm.exception.code, 0)


# ----------------------------------------------
# ** def test_load_exel : 
    def test_load_exel(self):# {{{
        filename = "Data_files/test.xlsx"
        # sheet_name = "показники"
        sheet_name = "квартири, площі"
        df = load_exel(filename, sheet_name)
        self.assertEqual( df.iloc[100, 0], 36)
        self.assertEqual( df.iloc[104, 0], 37)
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
        pass


# ----------------------------------------------
# * class setUp_Test : 
class setUp_Test(unittest.TestCase):
# ** @classmethod #setUpClass#  : 
    @classmethod #setUpClass# {{{
    def setUpClass(self):
        print("*"*33,"*"*33)
        filename = "Data_files/test.xlsx"
        # sheet_name = "показники"
        sheet_name = "квартири, площі"
        self.df = load_exel(filename, sheet_name)
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
        self.assertEqual(self.df.iloc[100, 0], 36)
        self.assertEqual(self.df.iloc[104, 0], 37)
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
        self.assertEqual(t2[0], None)
        self.assertEqual(t2[37], [
                                25482673,
                                25482672,])
        # print(t2[36])
        # print(t2[37])
        # print(t2[35])
        # print(t2[34])
        # print(t2[33])


# ** ---------------------------------------------:
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
# * ----------------------------------------------:
