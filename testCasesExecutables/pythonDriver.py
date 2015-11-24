#!/usr/bin/env python
#PROG Steven Draugel
#PROJ Team6
#FROM 11/23/2015

import importlib
import sys
import fileinput
import functools
from types import FunctionType
from os.path import *
import os
import sys

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#The shell needs to make a txt file calle testName.txt every time a
#test is run and put the name of the test case file in it. The this driver
#will parse that file(for 1 line containing the test case) and use it to call
#the test case.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Creates a list of all the test cases
filelocation = abspath(join(dirname( __file__ ), '../', 'testCases'))

report = abspath(join(dirname( __file__ ), '../', 'temp'))
reportFile = open(report + "/report.txt", 'a')
reportFile = open(report + "/report.txt", 'w')

testList = []
for file in os.listdir(str(filelocation)):
    if file.endswith(".txt"):
        testList.append(file)

#Itterates through the text file and assigns the class, method, inputs, etc. for use in the driver
numTests = len(testList)
print(numTests)
i = 0
for testCase in range(0, numTests):
    testName = abspath(join(dirname( __file__ ), '..', "testCases/" + str(testList[i])))
    array = []
    i+=1
    with open(testName, "r") as ins:
        j = 0
        for line in ins:
            array.append(line.split(':',1)[-1])
            j+=1

        className = str(array[0].strip().replace(" ", "."))
	className =  className.split('.',1)[-2]
        methodName = str(array[1].strip())
        inputData = array[2].strip()
        oracle = array[3].strip()
        eden = abspath(join(dirname( __file__ ), '../', 'docs/eden/modules'))
        newPath = sys.path.insert(0, eden)
        #Imports the class name so that the method can be called
	module = __import__(className)
        #module = importlib.import_module("arabic_reshaper.py", __name__)

        #Sets x to the method to be called
        x = getattr(module, methodName)

        #Calls the tested method and places it in result to be compared with the orcale's expected output
        result = x(inputData)

        oracleLocation = abspath(join(dirname( __file__ ), '..', 'oracles'))
        array2 = []
        with open(oracleLocation + "/" + oracle, "r") as filein:
            k = 0
            for line in filein:
                array2.append(line.split(':',1)[-1])
                k+=1

        expectedOutput = array2[2]
	description = array2[0]

        if (result == expectedOutput):
            outcome = "PASS"

        else:
            outcome = "FAIL"

        reportFile.write("Class Name: " + className + ", Method Name: " +
                         methodName + ", Input: " + inputData + ", Oracle: " + 
			 oracle + ", Result: " + outcome)
        print("Class Name: " + className + ", Method Name: " +
             methodName + ", Input: " + inputData + ", Description: " + description + ", Result: " + 
	     outcome)
reportFile.close()
