#!/bin/bash
#PROG Jeremy Butcheck
#PROJ Team6
#DATE 11/11/15

#directory= ${1-`pwd`}
file=$directory/input_file
driver=`awk '/driver:/ {print $2}' input_file`

input=`awk '
BEGIN{
    FS=" "
    RS="\n"
    ORS="\n"
}
/method:/||/module:/||/input:/||/oracle:/{
    $1="";
    print;
}' input_file`
echo "$input"

case "$driver" in 
    python)
          echo "$input" | ./script_runner.py
        #call that python driver
        ;;
    selenium)
        #call selenium
        ;;
    robot)
        #call robot
        ;;
esac


