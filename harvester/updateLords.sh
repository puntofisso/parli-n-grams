#!/bin/bash
PARLIGRAMDIR=$1
rsync -avz --progress data.theyworkforyou.com::parldata/scrapedxml/lordspages/daylord* $PARLIGRAMDIR/hansardLords/
