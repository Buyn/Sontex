#!/bin/bash
clear
source sontex-env/bin/activate
# @echo off
while true; do
  # python -m unittest
  python3 -m unittest ingtest01
  python3 -m unittest test_main.Test_Init.test_gui_calc_params
  python3 -m unittest test_winmain.Test_Init.test_winmain_test
  python3 -m unittest test_winmain.Test_Init.test_btn_ask_open_exel_file 
  python3 -m unittest test_winmain.Test_Init.test_btn_ask_open_DBfiles 
  python3 -m unittest test_winmain.Test_Init.test_btn_asksaveasfile
  echo "Press any key to run tests again or Ctrl+C to exit..."
  read -n 1 -s
  clear
done
