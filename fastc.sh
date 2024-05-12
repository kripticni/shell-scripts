#!/usr/bin/env bash

source=$(cat $HOME/.cache/fastc.save | awk -F '\t' '$1 == $(pwd) {print $2}')
arg=$1

case "$arg" in
	"compile") gcc -Wall -o C $source && ./C ;;
	"debug") gcc -Wall -g -o G $source && gdb G;;
	"config") sed -i '/$(pwd)/d' $HOME/.cache/fastc.save
		printf "%s\t%s" $(pwd) $2 > $HOME/.cache/fastc.save
		gcc -Wall -o C $2 && ./C;;
	*) echo "Usage: fastc.sh [OPTION] [SOURCEFILE]
                A simple script for faster C script management.

                Options:
                        compile: NULL
                        debug: NULL
                        config: SOURCEFILE
                        ";;
esac
