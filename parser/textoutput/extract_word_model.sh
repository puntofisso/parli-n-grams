#!/bin/bash
DIR=/home/AccHack14/parser/textoutput
#year=$1
#if [ $# -eq 0 ]
#then
#echo "No year supplied"
#exit
#fi

year=1986

# Extract text
for i in `ls /home/AccHack14/harvester/hansard/debates$year*`
do	
	filename=`basename $i`
	python2.7 harvestWordModel.py $i 
done

