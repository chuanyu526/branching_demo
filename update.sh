#!/bin/sh


cd /Users/water/tryBash
git fetch upstream
git merge upstream/master
git add .
git commit -m $1


