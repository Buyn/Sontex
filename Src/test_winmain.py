# ----------------------------------------------
# * import block :
import unittest
import sys

from winmain import *
from main import *


# ----------------------------------------------
# * class Test_Init : 
# ** ------------------------------------------:
class Test_Init(unittest.TestCase):

# ----------------------------------------------
# ** def test_winmain : 
    @unittest.skipIf(len(sys.argv) < 2  or sys.argv[1] != "test_winmain.Test_Init", "not sigle test")
    def test_winmain_test(self):
        # # sys.argv = ['', 'Test.testName']
        print(sys.argv)
        print(sys.argv[0])
        print(sys.argv[1])
        if sys.argv[1] == "test_winmain.Test_Init": print("test found")

        
# ----------------------------------------------

# ** def test_btn_ResimyoluClick : 
    @unittest.skipIf(len(sys.argv) < 2  or not sys.argv[1] == "test_winmain.Test_Init.test_btn_ResimyoluClick", "not sigle test")
    def test_btn_ResimyoluClick(self):
        test = btn_ResimyoluClick("",
                                  _filetypes=(("csv files","*.csv"), ("rlv files","*.rlv")),
                                  _title = "Select file csv or rlv")
        test = btn_ResimyoluClick("",
                                  _filetypes=[("csv files","*.csv"), ("rlv files","*.rlv")],
                                  _title = "Select file csv or rlv")
        test = btn_ResimyoluClick("")
        test = btn_ResimyoluClick("",
                                  _filetypes=("csv files","*.csv"),
                                  _title = "Select file csv")
            

# ----------------------------------------------

# ** def test_btn_ask_open_exel_file : 
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
        # test = btn_ask_open_exel_file("",
        #                           _filetypes=(("csv files","*.csv"), ("rlv files","*.rlv")),
        #                           _title = "Select file csv or rlv")
        # test = btn_ask_open_exel_file("",
        #                           _filetypes=[("csv files","*.csv"), ("rlv files","*.rlv")],
        #                           _title = "Select file csv or rlv")
        # test = btn_ask_open_exel_file("")
        # test = btn_ask_open_exel_file("",
        #                           _filetypes=("csv files","*.csv"),
        #                           _title = "Select file csv")
            

# ----------------------------------------------

# ** def test_btn_ask_open_DBfiles : 
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
        # test = btn_ask_open_DBfiles("\\",
        #                           # _filetypes=(("csv files","*.csv"), ("rlv files","*.rlv")),
        #                           _title = "test path \\")
        # test = btn_ask_open_DBfiles("",
        #                           _filetypes=(("csv files","*.csv"), ("rlv files","*.rlv")),
        #                           _title = "Select file csv or rlv")
        # test = btn_ask_open_DBfiles("",
        #                           _filetypes=[("csv files","*.csv"), ("rlv files","*.rlv")],
        #                           _title = "Select file csv or rlv")
        # test = btn_ask_open_DBfiles("")
        # test = btn_ask_open_DBfiles("",
        #                           _filetypes=("csv files","*.csv"),
        #                           _title = "Select file csv")
            

# ----------------------------------------------

# ** def test_btn_asksaveasfile : 
    @unittest.skipIf(len(sys.argv) < 2  or not sys.argv[1] == "test_winmain.Test_Init.test_btn_asksaveasfile", "not sigle test")
    def test_btn_asksaveasfile(self):
        test = btn_asksaveasfile("")
        test = btn_asksaveasfile("",
                          _filetypes=("csv files","*.csv"),
                          _title = "Select file to save report")
            

# ----------------------------------------------
# ** def test_Pull_log : 
    def test_test_Pull_log(self):
        gui_log.clear()
        self.assertEqual(len(gui_log), 0)          
        print_to_log("test")
        self.assertEqual(len(gui_log), 1)          
        test = pull_log()
        self.assertEqual(test, ["test"])          
        self.assertEqual(test[0], "test")          
        self.assertEqual(len(gui_log), 0)          


            

# ----------------------------------------------
# * Test runer : 
# ** ------------------------------------------:
# (compile " D:/Development/version-control/GitHub/Vadim/Tochil/main_test.py -k init")
# (compile " python -m unittest D:/Development/version-control/GitHub/Vadim/Tochil/main_test.py ")
# ** if __main__: 
if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(suite_Init())
    import sys
    # sys.argv = ['', 'Test.testName']
    print("args = ", sys.argv)
    unittest.main()


# ----------------------------------------------
# * -------------------------------------------:
