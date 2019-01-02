#!/usr/bin/env python3

import sh
import os
import sys


tumor_type = sys.argv[1:]
hlas = os.listdir('../../bar-plot/hla-union/')

for tt in tumor_type:

	sh.mkdir('-pv', '../../bar-plot/trans/{}/'.format(tt))
	print('Making direction {}'.format(tt))
		
	for hla in hlas:
		sh.cp('../../bar-plot/hla-union/{}/{}.csv'.format(hla, tt), '../../bar-plot/trans/{}/{}.csv'.format(tt, hla))
				