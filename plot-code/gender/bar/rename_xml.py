#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import re


tumor_type = sys.argv[1:]
pat = r'[a-z]+\.org_[a-z]+\.TCGA-[0-9A-Z]{2}-[0-9A-Z]{4}.xml'
for tt in tumor_type:
	path = '../../../TCGA-IC50/TCGA-{}/{}-all-clinical-files'.format(tt.upper(), tt)
	file_list = os.listdir(path)
	for f in file_list:
		if re.search(pat, f):
			file_path = os.path.join(path, f)
			portion = f.split('.')[2]
			new_name = portion + '.xml'
			new_name_path = os.path.join(path, new_name)
			os.rename(file_path, new_name_path)
			print("now we are handleding the {}-{0}".format(tt, new_name))