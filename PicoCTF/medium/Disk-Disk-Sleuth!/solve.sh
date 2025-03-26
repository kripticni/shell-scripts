#!/usr/bin/env bash
gunzip dds1-alpine.flag.img.gz
srch_strings -a -n 8 dds1-alpine.flag.img | grep -i pico
