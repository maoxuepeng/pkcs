#!/bin/sh

# trigger docker build
i=0
while [ 1 ];
do
  echo "$1	num[$i]	`date -u`"
  i=$((i+1)) 
  sleep 1
done
