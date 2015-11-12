#! /usr/bin/python 

import sys
import importlib
import fileinput
import functools

#from target_folder.sym_ed import breakfast

from target_folder import sym_ed

my_input = []
my_output = ''

for line in fileinput.input():
    my_input.append(line.strip())

module_name = my_input[0] 
method_name = my_input[1] 
args = my_input[2:] 

mod = importlib.import_module('sym_ed.breakfast'.format(module_name))
print mod

x = functools.partial(getattr(mod,'{}'.format(method_name)))
x()

#print True
