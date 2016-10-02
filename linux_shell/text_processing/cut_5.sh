#!/bin/bash
while read line
do
    echo "$line" | cut -f-3
done < "${1:-/dev/stdin}"
