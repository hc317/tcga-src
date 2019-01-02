#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import sys
import sh



def strip(arr):
    p = re.compile('\n')
    q = re.compile('\r')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
        arr[i]=re.sub(q,'',arr[i])
    return arr

tumor_type = sys.argv[1:]
pat = 'FEMALE'
sh.mkdir('-pv', '../../../bar-plot/gender/')

for tt in tumor_type:
	input_path = '../../../TCGA-IC50/TCGA-{}/{}-all-clinical-files'.format(tt.upper(), tt)
	input_file = '../../../bar-plot/{}-new-id.csv'.format(tt)

	male = open('../../../bar-plot/gender/{}-male-id.csv'.format(tt), 'a+')
	female = open('../../../bar-plot/gender/{}-female-id.csv'.format(tt), 'a+')

	f = open(input_file)
	id_arr = f.readlines()
	id_arr = strip(id_arr)
	f.close()
	for ia in id_arr:

		g = open('{}/{}.xml'.format(input_path, ia))
		lines = g.readlines()
		g.close()
		string = ''.join(lines)
		if re.search(pat, string):
			female.write(ia + '\n')
		else:
			male.write(ia + '\n')

	male.close()
	female.close()
