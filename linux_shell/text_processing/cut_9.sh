#!/bin/bash
while read line
do
    echo "$line" | cut -f2-
done < "${1:-/dev/stdin}"
