#!/usr/bin/env bash
cat hex.txt | tr ' ' '\n' | sed 's/^0//' |  xargs -I {} printf "\{}"
#easiest medium by far, easier than many easy ctfs too 
