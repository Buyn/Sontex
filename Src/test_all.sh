#!/bin/bash
clear
source sontex-env/bin/activate
# @echo off
while true; do
  python -m unittest
  echo "Press any key to run tests again or Ctrl+C to exit..."
  read -n 1 -s
  clear
done
