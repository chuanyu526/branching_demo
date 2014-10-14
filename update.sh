#!/bin/sh


. ./config.sh
cd $filePath
git add .
git commit -m $1


