import unittest
import sys
import os
import pandas as pd
from winmain import *
# (pyvenv-activate "sontex-env")

def load_exel(filename, sheet_name): 
    return pd.read_excel( filename,
                          sheet_name = sheet_name,
                          engine='openpyxl',
                          # index_col=0,
                          header=None,)

class Test(unittest.TestCase):

  def test_integ_initest(self):
      # sys.argv = ['', 'Test.testName']
      print(sys.argv)
      print(sys.argv[0])
      # print(sys.argv[1])
      # if sys.argv[1] == "ingtest01.Test.test_integ_initest": print("test found!!")

  def test_run_winmai_calc_exel(self):
    exel_path = "Data_files/test.xlsx"
    # csv_path = "Data_files/test.rlv"
    csv_path = None
    output_path = "Data_files/test_output.xlsx"
    # /home/buyn/Dev/Python/Sontex/Src/Data_files/output.xlsx
    home_counter = ""
    if os.path.exists(output_path):
      os.remove(output_path)

    self.assertFalse (os.path.exists(output_path), "Output file does exist")
    start_calc(exel_path, csv_path, output_path, home_counter)

    # Assert if the output file exists
    self.assertTrue(os.path.exists(output_path), "Output file does not exist")

    # gv_filename = "Data_files/test.xlsx"
    sheet_name = "Теплоенрго"
    df_report = load_exel(output_path, sheet_name)
    # print(df_report)
    self.assertIsNotNone(df_report )
    self.assertEqual(df_report.iloc[1, 1], "кв.1")
    self.assertEqual(df_report.iloc[1, 4], 2.326)
    self.assertEqual(df_report.shape[0], 41)
    self.assertEqual(df_report.iloc[40, 4], 63.72)

    sheet_name = "квартири, площі"
    df_report = load_exel(output_path, sheet_name)
    # print(df_report)
    self.assertIsNotNone(df_report )
    self.assertEqual(df_report.iloc[7, 1], "кв.7")
    # 8
    self.assertEqual(df_report.iloc[7, 18], 603)
    self.assertEqual(df_report.iloc[7, 17], 653)
    # 31
    self.assertEqual(df_report.iloc[30, 17], 445)
    self.assertEqual(df_report.iloc[30, 18], 437)
    self.assertEqual(df_report.shape[0], 141)
    self.assertEqual(df_report.iloc[109, 17], 1613.72)
    self.assertEqual(df_report.iloc[109, 18], 1550)

  def test_run_winmai_calc_home(self):
    exel_path = "Data_files/test.xlsx"
    csv_path = ""
    # csv_path = "Data_files/test.rlv"
    # csv_path = "Data_files/test.csv"
    output_path = "Data_files/test_output.xlsx"
    # /home/buyn/Dev/Python/Sontex/Src/Data_files/output.xlsx
    home_counter = [100,0]
    if os.path.exists(output_path):
      os.remove(output_path)

    self.assertFalse (os.path.exists(output_path), "Output file does exist")
    start_calc(exel_path, csv_path, output_path, home_counter)

    # Assert if the output file exists
    self.assertTrue(os.path.exists(output_path), "Output file does not exist")

    # gv_filename = "Data_files/test.xlsx"
    sheet_name = "Теплоенрго"
    df_report = load_exel(output_path, sheet_name)
    # print(df_report)
    self.assertIsNotNone(df_report )
    self.assertEqual(df_report.iloc[1, 1], "кв.1")
    self.assertEqual(df_report.iloc[1, 4], 3.65)
    self.assertEqual(df_report.shape[0], 41)
    self.assertEqual(df_report.iloc[40, 4], 100)

    sheet_name = "квартири, площі"
    df_report = load_exel(output_path, sheet_name)
    # print(df_report)
    self.assertIsNotNone(df_report )
    self.assertEqual(df_report.iloc[7, 1], "кв.7")
    # 8
    self.assertEqual(df_report.iloc[7, 18], 603)
    self.assertEqual(df_report.iloc[7, 17], 653)
    # 31
    self.assertEqual(df_report.iloc[30, 17], 445)
    self.assertEqual(df_report.iloc[30, 18], 437)
    self.assertEqual(df_report.shape[0], 141)
    self.assertEqual(df_report.iloc[109, 17], 100)
    self.assertEqual(df_report.iloc[109, 18], 0)

  def test_run_winmai_calc_rlv(self):
    exel_path = "Data_files/test.xlsx"
    # csv_path = ""
    csv_path = "Data_files/test.rlv"
    # csv_path = "Data_files/test.csv"
    output_path = "Data_files/test_output.xlsx"
    # /home/buyn/Dev/Python/Sontex/Src/Data_files/output.xlsx
    home_counter = None
    if os.path.exists(output_path):
      os.remove(output_path)

    self.assertFalse (os.path.exists(output_path), "Output file does exist")
    start_calc(exel_path, csv_path, output_path, home_counter)

    # Assert if the output file exists
    self.assertTrue(os.path.exists(output_path), "Output file does not exist")

    # gv_filename = "Data_files/test.xlsx"
    sheet_name = "Теплоенрго"
    df_report = load_exel(output_path, sheet_name)
    # print(df_report)
    self.assertIsNotNone(df_report )
    self.assertEqual(df_report.iloc[1, 1], "кв.1")
    self.assertEqual(df_report.iloc[1, 4], 2.326)
    self.assertEqual(df_report.shape[0], 41)
    self.assertEqual(df_report.iloc[40, 4], 63.72)

    sheet_name = "квартири, площі"
    df_report = load_exel(output_path, sheet_name)
    # print(df_report)
    self.assertIsNotNone(df_report )
    self.assertEqual(df_report.iloc[7, 1], "кв.7")
    # 8
    self.assertEqual(df_report.iloc[7, 18], 603)
    self.assertEqual(df_report.iloc[7, 17], 653)
    # 31
    self.assertEqual(df_report.iloc[30, 17], 195)
    self.assertEqual(df_report.iloc[30, 18], 437)
    self.assertEqual(df_report.shape[0], 141)
    self.assertEqual(df_report.iloc[109, 17], 1613.72)
    self.assertEqual(df_report.iloc[109, 18], 1550)

  def test_run_winmai_calc_rlv_csv(self):
    exel_path = "Data_files/test.xlsx"
    # csv_path = ""
    csv_path = "Data_files/test.rlv;Data_files/test.csv"
    # csv_path = "Data_files/test.csv"
    output_path = "Data_files/test_output.xlsx"
    # /home/buyn/Dev/Python/Sontex/Src/Data_files/output.xlsx
    home_counter = None
    if os.path.exists(output_path):
      os.remove(output_path)
    # Assert if the output file exists
    self.assertFalse (os.path.exists(output_path), "Output file does exist")
    start_calc(exel_path, csv_path, output_path, home_counter)
    # Assert if the output file not exists
    self.assertTrue(os.path.exists(output_path), "Output file does not exist")
    # gv_filename = "Data_files/test.xlsx"
    sheet_name = "Теплоенрго"
    df_report = load_exel(output_path, sheet_name)
    # print(df_report)
    self.assertIsNotNone(df_report )
    self.assertEqual(df_report.iloc[1, 1], "кв.1")
    self.assertEqual(df_report.iloc[1, 4], 2.326)
    self.assertEqual(df_report.shape[0], 41)
    self.assertEqual(df_report.iloc[40, 4], 63.72)
    sheet_name = "квартири, площі"
    df_report = load_exel(output_path, sheet_name)
    # print(df_report)
    self.assertIsNotNone(df_report )
    self.assertEqual(df_report.iloc[7, 1], "кв.7")
    # 8
    self.assertEqual(df_report.iloc[7, 18], 603)
    self.assertEqual(df_report.iloc[7, 17], 126)
    # 31
    self.assertEqual(df_report.iloc[30, 17], 76)
    self.assertEqual(df_report.iloc[30, 18], 437)
    self.assertEqual(df_report.shape[0], 141)
    self.assertEqual(df_report.iloc[109, 17], 1613.72)
    self.assertEqual(df_report.iloc[109, 18], 1550)

if __name__ == "__main__":
    print("args = ", sys.argv)
    unittest.main()
