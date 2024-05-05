#!/bin/bash
path=$HOME/.cache/dict.sh.save
echo "$path,$@"
arg=$1

case "$arg" in
	"write") name=$2 && echo $@ | awk -v N=3 '{for (i=N; i<NF+1; i++) {print $i}}' | sed ':a;N;$!ba;s/\n/ /g' > $path/$name;;
	"read")  name=$2 && echo "$name:" && cat $path/$name | sed 's/\n/ /';;
	"append")name=$2 && echo $@ | awk -v N=3 '{for (i=N; i<NF+1; i++) {print $i}}' | sed ':a;N;$!ba;s/\n/ /g' >> $path/$name;;
	"edit")  name=$2 && xdg-open $path/$name;;
        "info")  name=$2 stat $path/$name;;
	"ls")    ls $path/*;; 

	*) echo "Usage: dict [OPTION] [FILENAME] [TEXT]
		A simple script for saving and reading notes about subjects.
		
		Options:
			write: FILENAME TEXT
			append: FILENAME TEXT
			read: FILENAME
			edit: FILENAME
			info: FILENAME
			ls: NULL" ;;
esac

