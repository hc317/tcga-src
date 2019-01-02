#!/usr/bin/env python3

import sh
import os
import re
import sys


tumor_type = sys.argv[1:]

# tcga_id_num.py
tcga_id_num=[]
for tum in tumor_type:
	infile = "../../bar-plot/{}-new-id.csv".format(tum)
	with open(infile) as f:
		lines_num =len(f.readlines())
	tcga_id_num.append(lines_num)

#generate a dict whose key,value is tumor_type,tcga_id_num
den = dict(zip(tumor_type, tcga_id_num))

sh.mkdir('-pv', '../../bar-plot/lines/')

def strip(arr):
    p = re.compile('\r')
    q = re.compile('\n')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
        arr[i]=re.sub(q,'',arr[i])
    return arr

for tum in tumor_type:
	with open ('../../bar-plot/lines/{}.csv'.format(tum), 'a+') as new_file:
		new_file.write('Amount,HLA,Avg_Amount\n')
		hlas = os.listdir('../../bar-plot/trans/{}'.format(tum))
		hlas = strip(hlas)
		for hla in hlas:
			f = open('../../bar-plot/trans/{}/{}.csv'.format(tum, hla[:-4]))
			lines = f.readlines()		
			line_num = len(lines)
			con = str(line_num / den[tum])
			line_num = str(line_num)
			new_file.write('{},{},{}\n'.format(line_num, hla[:-4], con))
			f.close()

