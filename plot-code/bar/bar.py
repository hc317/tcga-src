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

for tt in tumor_type:
    tumor = pd.read_csv("../../bar-plot/frequency-lines/{}.csv".format(tt))

    name_list = tumor["HLA"]
    num_list = tumor["Avg_Amount"]

    tumor_csv = open("../../bar-plot/frequency-lines/{}.csv".format(tt))
    reader = csv.DictReader(tumor_csv)
    class_list = [row['HLA'] for row in reader]

    for i in range(len(class_list)):
        if (re.match("HLA-A[0-9][0-9]:[0-9][0-9]",class_list[i])):
            color = '#0000ff'
            plt.bar(name_list[i],num_list[i],label = tt.upper(),fc=color)
        elif (re.match("HLA-B[0-9][0-9]:[0-9][0-9]",class_list[i])):
            color = '#00ff00'
            plt.bar(name_list[i],num_list[i],label = tt.upper(),fc=color)
        elif (re.match("HLA-C[0-9][0-9]:[0-9][0-9]",class_list[i])):
            color = '#ffa500'
            plt.bar(name_list[i],num_list[i],label = tt.upper(),fc=color)        

    plt.ylabel("Number of Neoantigens Per Patient")
    plt.xticks=([])
    plt.gca().set_xticks([])
    plt.savefig("../../bar-plot/bar-{}.png".format(tt),dpi = 2560)
    plt.show()
