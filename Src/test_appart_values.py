# ----------------------------------------------
# * import block :
import unittest

from appart_values import *


# ----------------------------------------------
# * class Test_Init : 
# ** ------------------------------------------:
class Test_Init(unittest.TestCase):

# ----------------------------------------------
# ** def test_init1 : 
    def test_init1(self):# {{{
        print("Init Test")
        # self.assertIsNone(main(1))


# ** def test_get_next_appindex : 
    def test_get_next_appindex(self):# {{{
        # last_app = 101
        # last_app = 100
        # next_app, end_app = get_next_appindex(last_app)
        # print("next is = ", next_app)
        # print("next value", df.iloc[next_app, 0])
        # print("naber of counters = ", next_app - last_app)
        # if end_app:
        #     print("end of list")
        pass


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
