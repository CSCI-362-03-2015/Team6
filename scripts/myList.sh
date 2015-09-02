#!/bin/bash
#PROG Jeremy, Pat, Aaron (Team6)
#FROM 09/02/2015
#PURP display project directory structure in a browser

#Code for finding directory of script using environmental variables found on stack overflow
#http://stackoverflow.com/questions/59895/can-a-bash-script-tell-what-directory-its-stored-in
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
touch $DIR/../temp/directory.html
echo "<html>
<body>
<pre>
" > $DIR/../temp/directory.html
ls -R $DIR/../ >> $DIR/../temp/directory.html
echo "</pre></body>
<html>" >> $DIR/../temp/directory.html
google-chrome $DIR/../temp/directory.html


