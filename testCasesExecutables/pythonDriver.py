#! /usr/bin/python 
#PROG Steven Draugel
#PROJ Team6
#FROM 11/19/2015

import importlib
import sys
import fileinput
import functools
from types import FunctionType
from os.path import *
import os
import sys
#import eden

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#The shell needs to make a txt file calle testName.txt every time a
#test is run and put the name of the test case file in it. The this driver
#will parse that file(for 1 line containing the test case) and use it to call
#the test case.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
outcome = ""

#Creates a list of all the test cases
filelocation = abspath(join(dirname( __file__ ), '..', 'testcases'))
testList = []
for file in os.listdir(filelocation):
    if file.endswith(".txt"):
        testList.append(file)

#Itterates through the text file and assigns the class, method, inputs, etc. for use in the driver

numTests = len(testList)

for testCase in range(0, numTests):
    i = 0
    testName = abspath(join(dirname( __file__ ), '..', "testcases/" + str(testList[i])))
    print(testName)
    i+=1
    array = []
    with open(testName, "r") as ins:
        j = 0
        for line in ins:
            array.append(line.split(':',1)[-1])
            print(array[j])
            j+=1

        className = array[0].strip().replace(" ", ".")
        methodName = str(array[1].strip())
        inputData = array[2].strip()
        oracle = array[3].strip()
        oracle += ".txt"
        print("Oracle: " + oracle)

        eden = abspath(join(dirname( __file__ ), '..', 'Eden'))
        sys.path.insert(0, eden)
        
        #Imports the class name so that the method can be called

        module = importlib.import_module(className)

        #Sets x to the method to be called
        x = getattr(module, methodName)

        #Calls the tested method and places it in result to be compared with the orcale's expected output
        result = x(inputData)
        print("Result: " + result)

        oracleLocation = abspath(join(dirname( __file__ ), '..', 'oracles'))
        print(oracleLocation)
        array2 = []
        with open(oracleLocation + "\\" + oracle, "r") as filein:
            i = 0
            for line in filein:
                array2.append(line.split(':',1)[-1])
                i+=1

        expectedOutput = array2[2]
        print("Expected: " + expectedOutput)

        if (result == expectedOutput):
            outcome = "PASS"

        else:
            outcome = "FAIL"

        #return outcome
        print(outcome)
