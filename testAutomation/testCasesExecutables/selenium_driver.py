#!/usr/bin/env python
#PROG Aaron Monahan
#PROJ Team6
#FROM 11/30/2015

import importlib
import sys
import fileinput
import functools
from types import FunctionType
from os.path import *
import os
import sys
import getopt
import subprocess





filelocation = abspath(join(dirname( __file__ ), '../', 'testCases/selTests'))

report = abspath(join(dirname( __file__ ), '../', 'temp'))
reportFile = open(report + "/report.txt", 'a')
reportFile = open(report + "/report.txt", 'w')


testList = []
for file in os.listdir(str(filelocation)):
	testList.append(file)

numTests = len(testList)
i = 0
for testCase in range(0, numTests):
	testName = abspath(join(dirname( __file__ ), '..', "testCases/selTests/" + str(testList[i])))
	array = []
	i+=1
	with open(testName, "r") as ins:
        	j = 0
		print("----Running Test: " + testName + "----")
		filename = basename(testName)
		subprocess.call(['python', testName])
		



