#!/bin/bash
cat /home/aleksic/.cache/fastc.save
source=$(cat /home/aleksic/.cache/fastc.save)
case "$1" in
	"build") gcc -o C $source && ./C ;;
	"config") echo $2 > /home/aleksic/.cache/fastc.save && source=$2 && gcc -o C $source && ./C ;;
	*) echo "build, or config sourcefile" ;;
esac
