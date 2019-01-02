#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sh
import os
import sys
import re


def strip(arr):
    p = re.compile('\n')
    q = re.compile('\r')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
        arr[i]=re.sub(q,'',arr[i])
    return arr

tumor_type = sys.argv[1:]
gender = ['male', 'female']

for tt in tumor_type:
	for gen in gender:
		
		input_path = '../../../box-plot/gender/{}-{}-id.csv'.format(tt.upper(), tt, gen)
		output_file = '../../../box-plot/gender/{}-{}-patient.csv'.format(tt, gen)
		f = open(output_file, 'a+')
		tcga_id = open(input_path)
		tcga_id_arr = tcga_id.readlines()
		tcga_id_arr = strip(tcga_id_arr)
		tcga_id.close()
		for tia in tcga_id_arr:
			try:
				g = open('../../../TCGA-IC50/TCGA-{}/{}-pre/{}.vcf.fa.pep/A/HLA-A01:01.csv'.format(tt.upper(), tt, tia))
				lines = g.readlines()
				line_num = str(len(lines) - 1)
				g.close()
				f.write(line_num + '\n')
			except:
				pass

		f.close()

