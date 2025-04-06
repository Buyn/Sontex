#!/bin/bash
source sontex-env/bin/activate
# @echo off
while true; do
  # python -m unittest
  python3 -m unittest ingtest01.Test.test_integ_initest
  echo "Press any key to run tests again or Ctrl+C to exit..."
  read -n 1 -s
  clear
done
