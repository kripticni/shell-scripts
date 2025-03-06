#!/usr/bin/env bash
timeout 5 nc mercury.picoctf.net 35652 > ascii.txt
cat ascii.txt | sed 's/ //g' | xargs -n1 bash -c 'printf "\\$(printf "%03o" "$0")"'

#nice one for automation
