import unittest
import global_values as gv

class setUp_Test(unittest.TestCase):

    def test_set_global_coefficients(self):
      self.assertEqual(gv.gk_Qmzk, 0.1)
      self.assertEqual(gv.gk_Qfun_sys, 0.05)
      gv.set_global_coefficients(Qfun_sys = 0)
      # gk_Qfun_sys = 0
      self.assertEqual(gv.gk_Qfun_sys, 0)
      gv.set_global_coefficients(Qmzk = 0)
      self.assertEqual(gv.gk_Qmzk, 0)
      gv.set_global_coefficients(Qmzk = 10, Qfun_sys = 10)
      self.assertEqual(gv.gk_Qfun_sys, 10)
      self.assertEqual(gv.gk_Qmzk, 10)
      gv.set_global_coefficients(Qfun_sys = 0.05, Qmzk = 0.1)
      self.assertEqual(gv.gk_Qfun_sys, 0.05)
      self.assertEqual(gv.gk_Qmzk, 0.1)

if __name__ == "__main__":
    unittest.main()
