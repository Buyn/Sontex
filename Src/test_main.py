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
        self.assertIsNone(main(1))


# ----------------------------------------------
# ** def load_exel : 
    def load_exel(self):# {{{
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
        # print(df.iloc[0:5, 0:2])
        print(df.iloc[101, 0])
        print(df.iloc[102, 0])
        print(df.iloc[103, 0])
        print(df.iloc[104, 0])
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
