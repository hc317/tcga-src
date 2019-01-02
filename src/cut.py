#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 11:23:15 2018

@author: frank-lsy
"""

# Purpose: remove the normal sequence
# Starting: src/ directory
# Usage: python3 cut.py type1 type2 type3 etc.

import sh
import os
import sys


tumor_list = sys.argv[1:]

for tumor in tumor_list:
	
	tumor_abbr = tumor[-4:].lower()
	input_dir = "../{}/{}-vep-vcf/".format(tumor.upper(), tumor_abbr)
	output_dir = "../{}/{}-cut/".format(tumor.upper(), tumor_abbr)
	sh.mkdir('-pv', output_dir)

	files = os.listdir(input_dir)
	for file in files:
		with open(input_dir + file,'r') as reader, open(output_dir + file, 'w') as writer:
			for line in reader:
				items = line.strip().split()
				print(' '.join(items[:10]), file=writer)
