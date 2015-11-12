#!/bin/bash
#PROG Jeremy Butcheck
#PROJ Team6
#DATE 11/11/15

directory=${1-`pwd`}
file=$directory/input_file

for filename in "$directory/../testCases/"*
do 

echo $filename

driver=`awk '/driver:/ {print $2}' Test1`
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
echo "$input"

case "$driver" in 
    python)
          echo "$input" | ./unit_test.py
        #call that python driver
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
