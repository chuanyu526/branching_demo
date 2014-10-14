#!/bin/sh


. ./config.sh
cd $filePath
branches=$(git branch)
while read -r line; do
    if [ "$1" == "$line" ]; then 
    	#echo true
    	exit
    fi
done <<< "$branches"
exit 1