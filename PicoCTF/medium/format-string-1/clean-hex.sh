#!/usr/bin/env bash
cat hex.txt | sed 's/,(nil)//g' | tr ',' ' ' > cleanhex.txt
