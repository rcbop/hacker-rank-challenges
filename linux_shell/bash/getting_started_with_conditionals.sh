#!/bin/bash
read input
if [[ "$input" == "Y" || "$input" == "y" ]]; then
    echo "YES"
elif [[ "$input" == "N" || "$input" == "n" ]]; then
    echo "NO"
else
    echo "ERROR"
fi
