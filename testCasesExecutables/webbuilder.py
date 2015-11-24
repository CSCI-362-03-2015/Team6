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
<table border="1" style="width:100%">
  <tr>
'''
    reportsLocation = abspath(join(dirname( __file__ ), '../', 'temp'))
    reportFile = open(reportsLocation + "/report.txt", 'r')
    for line in reportFile:
        contents+= "<td>" + str(line) + "</td>"
    contents+= '''
</tr>
</body>
</html>
'''
    print(contents)
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
