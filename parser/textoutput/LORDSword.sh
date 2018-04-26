#!/bin/bash
year=$1
HARV=$2
PARS=$3

TEXTDIR=LORDS0_totals
OUTDIR=LORDSsaved
FILE=totalLORDS$year
WORD2VEC=$PARS/word2vec




# round 1 (1grams)
$WORD2VEC/word2phrase -debug 5 -min-count 1 -threshold 30 -train $PARS/$TEXTDIR/$FILE -output "$PARS/$OUTDIR/aaa"

#round 2 (up to 4 grams)
$WORD2VEC/word2phrase -debug 5 -train $PARS/$OUTDIR/aaa -output $PARS/$OUTDIR/bbb -min-count 1 -threshold 30

#round 3 (up to 8grams)
$WORD2VEC/word2phrase -debug 5 -train $PARS/$OUTDIR/bbb -output $PARS/$OUTDIR/ccc -min-count 1 -threshold 30

# generate vocabulary file
$WORD2VEC/word2vec -train $PARS/$OUTDIR/ccc -save-vocab $PARS/$OUTDIR/toimport/vocab -min-count 1

rm -f $PARS/$OUTDIR/aaa
rm -f $PARS/$OUTDIR/bbb
rm -f $PARS/$OUTDIR/ccc
