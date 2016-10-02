#!/bin/bash
while read line
do
    echo "$line" | cut -c3
done < "${1:-/dev/stdin}"
