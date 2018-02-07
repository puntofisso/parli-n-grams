#!/bin/bash
linode-linode -a start --label api
ssh webuser@api.ptfs.uk '/var/www/html/parli-n-grams/parser/textoutput/processcurrentyear.sh 2018'
