#!/bin/sh
year=$1
HARV=$2
PARS=$3


rm -f $PARS/LORDSsaved/toimport/yearcounts.csv
touch $PARS/LORDSsaved/toimport/yearcounts.csv

file="$PARS/LORDSsaved/toimport/vocab"
cnt=`cat $file | awk '{sum = sum + $2} END {print sum}'`
echo "$year,$cnt" >> $PARS/LORDSsaved/toimport/yearcounts.csv


echo "Created file"
echo "DELETE FROM yearcountsLords WHERE year=$year;"  | mysql 

while read line
do
	myyear=`echo $line | awk -F"," {'print $1'}`
	count=`echo $line | awk -F"," {'print $2'}`
	echo "INSERT INTO yearcountsLords (year, count) VALUES ('$myyear', '$count');" | mysql
done < $PARS/LORDSsaved/toimport/yearcounts.csv
