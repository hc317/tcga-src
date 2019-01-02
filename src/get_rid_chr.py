#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Purpose: remove the 'chr' in the mutect.maf
# Starting: src/ directory
# Usage: python3 get_rid_chr.py type1 type2 type3 etc.

import re
import os
import sys


tumor_type = sys.argv[1:]
pat = 'chr'
for tt in tumor_type:
	tt = tt.upper()
	new = '../{}/new-mutect.maf'.format(tt)
	old = '../{}/mutect.maf'.format(tt)
	f = open(new, 'a+')
	with open(old) as g:
		lines = g.readlines()
		for line in lines:
			new_line = re.sub(pat, '', line)
			f.write(new_line)
	f.close()

	#del the old mutect.maf
	os.remove(old)
	#change the name of new file to the old's
	os.rename(new, old)
	print('{} finish!!!'.format(tt))
