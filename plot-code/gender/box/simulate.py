#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import re
import sh
import sys
import pprint


def strip(arr):
    p = re.compile('\n')
    q = re.compile('\r')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
        arr[i]=re.sub(q,'',arr[i])
    return arr

def weighted_choice(weights):
	rnd = random.random() * sum(weights)
	for i, w in enumerate(weights):
		rnd -= w
		if rnd < 0: 
			return i

hla_a = open('../../../TCGA-IC50/dataset/HLA-A.csv')
hla_b = open('../../../TCGA-IC50/dataset/HLA-B.csv')
hla_c = open('../../../TCGA-IC50/dataset/HLA-C.csv')

hla_a_arr = hla_a.readlines()
hla_b_arr = hla_b.readlines()
hla_c_arr = hla_c.readlines()

hla_a.close()
hla_b.close()
hla_c.close()

hla_a_frequency = open('../../../TCGA-IC50/dataset/HLA-frequency/HLA-A-frequency.csv')
hla_b_frequency = open('../../../TCGA-IC50/dataset/HLA-frequency/HLA-B-frequency.csv')
hla_c_frequency = open('../../../TCGA-IC50/dataset/HLA-frequency/HLA-C-frequency.csv')

hla_a_arr_frequency = hla_a_frequency.readlines()
hla_b_arr_frequency = hla_b_frequency.readlines()
hla_c_arr_frequency = hla_c_frequency.readlines()

hla_a_frequency.close()
hla_b_frequency.close()
hla_c_frequency.close()

hla_a_arr_frequency = strip(hla_a_arr_frequency)
hla_b_arr_frequency = strip(hla_b_arr_frequency)
hla_c_arr_frequency = strip(hla_c_arr_frequency)

hla_a_arr_frequency = list(map(float, hla_a_arr_frequency))
hla_b_arr_frequency = list(map(float, hla_b_arr_frequency))
hla_c_arr_frequency = list(map(float, hla_c_arr_frequency))

hla_a_arr = strip(hla_a_arr)
hla_b_arr = strip(hla_b_arr)
hla_c_arr = strip(hla_c_arr)

tum = sys.argv[1]
gen = sys.argv[2]

tum_gen = open('../../../bar-plot/gender/{}-{}-id.csv'.format(tum, gen))
tum_gen_arr = tum_gen.readlines()
tum_gen.close()
new_tum_gen = strip(tum_gen_arr)

seq = []
for i in range(1000):
	seq.append(i)

rand_dict = dict.fromkeys(seq)
rand_hla = [''] * 6

for tg in new_tum_gen:
	for j in range(1000):
		rand_hla[0] = hla_a_arr[weighted_choice(hla_a_arr_frequency)]			
		rand_hla[1] = hla_a_arr[weighted_choice(hla_a_arr_frequency)]
		rand_hla[2] = hla_b_arr[weighted_choice(hla_b_arr_frequency)]
		rand_hla[3] = hla_b_arr[weighted_choice(hla_b_arr_frequency)]
		rand_hla[4] = hla_c_arr[weighted_choice(hla_c_arr_frequency)]
		rand_hla[5] = hla_c_arr[weighted_choice(hla_c_arr_frequency)]
		rand_dict[j] = rand_hla
		rand_hla = [''] * 6
	pprint.pprint(rand_dict) 

	for k in range(1000):
		for l in range(6):
			original_file = '../../../TCGA-IC50/TCGA-{}/{}-qualified/{}.vcf.fa.pep/{}/qualified-{}.csv'.format(tum.upper(), tum, tg, rand_dict[k][l][4], rand_dict[k][l])
			output_dir = '../../../box-plot/gender/mid/{}-{}/{}/{}'.format(tum, gen, tg, k+1)
			sh.mkdir('-pv', output_dir)
			output_file = '{}/{}.csv'.format(output_dir, rand_dict[k][l])
			sh.cp(original_file, output_file)
	print('finish!')