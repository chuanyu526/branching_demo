#!/bin/sh

. ./config.sh
cd filePath
branches=$(git branch)
star="* master"
while read -r line; do
    if [ "$star" == "$line" ]; then 
    	exit
    fi
done <<< "$branches"
exit 1