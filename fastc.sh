#!/usr/bin/env bash

source=$(cat $HOME/.cache/fastc.save | awk -F '\t' -v dir=$(pwd) '$1 == dir {print $2}')
save=$2
if [ -z "$source" ] && [ "$1" != "config" ]; then
  save=$(ls | xargs | fzf)
  arg="config"
else
  arg=$1
fi

case "$arg" in
	"compile") gcc -Wall -o C $source && ./C ;;
	"debug") gcc -Wall -g -o G $source && gdb G;;
	"config") sed -i "/$(pwd)/d" $HOME/.cache/fastc.save
		printf "%s\t%s\n" "$(pwd)" "$save" >> $HOME/.cache/fastc.save
		gcc -Wall -o C $save && ./C;;
	*) echo "Usage: fastc.sh [OPTION] [SOURCEFILE]
                A simple script for faster C script management.

                Options:
                        compile: NULL
                        debug: NULL
                        config: SOURCEFILE
                        ";;
esac
