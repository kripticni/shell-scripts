#!/bin/bash
source=$(cat $HOME/.cache/fastc.save)
case "$1" in
	"build") gcc -Wall -o C $source && ./C ;;
	"config") echo $2 > $HOME/.cache/fastc.save && source=$2 && gcc -Wall -o C $source && ./C ;;
	"debug") gcc -Wall -g -o G $source && gdb G;; 
	*) echo "build, or config sourcefile" ;;
esac
