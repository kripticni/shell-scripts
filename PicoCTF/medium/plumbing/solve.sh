#!/usr/bin/env bash
timeout 10 nc jupiter.challenges.picoctf.org 7480 > output.txt; cat output.txt | grep -i pico
#could have solved it more elegantly but i wanted to keep the output and make
#it automatic
