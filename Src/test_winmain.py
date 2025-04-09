import unittest
import sys

from winmain import *
from main import *

class Test_Init(unittest.TestCase):

    @unittest.skipIf(len(sys.argv) < 2  or sys.argv[1] != "test_winmain.Test_Init", "not sigle test")
    def test_winmain_test(self):
        # # sys.argv = ['', 'Test.testName']
        print(sys.argv)
        print(sys.argv[0])
        print(sys.argv[1])
        if sys.argv[1] == "test_winmain.Test_Init": print("test found")

    def test_get_dates_from_filename_string(self):
      string = "Data_files/test.rlv"
      t = get_dates_from_filename_string(string)
      # print(t)
      self.assertEqual(len(t), 19)
      self.assertEqual(t[0], "02.04.2023")
      self.assertEqual(t[1], "01.04.2023")
      t =None
      string = "Data_files/test.rlv;Data_files/test.csv"
      t = get_dates_from_filename_string(string)
      self.assertEqual(len(t), 19)
      self.assertEqual(t[0], "02.04.2023")
      self.assertEqual(t[1], "01.04.2023")
      t =None
      string = " ;   Data_files/test.rlv ;  Data_files/test.csv  ;"
      t = get_dates_from_filename_string(string)
      self.assertIsNotNone(t)
      self.assertEqual(len(t), 19)
      self.assertEqual(t[0], "02.04.2023")
      self.assertEqual(t[1], "01.04.2023")
      t =None
      string = "Data_files/test.csv;Data_files/test.rlv"
      t = get_dates_from_filename_string(string)
      self.assertEqual(len(t), 37)
      self.assertEqual(t[0], "19.04.2021 13:52:24")
      self.assertEqual(t[1], "2021-04-16")

    @unittest.skipIf(len(sys.argv) < 2  or not sys.argv[1] == "test_winmain.Test_Init.test_btn_ask_open_exel_file", "not sigle test")
    def test_btn_ask_open_exel_file(self):
        test = btn_ask_open_exel_file("/",
                                  # _filetypes=(("csv files","*.csv"), ("rlv files","*.rlv")),
                                  _title = "test path /")
        test = btn_ask_open_exel_file("D:/Development/version-control/GitHub/Zmei/Sontex/Src/Data_files/test.xlsx",
                                  # _filetypes=(("csv files","*.csv"), ("rlv files","*.rlv")),
                                  _title = "D:/Development/version-control/GitHub/Zmei/Sontex/Src/Data_files/test.xlsx")
        test = btn_ask_open_exel_file("\\",
                                  # _filetypes=(("csv files","*.csv"), ("rlv files","*.rlv")),
                                  _title = "test path \\")

    @unittest.skipIf(len(sys.argv) < 2  or not sys.argv[1] == "test_winmain.Test_Init.test_btn_ask_open_DBfiles", "not sigle test")
    def test_btn_ask_open_DBfiles(self):
        test = btn_ask_open_DBfiles("/",
                                  # _filetypes=(("csv files","*.csv"), ("rlv files","*.rlv")),
                                  _title = "test path /")
        print("test = ", test)
        test = btn_ask_open_DBfiles("D:/Development/version-control/GitHub/Zmei/Sontex/Src/Data_files/test.xlsx",
                                  # _filetypes=(("csv files","*.csv"), ("rlv files","*.rlv")),
                                  _title = "D:/Development/version-control/GitHub/Zmei/Sontex/Src/Data_files/test.xlsx")
        print("test = ", test)

    @unittest.skipIf(len(sys.argv) < 2  or not sys.argv[1] == "test_winmain.Test_Init.test_btn_asksaveasfile", "not sigle test")
    def test_btn_asksaveasfile(self):
        test = btn_asksaveasfile("")
        test = btn_asksaveasfile("",
                          _filetypes=("csv files","*.csv"),
                          _title = "Select file to save report")

    def test_Pull_log(self):
        gui_log.clear()
        self.assertEqual(len(gui_log), 0)          
        import datetime
        x = datetime.datetime.now().strftime("%H:%M:%S.%f")+": "
        print_to_log("test")
        self.assertEqual(len(gui_log), 1)          
        test = pull_log()
        self.assertNotEqual(test, [x+"test"])          
        self.assertNotEqual(test[0], x+"test")          
        self.assertEqual(len(gui_log), 0)

# ** if __main__: 
if __name__ == "__main__":
    import sys
    print("args = ", sys.argv)
    unittest.main()
