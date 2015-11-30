import importlib
import sys
import fileinput
import functools
from types import FunctionType
from os.path import *
import os
import sys

def main():
    contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>Team 6 Testing Framework Report</title>
	
</head>
<body>

<h1> Team6 </h1>
<h2> Eden Test Results </h2>
<table border="1"  style="width:100%">
  <tr>
	<th> Class Name: </th>
	<th> Module Name: </th>
	<th> Input: </th>
	<th> Description: </th>
	<th> Oracle: </th>
	<th> Result: </th>
 </tr>
 <tr>
'''
    reportsLocation = abspath(join(dirname( __file__ ), '../', 'temp'))
    reportFile = open(reportsLocation + "/report.txt", 'r')
    i = 0
    for line in reportFile:
        if(i == 6):
        	i = 0
        	contents+= "</tr>" + "<tr>" 
        contents+= "<td>" + str(line) + "</td>"
        i+=1
    contents+= '''
</tr>
</body>
</html>
'''
    browseLocal(contents)

def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename))

main()
