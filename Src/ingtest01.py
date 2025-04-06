import unittest
import sys
from winmain import *
# (pyvenv-activate "sontex-env")

class Test(unittest.TestCase):

  @unittest.skipIf(len(sys.argv) < 2  or sys.argv[1] != "ingtest01.Test.test_integ_initest", "not sigle test")
  def test_integ_initest(self):
      # sys.argv = ['', 'Test.testName']
      print(sys.argv)
      print(sys.argv[0])
      print(sys.argv[1])
      if sys.argv[1] == "ingtest01.Test.test_integ_initest": print("test found!!")

if __name__ == "__main__":
    print("args = ", sys.argv)
    unittest.main()
