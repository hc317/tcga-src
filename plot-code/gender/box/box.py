#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 10:50:47 2018

@author: frank-lsy
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys


maybe = pd.read_csv("../../../box-plot/gender/maybe_gender.csv")
tumor_type = sys.argv[1:]
gender = ['male', 'female']
columns = []
for tt in tumor_type:
  for gen in gender:
    columns.append("{}-{}".format(tt, gen))

f = sns.boxplot(x="tumor_type",
                  y="number_per_patient",
                  hue="qualified",
                  data=maybe,
                  showmeans=True,
                  notch=False,
                  flierprops = {'marker':'o','markerfacecolor':'black','color':'darkred'},
                  meanprops = {'marker':'D','markerfacecolor':'darkgreen'},
                  medianprops = {'linestyle':'-','color':'darkred','linewidth':2},
                  whiskerprops = {'linestyle':'--','color':'green'})

plt.yscale('log')
plt.ylabel("Amount")
plt.xlabel("Type")
plt.savefig("/adata/paint/box-gender.png",dpi = 2560)
plt.show()

