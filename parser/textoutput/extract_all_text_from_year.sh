#!/bin/bash
year=$1
HARV=$2
PARS=$3

# Remove previously generated files
rm -rf $PARS/$year
mkdir -p $PARS/$year

# Extract text
for i in `ls $HARV/hansard/debates$year*`
do	
	filename=`basename $i`
	python2.7 $PARS/harvest.py $i $HARV/hansard > $PARS/$year/$filename.txt
done

