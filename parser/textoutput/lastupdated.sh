#!/bin/bash
lastupdate=`TZ=London date`
echo "DELETE FROM updatestring WHERE 1" | mysql 
echo "INSERT INTO updatestring (string) VALUES ('$lastupdate');" | mysql
