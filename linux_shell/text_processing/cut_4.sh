#!/bin/bash
while read line
do
    echo "$line" | cut -c1-4
done < "${1:-/dev/stdin}"
