#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Fri Nov 23 2018

# PURPOSE: print the number of tcga_id for the script of hla-union.sh
# STARTINH: plot-code/bar/tcga_id_num.py
# USAGE: ./tcga_id_num.py type (just count one by one)


import sys

tumor_gender = sys.argv[1]
infile = "../../../bar-plot/gender/{}-id.csv".format(tumor_gender)
with open(infile) as f:
	lines_num =len(f.readlines())
print(lines_num)
 
