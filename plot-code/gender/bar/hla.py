#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Purpose: collect HLA-[ABC] files into one path
# Starting: painting_code/gender/bar/
# Usage: python3 hla_set.py type1 type2 type3 etc.

import os
import sh
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
output_path = '../../../bar-plot/gender/hla'

for gen in gender:
	for tt in tumor_type:
		input_path = '../../../TCGA-IC50/TCGA-{}/{}-qualified'.format(tt.upper(), tt)
		input_file = '../../../bar-plot/gender/{}-{}-id.csv'.format(tt, gen)
		#output_path = '/adata/paint/TCGA-{}/hla-{}'.format(tt_upper,gen)
		hla_type = ['A','B','C']

		with open(input_file) as f: tcga_id = f.readlines()
		tcga_id = strip(tcga_id)

		for ht in hla_type:
			
			hla_arr = os.listdir('{}/{}.vcf.fa.pep/{}/'.format(input_path, tcga_id[0], ht))
			
			for ha in hla_arr:

				output_path_more = '{}/{}/{}-{}'.format(output_path, ha[len(ha)-14:len(ha)-4], tt, gen)
				sh.mkdir('-pv', output_path_more)

				for ti in tcga_id:
					with open('{}/{}.vcf.fa.pep/{}/{}'.format(input_path, ti, ht, ha)) as in_file, open('{}/{}.csv'.format(output_path_more, ti), 'a+') as out_file:
						lines = in_file.readlines()
						while '\n' in lines:
							lines.remove('\n')
						out_file.writelines(lines)




