#!/bin/bash
year=$1
HARV=$2
PARS=$3

file="$PARS/saved/toimport/vocab"

echo "DELETE FROM ngrams WHERE year = '$year';"  | mysql 

basesql="INSERT INTO ngrams (ngram, year, count) VALUES"
counter=0
sql=""
len=`wc -l $file | awk {'print $1;'}`


while read line
do
	ngram=`echo $line | awk {'print $1'}`
	count=`echo $line | awk {'print $2'}`
	thissql="('$ngram', '$year', '$count')"

	if [ $(( $counter % 5000 )) -eq 0 ]; then
		echo "Processed $counter / $len"
		sql="$basesql $sql $thissql;"
		echo $sql | mysql
		sql=""
	else
		sql="$sql $thissql,"
	fi

	counter=`expr $counter + 1`
done < $file

if [[ ! -z $sql ]]; then
	sql="$basesql $sql"
	sql=${sql%?};
	sql="$sql;"
	echo $sql | mysql
	echo "Processed $counter / $len"
fi
