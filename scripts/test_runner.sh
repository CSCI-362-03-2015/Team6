#!/bin/bash
scriptsdir=tests

for SCRIPT in "$scriptsdir"/*
do
	"$SCRIPT"
done

		
