#!/bin/bash

if [ -z "$1" ]
  then
    echo "No argument supplied"
    exit 255
fi
DIR=/home/AccHack14/parser/textoutput
TEXTDIR=0_totals
OUTDIR=saved
FILE=total$1
WORD2VEC=/home/AccHack14/parser/textoutput/word2vec


# round 1 (1grams)
$WORD2VEC/word2phrase -debug 5 -train $DIR/$TEXTDIR/$FILE -output $DIR/$OUTDIR/$FILE\_phrase_1.txt -min-count 1 -threshold 30

#round 2 (up to 4 grams)
$WORD2VEC/word2phrase -debug 5 -train $DIR/$OUTDIR/$FILE\_phrase_1.txt -output $DIR/$OUTDIR/$FILE\_phrase_2.txt -min-count 1 -threshold 30

#round 3 (up to 8grams)
$WORD2VEC/word2phrase -debug 5 -train $DIR/$OUTDIR/$FILE\_phrase_2.txt -output $DIR/$OUTDIR/$FILE\_phrase_3.txt -min-count 1 -threshold 30

# generate model
$WORD2VEC/word2vec -train $DIR/$OUTDIR/$FILE\_phrase_3.txt -cbow 0 -output model2015.txt 

rm -f $DIR/$OUTDIR/$FILE\_phrase_1.txt
rm -f $DIR/$OUTDIR/$FILE\_phrase_2.txt
rm -f $DIR/$OUTDIR/$FILE\_phrase_3.txt
