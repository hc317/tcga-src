#!/bin/bash
# Sun Nov 25 2018

# path: plot-code/gender/bar/set-gender-bar-more.sh
# usage: ./set-gender-bar-more.sh type1(xxxx.lower()) type2 type3 type4


./bar.py "$@"
# output bar-plot/gender/bar-tumor_type-gender.png
echo "FINISH bar.py $@"

./hla_frequency.py "$@"
# output bar-plot/gender/tumor_type-gender-hla-frequency.png
echo "FINISH hla_frequency.py $@"

../../bar/joint.py "$@"
# output bar-plot/gender/tumor_type-gender.png
echo "FINISH joint.py $@"
echo "FINISH bar-plot-gender $@"
