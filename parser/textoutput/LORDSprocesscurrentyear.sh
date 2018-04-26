#!/bin/bash
year=$1
if [ $# -eq 0 ]
then
echo "No year supplied"
exit
fi

PARLI=/var/www/html/parli-n-grams
PARLI=/Users/puntofisso/Dropbox/DEV/parli-n-grams/parli-n-grams
HARV=$PARLI/harvester/
PARS=$PARLI/parser/textoutput

echo "Updating Hansard..."
$HARV/updateLords.sh $HARV

echo "Extracting text"
$PARS/LORDSextract_all_text_from_year.sh $year $HARV $PARS

echo "Aggregating text for year"
$PARS/LORDSaggregateyear.sh $year $HARV $PARS

exit

echo "Running data mining"
$PARS/LORDSword.sh $year $HARV $PARS

echo "Updating DB"
$PARS/LORDSupdateyeardb.sh $year $HARV $PARS

echo "Updating counts"
$PARS/LORDSupdateyearcounts.sh $year $HARV $PARS

#echo "Updating lastupdate string"
#$PARS/lastupdated.sh

#echo "Shutting down"
#sudo shutdown -h now
