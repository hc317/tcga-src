#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import sys
import sh
import re

def strip(arr):
    p = re.compile('\r')
    q = re.compile('\n')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
        arr[i]=re.sub(q,'',arr[i])
    return arr

tumor_type = sys.argv[1:]
gender = ['male', 'female']

input_path = '../../../bar-plot/gender/lines'
output_path = '../../../bar-plot/gender/frequency-lines'
sh.mkdir('-pv', output_path)

for tt in tumor_type:
	for gen in gender:

		input_file = pd.read_csv('{}/{}-{}.csv'.format(input_path, tt, gen))
		hla_input = list(input_file['HLA'])
		amount = list(input_file['Amount'])
		avg_amount = list(input_file['Avg_Amount'])

		find_file = pd.read_csv('../../../TCGA-IC50/dataset/HLA-frequency/HLA-all.csv')
		find_hla = list(find_file['Type'])
		find_frequency = list(find_file['Frequency'])

		g = open('{}/{}-{}.csv'.format(output_path, tt, gen), 'a+')
		g.write('Amount,HLA,Avg_Amount,Frequency\n')

		for HLA in hla_input:
			index_f = find_hla.index(HLA)
			Frequency = find_frequency[index_f]

			index_i = hla_input.index(HLA)
			Amount = amount[index_i]
			Avg_Amount = avg_amount[index_i]
			
			g.write('{},{},{},{}\n'.format(Amount, HLA, Avg_Amount, Frequency))
		g.close()
