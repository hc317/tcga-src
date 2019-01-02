#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Purpose: obtain id from clinical-flies for each types
# Starting: src/ directory
# Usage: python3 get_id.py type1 type2 typ3 etc.


import os
import sys


tumor_list = sys.argv[1:]

for tumor in tumor_list:
	tumor_abbr = tumor[-4:].lower()
	files = os.listdir('../{}/{}-all-clinical-files/'.format(tumor.upper(), tumor_abbr))
	f = open('../{}/{}-id.csv'.format(tumor.upper(), tumor_abbr), 'a+')

	for file in files:
		if file[-3:] == 'xml':
			#print(file[len(file)-16:len(file)-4])
			f.write(file[len(file)-16:len(file)-4] + '\n')

	f.close()
