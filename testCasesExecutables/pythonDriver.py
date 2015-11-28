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
import getopt

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
    testList.append(file)
    #if file.endswith(".txt"):
        #testList.append(file)

#Itterates through the text file and assigns the class, method, inputs, etc. for use in the driver
numTests = len(testList)
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

        className = str(array[0].strip())
        folderLocation = className.split(' ',1)[0]
        classLocation = className.split(' ',1)[1]
        methodName = str(array[1].strip())
        inputData = array[2].strip()
        inputData1 = inputData.split(' ',1)[0]
	try:
            inputData2 = inputData.split(' ',1)[1]
        except IndexError:
	    inputData2 = " "
        oracle = array[3].strip() + ".txt"
        userPath = abspath(join(dirname( __file__ ), '../', ''))
        if(folderLocation != "modules"):
            eden = userPath + '/temp/eden/modules/' + str(folderLocation) + '/'
        else:
            eden = userPath + '/temp/eden/modules/'
        newPath = sys.path.insert(0, eden)
        #Imports the class name so that the method can be called
        module = __import__(str(classLocation))
        #module = importlib.import_module(className)

        #Sets x to the method to be called
        x = getattr(module, methodName)

        #Calls the tested method and places it in result to be compared with the orcale's expected output
        if (inputData2 == " "):
            result = x(inputData1)
        else:
            result = x(inputData1, inputData2)

        oracleLocation = abspath(join(dirname( __file__ ), '../', 'oracles'))
        array2 = []
        with open(oracleLocation + "/" + oracle, "r") as filein:
            k = 0
            for line in filein:
                array2.append(line.split(':',1)[-1])
                k+=1
        expectedOutput = str(array2[2].strip())
        description = array2[1]

        if (str(result) == str(expectedOutput)):
            outcome = "PASS"

        else:
            outcome = "FAIL"

        reportFile.write("Class Name:" + className + "\n" + "Method Name:" + methodName + "\n" + "Inputs:" + str(inputData1) + str(inputData2) + "\n" + "Description:" + description + "Oracle:" + oracle + "\n" + "Result:" + outcome + "\n")
        print("Class Name:" + className + "\n" + "Method Name:" +
                         methodName + "\n" + "Input:" + inputData + "\n" +
                         "Oracle:" + oracle + "\n")
reportFile.close()
