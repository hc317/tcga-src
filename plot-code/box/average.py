#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sh
import sys


def strip(arr):
    p = re.compile('\n')
    q = re.compile('\r')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
        arr[i]=re.sub(q,'',arr[i])
    return arr

def average(arr):
    tmp = 0
    for item in arr:
        tmp += item
    avg = tmp/len(arr)
    return avg

tumor_type = sys.argv[1:]
sh.mkdir('-pv', '../../box-plot/average-qualified-lines')
for tt in tumor_type:
    tumor = open('../../bar-plot/{}-new-id.csv'.format(tt))
    tcga_id_arr = tumor.readlines()
    tumor.close()
    new_tcga_id_arr = strip(tcga_id_arr)

    output_file = '../../box-plot/average-qualified-lines/{}.csv'.format(tt)

    avg_arr = []
    for tia in new_tcga_id_arr:
        input_file = '../../box-plot/qualified-lines/{}/{}.csv'.format(tt, tia)
        f = open(input_file)
        file = f.readlines()
        f.close()
        new_file = strip(file)
        new_file = list(map(float,new_file))
        avg = average(new_file)
        avg_arr.append(str(avg) + '\n')

    g = open(output_file, 'a+')
    g.writelines(avg_arr)
    g.close()