#!/usr/bin/env bash
john --wordlist=rockyou.txt hash.challenge.txt --format=RAW-sha256
john hash.challenge.txt --show --format=RAW-sha256
#the solution is ariena
