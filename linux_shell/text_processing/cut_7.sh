#!/bin/bash
while read line
do
    echo "$line" | cut -d' ' -f4
done < "${1:-/dev/stdin}"
