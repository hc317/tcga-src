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
gender = ['male', 'female']

tt_gen_list = []
new_tt_gen_list = []
for tt in tumor_type:
    for gen in gender:
        tt_gen = open("../../../bar-plot/gender/{}-{}-id.csv".format(tt, gen))
        tt_gen_arr = tt_gen.readlines()
        tt_gen.close()
        new_tt_gen = strip(tt_gen_arr)
        tt_gen_list.append("{}-{}".format(tt, gen))
        new_tt_gen_list.append(new_tt_gen)

tumor_ids = dict(zip(tt_gen_list, new_tt_gen_list))

sh.mkdir('-pv', '../../../box-plot/gender/average-qualified-lines')
for tgl in tt_gen_list:
    output_file = '../../../box-plot/gender/average-qualified-lines/{}.csv'.format(tgl)
    avg_arr = []
    for ti in tumor_ids[tgl]:
        input_file = '../../../box-plot/gender/qualified-lines/{}/{}.csv'.format(tgl,ti)
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