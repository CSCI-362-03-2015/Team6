#!/bin/bash
#PROG Jeremy Butcheck
#PROJ Team6
#DATE 11/11/15

#This script is meant to be run from scripts directory. Is NOT directory agnostic

directory=${1-`pwd`}

#iterate though testCases directory
for filename in "$directory/../testCases/"*
do 

echo $filename

#driver field from testcase file stored in $driver env variable 
driver=`awk '/driver:/ {print $2}' $filename`

#class , input , and oracle fields concatenated and stored in $input env variable
input=`awk '
BEGIN{
    FS=" "
    RS="\n"
    ORS="\n"
}
/method:/||/class:/||/input:/||/oracle:/{
    $1="";
    print;
}' $filename`

echo $driver
case "$driver" in 
    python)
        #call that python driver, pipe input variable
        #output to console
        echo "$input" | ./../testCasesExecutables/unit_test.py
        ;;
    selenium)
        #call selenium
        ;;
    robot)
        #call robot
        ;;
esac
echo

done
