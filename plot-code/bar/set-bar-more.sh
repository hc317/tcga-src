#!/bin/bash
# Fri Nov 23 2018

# path: plot-code/bar/set-bar-more.sh
# usage: ./set-bar-more.sh type1(xxxx.lower()) type2 type3 type4


./bar.py "$@"
# output bar-plot/bar-tumor_type.png
echo "FINISH bar.py $@"

./hla_frequency.py "$@"
# output bar-plot/tumor_type-hla-frequency.png
echo "FINISH hla_frequency.py $@"

./joint.py "$@"
#output bar-plot/tumor_type-(gender).png
echo "FINISH joint.py $@"
echo "FINISH bar-plot $@"
