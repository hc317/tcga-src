#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Purpose: choose the IC50 that smaller than 500nM
# Starting: src/ directory
# Usage: python3 ic50.py type1 type2 type3 etc.

import sh
import os
import sys
import function


tumor_list = sys.argv[1:]

for tumor in tumor_list:
    
    tumor_abbr = tumor[-4:].lower()
    folder_in = "../{}/{}-pre".format(tumor.upper(), tumor_abbr)
    folder_out = "../{}/{}-qualified".format(tumor.upper(), tumor_abbr)
    fir_folders = os.listdir(folder_in + '/')

    for fir_folder in fir_folders:
        abcs = os.listdir('{0}/{1}/'.format(folder_in, fir_folder))
        for abc in abcs:
            files = os.listdir('{0}/{1}/{2}/'.format(folder_in, fir_folder, abc))
            for file in files:            
                input_file = "{0}/{1}/{2}/{3}".format(folder_in, fir_folder, abc, file)

                sh.mkdir('-pv', '{0}/{1}/{2}/'.format(folder_out,fir_folder, abc))
                output_file = "{0}/{1}/{2}/qualified-".format(folder_out,fir_folder, abc) + file
                function.qualified_peptide(input_file, output_file)
