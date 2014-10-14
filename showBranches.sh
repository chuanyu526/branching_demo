#!/bin/sh


. ./config.sh
cd $filePath
branches=$(git branch)
while read -r line; do
    echo " $line "
done <<< "$branches"
