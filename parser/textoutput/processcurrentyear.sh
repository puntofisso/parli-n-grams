#!/bin/bash
year=$1
if [ $# -eq 0 ]
then
echo "No year supplied"
exit
fi

PARLI=/var/www/html/parli-n-grams
HARV=$PARLI/harvester/
PARS=$PARLI/parser/textoutput

echo "Updating Hansard..."
$HARV/update.sh $HARV

echo "Extracting text"
$PARS/extract_all_text_from_year.sh $year $HARV $PARS

echo "Aggregating text for year"
$PARS/aggregateyear.sh $year $HARV $PARS

echo "Running data mining"
$PARS/word.sh $year $HARV $PARS

echo "Updating DB"
$PARS/updateyeardb.sh $year $HARV $PARS

echo "Updating counts"
$PARS/updateyearcounts.sh $year $HARV $PARS

echo "Updating lastupdate string"
$PARS/lastupdated.sh
