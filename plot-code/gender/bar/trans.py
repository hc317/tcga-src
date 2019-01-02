#!/usr/bin/env python3

import sh
import os
import sys


tumor_type = sys.argv[1:]
gender = ['male', 'female']

for gen in gender:
	for tt in tumor_type:
		hlas = os.listdir('../../../bar-plot/gender/hla-union/')
		sh.mkdir('-pv', '../../../bar-plot/gender/trans/{}-{}/'.format(tt, gen))
		#print('Making direction {}...'.format(tumor_abbr))
			
		for hla in hlas:
			sh.cp('../../../bar-plot/gender/hla-union/{}/{}-{}.csv'.format(hla, tt, gen), \
				  '../../../bar-plot/gender/trans/{}-{}/{}.csv'.format(tt, gen, hla))