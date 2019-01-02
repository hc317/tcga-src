#!/usr/bin/env python3

import sh
import os
import re
import sys


def strip(arr):
    p = re.compile('\r')
    q = re.compile('\n')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
        arr[i]=re.sub(q,'',arr[i])
    return arr

tumor_type = sys.argv[1:]
gender = ['male', 'female']

# tcga_id_num.py
tcga_id_num = []
tumor_type_gender = []
for gen in gender:
	for tum in tumor_type:
		infile = "../../../bar-plot/gender/{}-{}-id.csv".format(tum, gen)
		with open(infile) as f:
			lines_num =len(f.readlines())
		tcga_id_num.append(lines_num)
		tumor_type_gender.append("{}-{}".format(tum, gen))

#generate a dict whose key,value is tumor_type,tcga_id_num
den = dict(zip(tumor_type_gender, tcga_id_num))

input_path = '../../../bar-plot/gender/trans'
output_path = '../../../bar-plot/gender/lines'
sh.mkdir('-pv', output_path)

for tt in tumor_type:
	for gen in gender:
		with open ('{}/{}-{}.csv'.format(output_path, tt, gen), 'a+') as new_file:
			new_file.write('Amount,HLA,Avg_Amount\n')
			hlas = os.listdir('{}/{}-{}'.format(input_path, tt, gen))
			hlas = strip(hlas)
			for hla in hlas:
				f = open('{}/{}-{}/{}.csv'.format(input_path, tt, gen, hla[:-4]))
				#  get lines number
				lines = f.readlines()
				line_num = len(lines)
				con = str(line_num / den['{}-{}'.format(tt, gen)])
				line_num = str(line_num)
				#  write into new file
				new_file.write('{},{},{}\n'.format(line_num, hla[:-4], con))
				f.close()