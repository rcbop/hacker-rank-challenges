#!/bin/bash
for i in {1..99}
do
    if [[ $((i%2)) -gt 0 ]]; then echo $i; fi
done
