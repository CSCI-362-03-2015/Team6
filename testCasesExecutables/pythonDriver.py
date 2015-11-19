#! /usr/bin/python 
#PROG Steven Draugel
#PROJ Team6
#FROM 11/19/2015

import importlib
import sys
import fileinput
import functools
from types import FunctionType
#import eden

#~~~~~~~~~Need to figure out how to pass in with shell~~~~~~~~~~~~
testName = "test1.txt"
outcome = ""

#Itterates through the text file and assigns the class, method, inputs, etc. for use in the driver
array = []
with open(testName, "r") as ins:
    i = 0
    for line in ins:
        array.append(line.split(':',1)[-1])
        print(array[i])
        i+=1

className = array[0].strip().replace(" ", ".")
methodName = str(array[1].strip())
inputData = array[2].strip()
oracle = array[3].strip()
oracle += ".txt"

#Imports the class name so that the method can be called
module = importlib.import_module(className)

#Sets x to the method to be called
x = getattr(module, methodName)

#Calls the tested method and places it in result to be compared with the orcale's expected output
result = x(inputData)
print("Result: " + result)

array2 = []
with open(oracle, "r") as filein:
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
