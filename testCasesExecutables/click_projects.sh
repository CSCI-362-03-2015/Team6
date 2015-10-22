#!/bin/bash

#Builds the oracle for the test case
echo “Test Case 1” > /oracles/Test_Case_1
echo “Search” >> /oracles/Test_Case_1

#Updates the HTML doc with PASS/FAIL and test case info

touch temp/results.html
directory=${1-`pwd`}
echo "
<html>
    <body>
        <pre>
Team 6 test runner

" > temp/results.html

for filename in "$directory/testCases/*"
do
    head -n 3 $filename >> temp/results.html
    test=`awk '/EXECUTABLE/ {print $2}' $filename` 
    cp testCasesExecutables/$test testCasesExecutables/team6/$test;
    

    #Runs the test case
    python /home/web2py/web2py.py --no-banner -M -S \
    eden -R /home/web2py/applications/eden/tests/edentest_runner.py -A \
    /home/web2py/applications/eden/tests/implementation/testsuites/team6/click_projects \
    |grep -E '(PASS|FAIL)'|head -n 1 >> temp/results.html
    
    rm testCasesExecutables/team6/$test
done

echo "
    </pre>
  </body>
<html>" >> temp/results.html
