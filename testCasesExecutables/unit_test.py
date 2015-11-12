#! /usr/bin/python 

import sys
import importlib
import fileinput
import functools

import eden_modules

my_input = []
my_output = ''

for line in fileinput.input():
    my_input.append(line.strip())

module_name = my_input[0] 
method_name = my_input[1] 
args = my_input[2:] 

mod = importlib.import_module('eden_modules.{}'.format(module_name.replace(".py","")))
print mod

method = functools.partial(getattr(mod,'{}'.format(method_name)),args)
print method()

