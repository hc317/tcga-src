#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Purpose: remove the 'Z' in the peptides
# Starting: src/ directory
# Usage: python3 get_real_pep.py type1 type2 type3 etc.

import re
import os
import sh
import sys

tumor_list = sys.argv[1:]

for tumor in tumor_list:
	
	tumor_abbr = tumor[-4:].lower()
	folder_in = "../{}/{}-pre".format(tumor.upper(), tumor_abbr)
	folder_out = "../{}/{}-real-pep".format(tumor.upper(), tumor_abbr)

	fir_folders = os.listdir(folder_in)

	for fir_folder in fir_folders:
		abcs = os.listdir('{0}/{1}/'.format(folder_in, fir_folder))
		for abc in abcs:
			files = os.listdir('{0}/{1}/{2}/'.format(folder_in, fir_folder, abc))
			for file in files:
				f = open("{0}/{1}/{2}/{3}".format(folder_in, fir_folder, abc, file), 'r')
				sh.mkdir('-pv', '{0}/{1}/{2}/'.format(folder_out,fir_folder, abc))
				g = open("{0}/{1}/{2}/{3}".format(folder_out,fir_folder, abc, file),'a+')
				lines = f.readlines()
				f.close()
				for line in lines:				
					new_line = re.sub('Z+', '', line)				
					g.write(new_line)
				g.close()