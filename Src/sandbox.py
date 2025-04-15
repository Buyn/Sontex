from global_values import *

# gk_Qfun_sys = 0.05
# gk_Qmzk = 0.1
print("befor gk_Qfun_sys=", gk_Qfun_sys)
print("befor gk_Qmzk=", gk_Qmzk)

def fun01():
  global gk_Qfun_sys, gk_Qmzk
  print("in fun 01 befor gk_Qfun_sys=", gk_Qfun_sys)
  print("in fun 01 befor gk_Qmzk=", gk_Qmzk)
  gk_Qfun_sys = 1
  gk_Qmzk = 1
  print("in fun 01 befor gk_Qfun_sys=", gk_Qfun_sys)
  print("in fun 01 befor gk_Qmzk=", gk_Qmzk)

fun01()

# gk_Qfun_sys = 0.05
# gk_Qmzk = 0.1
print("befor gk_Qfun_sys=", gk_Qfun_sys)
print("befor gk_Qmzk=", gk_Qmzk)

def fun02():
  global gk_Qfun_sys, gk_Qmzk
  print("in fun 02 befor gk_Qfun_sys=", gk_Qfun_sys)
  print("in fun 02 befor gk_Qmzk=", gk_Qmzk)
  gk_Qfun_sys = 0.11
  gk_Qmzk = 0.11
  print("in fun 02 befor gk_Qfun_sys=", gk_Qfun_sys)
  print("in fun 02 befor gk_Qmzk=", gk_Qmzk)

fun02()
fun01()
fun02()
