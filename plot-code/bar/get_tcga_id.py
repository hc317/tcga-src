#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Purpose: wirte patients' ID to the type.csv file
# Starting: plot_code/bar
# Usage: python3 get_tcga_id.py type1(xxxx.lower()) type2 type3 etc.

import os
import sys
import sh

tumor_type = sys.argv[1:]

for tt in tumor_type:

	input_path = '../../TCGA-IC50/TCGA-{}/{}-qualified/'.format(tt.upper(), tt)

	output_path = '../../bar-plot'
	output_file = '{}/{}-new-id.csv'.format(output_path, tt)
	sh.mkdir('-pv', output_path)

	tcga_id = os.listdir(input_path)
	with open(output_file, 'a+') as new_file:
		for ti in tcga_id:
			print(ti[:12], file=new_file)