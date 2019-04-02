#!/bin/bash
for file in "$@"
do
echo $file
python check_grades.py $file
echo ""
done
