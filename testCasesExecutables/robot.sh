#!/bin/bash
#Creates the directory to hold the tests
mkdir home/web2py/applications/eden/tests/implementation/testsuits/robot_tests

#Moves all test cases to the correct location to be run
for file in *.txt;
do
mv ~/Desktop/tests/"$file" /home/web2py/applications/eden/tests/implementation/testsuits/robot_tests
done

#runs all of the test cases
for file in *.txt;
do
pybot /home/web2py/applications/eden/tests/implementation/testsuites/robot_tests/"$file"
done
