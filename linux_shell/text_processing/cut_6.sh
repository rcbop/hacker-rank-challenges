#!/bin/bash
while read line
do
    echo "$line" | cut -c13-
done < "${1:-/dev/stdin}"
