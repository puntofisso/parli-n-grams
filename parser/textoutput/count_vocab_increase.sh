#!/bin/bash


for i in readability/*.tokenized 
do
	rm -f $i.increments
	totallength=`wc -l $i | awk {'print $1'}`
	#echo "Total Words Spoken: $totallength"
	totalvocabulary=`sort $i | uniq | wc -l`
	#echo "Total Vocabulary: $totalvocabulary"
	for j in `seq 50 50 10000`
	do
		vocab=`head -$j $i | sort | uniq | wc -l`
		echo "$j,$vocab" >> $i.increments
	done
done
