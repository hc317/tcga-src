#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys


def strip(arr):
    p = re.compile('\n')
    q = re.compile('\r')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
        arr[i]=re.sub(q,'',arr[i])
    return arr

tumor_type = sys.argv[1:]

input_path1 = '../../box-plot'
input_path2 = '../../box-plot/average-qualified-lines'

output_file = '../../box-plot/maybe.csv'
f = open(output_file, 'a+')
f.write('number_per_patient,tumor_type,qualified,type\n')

for tt in tumor_type:
    tumor_all = open('{}/{}-patient.csv'.format(input_path1, tt))
    tumor_new = open('{}/{}.csv'.format(input_path2, tt))

    tumor_num1 = tumor_all.readlines()
    tumor_num2 = tumor_new.readlines()

    tumor_all.close()
    tumor_new.close()

    tumor_num1 = strip(tumor_num1)
    tumor_num2 = strip(tumor_num2)

    for tn in tumor_num1:
        f.write('{},{},NO,antigen\n'.format(tn, tt.upper()))
    for tn in tumor_num2:
        f.write('{},{},YES,neoantigen\n'.format(tn, tt.upper()))

f.close()