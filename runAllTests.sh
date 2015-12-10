#!/bin/bash

echo Running all testcases.......
sleep 3

#Runs all of the Python tests
python ./TestAutomation/testCasesExecutables/pythonDriver.py
sleep 3

echo Opening default browser with results....
sleep 3
#Opens a browser and displays the results of pythonDriver.py
python ./TestAutomation/testCasesExecutables/webbuilder.py
