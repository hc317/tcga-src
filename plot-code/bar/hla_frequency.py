#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import csv
import re
import sys

def draw(input_csv,output_png):
    
    hla = pd.read_csv(input_csv)

    tmp = open(input_csv,'r')
    reader = csv.DictReader(tmp)
    class_list = [row['HLA'] for row in reader]
    name_list = hla["HLA"]
    hla_list = hla["Frequency"]
    for i in range(len(class_list)):
        if (re.match("HLA-A[0-9][0-9]:[0-9][0-9]",class_list[i])):
            color = '#0000ff'        
            plt.bar(name_list[i],hla_list[i], fc = color)
        elif (re.match("HLA-B[0-9][0-9]:[0-9][0-9]",class_list[i])):
            color = '#00ff00'        
            plt.bar(name_list[i],hla_list[i], fc = color)
        elif (re.match("HLA-C[0-9][0-9]:[0-9][0-9]",class_list[i])):
            color = '#ffa500'        
            plt.bar(name_list[i],hla_list[i], fc = color)
    plt.gca().invert_yaxis()
    plt.ylabel("Allele Frequency")
    plt.xlabel("Allele")
    plt.xticks=([])
    plt.gca().set_xticks([])
    plt.savefig(output_png,dpi = 2560)
    plt.show()

tumor_type = sys.argv[1:]

for tt in tumor_type:
    draw("../../bar-plot/frequency-lines/{}.csv".format(tt), \
         "../../bar-plot/{}-hla-frequency.png".format(tt))