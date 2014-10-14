#!/bin/sh


cd /Users/water/tryBash
branches=$(git branch)
while read -r line; do
    echo " $line "
done <<< "$branches"
