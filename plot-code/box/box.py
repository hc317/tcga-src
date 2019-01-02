#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys


maybe = pd.read_csv("../../box-plot/maybe.csv")
columns = sys.argv[1:]
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
plt.savefig("../../box-plot/box.png",dpi = 2560)
plt.show()
