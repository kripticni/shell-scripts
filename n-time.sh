#!/usr/bin/env bash

NUM_EXECUTIONS=100000
PROGRAM="$HOME/Calculators/Sudoku/solver"

TEMP_FILE=$(mktemp)
START_TIME=$(date +%s.%N)

for ((i=1; i<=NUM_EXECUTIONS; i++))
do
  { time $PROGRAM > /dev/null; } 2>> $TEMP_FILE
done

END_TIME=$(date +%s.%N)

TOTAL_TIME=$(echo "$END_TIME - $START_TIME" | bc)
echo "Exec time for $NUM_EXECUTIONS: $TOTAL_TIME s"

TOTAL_SECONDS=$(awk '{ total += $1 } END { print total }' $TEMP_FILE)
AVERAGE_TIME=$(echo "$TOTAL_SECONDS / $NUM_EXECUTIONS" | bc -l)
echo "Average time: $AVERAGE_TIME s"

rm $TEMP_FILE
