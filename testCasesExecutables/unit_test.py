#! /usr/bin/python 
#PROG Jeremy Butcheck
#PROJ Team6
#FROM 11/11/2015

import sys
import importlib
import fileinput
import functools
import os

import eden

sys.path.append(os.getcwd() + '/testCasesExecutables/eden/modules');
sys.path.append(os.getcwd() + '/home/web2py/gluon');
print sys.path 
my_input = []
my_output = ''

for line in fileinput.input():
    my_input.append(line.strip())

module_name = my_input[0].replace(" ",".") 
method_name = my_input[1] 
args = my_input[2:] 

mod = importlib.import_module('eden.{}'.format(module_name.replace(".py","")))
print mod

method = functools.partial(getattr(mod,'{}'.format(method_name)),args)
print method()
