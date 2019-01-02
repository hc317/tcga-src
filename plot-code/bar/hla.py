#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Purpose: collect HLA-[ABC] files into one directory
# Starting: painting_code/
# Usage: python3 hla_set.py type1(xxxx.lower()) type2 type3 etc.

import os
import sh
import sys


tumor_type = sys.argv[1:]

for tt in tumor_type:

	input_file = '../../TCGA-IC50/TCGA-{}/{}-qualified'.format(tt.upper(), tt)
	output_file = '../../bar-plot/hla'

	tcga_id = os.listdir(input_file)
	hla_part = ['A','B','C']

	for hp in hla_part:
		
		hla_class = os.listdir('{}/{}/{}/'.format(input_file, tcga_id[0], hp))
		
		for hc in hla_class:

			output_file_sec = '{}/{}/{}/'.format(output_file, hc[len(hc)-14:len(hc)-4], tt)
			sh.mkdir('-pv', output_file_sec)

			for ti in tcga_id:
				with open('{}/{}/{}/{}'.format(input_file, ti, hp, hc), 'r') as ifile, open('{}/{}.csv'.format(output_file_sec, ti[:12]), 'a+') as ofile:
					lines = ifile.readlines()
					while '\n' in lines:
						lines.remove('\n')
					ofile.writelines(lines)



