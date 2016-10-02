#!/bin/bash
while read line
do
    echo "$line" | cut -d' ' -f-3
done < "${1:-/dev/stdin}"
