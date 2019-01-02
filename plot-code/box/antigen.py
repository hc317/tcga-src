#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sh
import os
import sys

tumor_type = sys.argv[1:]
for tt in tumor_type:

	input_path = '../../TCGA-IC50/TCGA-{}/{}-pre'.format(tt.upper(), tt)
	output_file = '../../box-plot/{}-patient.csv'.format(tt)
	f = open(output_file, 'a+')
	tcga_id = os.listdir(input_path)
	for ti in tcga_id:
		try:
			g = open('{}/{}/A/HLA-A01:01.csv'.format(input_path, ti))
			lines = g.readlines()
			line_num = str(len(lines) - 1)
			f.write(line_num + '\n')
		except:
			pass
	f.close()

