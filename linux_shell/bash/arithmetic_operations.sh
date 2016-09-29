#!/bin/bash
read input
printf "%.3f" `echo $input | bc -l`
