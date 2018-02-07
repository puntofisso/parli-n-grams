#!/bin/sh
year=$1
HARV=$2
PARS=$3


rm -f $PARS/saved/toimport/yearcounts.csv
touch $PARS/saved/toimport/yearcounts.csv

file="$PARS/saved/toimport/vocab"
cnt=`cat $file | awk '{sum = sum + $2} END {print sum}'`
echo "$year,$cnt" >> $PARS/saved/toimport/yearcounts.csv


echo "Created file"
echo "DELETE FROM yearcounts WHERE year=$year;"  | mysql 

while read line
do
	myyear=`echo $line | awk -F"," {'print $1'}`
	count=`echo $line | awk -F"," {'print $2'}`
	echo "INSERT INTO yearcounts (year, count) VALUES ('$myyear', '$count');" | mysql
done < $PARS/saved/toimport/yearcounts.csv
