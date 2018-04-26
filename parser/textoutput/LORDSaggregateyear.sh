#!/bin/sh
year=$1
HARV=$2
PARS=$3

yeardir=LORDS$1

echo "Aggregating $yeardir"
rm -f $PARS/$yeardir/total$year
for file in $PARS/$yeardir/*.txt
do 
	cat $file >> $PARS/$yeardir/total$yeardir
done
mv $PARS/$yeardir/total$yeardir $PARS/LORDS0_totals
