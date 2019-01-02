#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:53:24 2018

@author: frank-lsy
"""

import matplotlib.pyplot as plt
import pandas as pd
import csv
import re
import sys

tumor_type = sys.argv[1:]
gender = ['male', 'female']

for tt in tumor_type:
    for gen in gender:
        tum_gen = pd.read_csv('../../../bar-plot/gender/frequency-lines/{}-{}.csv'.format(tt, gen))

        name_list = tum_gen["HLA"]
        tum_gen_list = tum_gen["Avg_Amount"]

        tum_gen_csv = open("../../../bar-plot/gender/frequency-lines/{}-{}.csv".format(tt, gen))
        reader = csv.DictReader(tum_gen_csv)
        tum_gen_class_list = [row['HLA'] for row in reader]

        for i in range(len(tum_gen_class_list)):
            if (re.match("HLA-A[0-9][0-9]:[0-9][0-9]",tum_gen_class_list[i])):
                color = '#0000ff'
                plt.bar(name_list[i],tum_gen_list[i],label = tt.upper(),fc=color)
            elif (re.match("HLA-B[0-9][0-9]:[0-9][0-9]",tum_gen_class_list[i])):
                color = '#00ff00'
                plt.bar(name_list[i],tum_gen_list[i],label = tt.upper(),fc=color)
            elif (re.match("HLA-C[0-9][0-9]:[0-9][0-9]",tum_gen_class_list[i])):
                color = '#ffa500'
                plt.bar(name_list[i],tum_gen_list[i],label = tt.upper(),fc=color)        

        plt.ylabel("Number of Neoantigens Per Patient")
        plt.xticks=([])
        plt.gca().set_xticks([])
        plt.savefig("../../../bar-plot/gender/bar-{}-{}.png".format(tt, gen),dpi = 2560)
        plt.show()
