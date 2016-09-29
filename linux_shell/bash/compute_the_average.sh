#!/bin/bash
read size
sum=0
for ((c=0;c<size;c++))
do
    read y
    sum=$((sum+y))
done
result=$(echo "$sum/$size" | bc -l);
printf "%.3f" $result
