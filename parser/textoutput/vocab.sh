#!/bin/bash

mkdir -p readability

rm -f readability/vocabulary.csv

for i in clementattlee.txt gordonbrown.txt jacobreesmogg.txt johnmajor.txt nickclegg.txt williamhague.txt edmilliband.txt haroldwilson.txt jeremycorbyn.txt margaretthatcher.txt tonyblair.txt winstonchurchill.txt
do

	count=`cat $i | tokenizer -L en-u8 -n -s | sort | uniq | wc -l`
	name=`echo $i | cut -d . -f 1`
	
	echo "$name:$count"  >> readability/vocabulary.csv
done
