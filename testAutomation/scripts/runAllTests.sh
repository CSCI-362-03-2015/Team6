#!/bin/bash

echo Running all testcases.......
sleep 1

#Runs all of the Python tests
python ../testCasesExecutables/pythonDriver.py
sleep 1

echo Opening default browser with results....
sleep 1
#Opens a browser and displays the results of pythonDriver.py
python ../testCasesExecutables/webbuilder.py
