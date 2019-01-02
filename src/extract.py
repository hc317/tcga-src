#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Purpose: extract ID from mutect.maf according to type
# Starting: src/ directory
# Usage: python3 extract.py type1 type2 type3 etc.

import sys
import function


tumor_list = sys.argv[1:]

for tumor in tumor_list:
	tumor_abbr = tumor[-4:].lower()
	with open('../{}/{}-id.csv'.format(tumor.upper(), tumor_abbr), 'r') as f:
		lines = f.readlines()
		mod_lines = function.strip(lines)

	input_file = '../{}/mutect.maf'.format(tumor.upper())
	output_file = '../{}/{}-maf/'.format(tumor.upper(), tumor_abbr)
	function.extract(input_file, mod_lines, output_file)