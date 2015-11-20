#!/bin/bash

touch home/web2py/applications/eden/tests/implementation/testsuits/selenium_tests

#Creates the directory to hold the tests
mkdir home/web2py/applications/eden/tests/implementation/testsuits/selenium_tests

#Moves all test cases to the correct location to be run
for file in *.py;
do
mv ~/testCases/tests/"$file" /home/web2py/applications/eden/tests/implementation/testsuits/selenium_tests
done

#runs all of the test cases
for file in *.py;
do
python /home/web2py/applications/eden/tests/implementation/testsuites/selenium_tests/"$file"
done
