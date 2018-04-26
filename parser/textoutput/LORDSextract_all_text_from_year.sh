#!/bin/bash
year=$1
HARV=$2
PARS=$3

# Remove previously generated files
rm -rf $PARS/LORDS$year
mkdir -p $PARS/LORDS$year

# Extract text
for i in `ls $HARV/hansardLords/daylord$year*`
do	
	filename=`basename $i`
	python2.7 $PARS/LORDSharvest.py $HARV/hansardLords $i > $PARS/LORDS$year/$filename.txt
done

