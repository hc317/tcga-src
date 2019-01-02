#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
import sh
import csv

IC50_THRESHOLD = 500

def strip(arr):
    p = re.compile('\n')
    q = re.compile('\*')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
        arr[i]=re.sub(q,'',arr[i])
    
    return arr


def extract(input_file,source_arr,output_dir):
    sh.mkdir('-pv', output_dir)
    head = 'Hugo_Symbol	Entrez_Gene_Id	Center	NCBI_Build	Chromosome	Start_Position	End_Position	Strand	Variant_Classification	Variant_Type	Reference_Allele	Tumor_Seq_Allele1	Tumor_Seq_Allele2	dbSNP_RS	dbSNP_Val_Status	Tumor_Sample_Barcode	Matched_Norm_Sample_Barcode	Match_Norm_Seq_Allele1	Match_Norm_Seq_Allele2	Tumor_Validation_Allele1	Tumor_Validation_Allele2	Match_Norm_Validation_Allele1	Match_Norm_Validation_Allele2	Verification_Status	Validation_Status	Mutation_Status	Sequencing_Phase	Sequence_Source	Validation_Method	Score	BAM_File	Sequencer	Tumor_Sample_UUID	Matched_Norm_Sample_UUID	HGVSc	HGVSp	HGVSp_Short	Transcript_ID	Exon_Number	t_depth	t_ref_count	t_alt_count	n_depth	n_ref_count	n_alt_count	all_effects	Allele	Gene	Feature	Feature_type	One_Consequence	Consequence	cDNA_position	CDS_position	Protein_position	Amino_acids	Codons	Existing_variation	ALLELE_NUM	DISTANCE	TRANSCRIPT_STRAND	SYMBOL	SYMBOL_SOURCE	HGNC_ID	BIOTYPE	CANONICAL	CCDS	ENSP	SWISSPROT	TREMBL	UNIPARC	RefSeq	SIFT	PolyPhen	EXON	INTRON	DOMAINS	GMAF	AFR_MAF	AMR_MAF	ASN_MAF	EAS_MAF	EUR_MAF	SAS_MAF	AA_MAF	EA_MAF	CLIN_SIG	SOMATIC	PUBMED	MOTIF_NAME	MOTIF_POS	HIGH_INF_POS	MOTIF_SCORE_CHANGE	IMPACT	PICK	VARIANT_CLASS	TSL	HGVS_OFFSET	PHENO	MINIMISED	ExAC_AF	ExAC_AF_Adj	ExAC_AF_AFR	ExAC_AF_AMR	ExAC_AF_EAS	ExAC_AF_FIN	ExAC_AF_NFE	ExAC_AF_OTH	ExAC_AF_SAS	GENE_PHENO	FILTER	CONTEXT	src_vcf_id	tumor_bam_uuid	normal_bam_uuid	case_id	GDC_FILTER	COSMIC	MC3_Overlap	GDC_Validation_Status\n'
    for item in source_arr:
        f = open(input_file,'r')
        line_num = 0
        g = open(output_dir + item + '.maf', 'w')
        g.writelines(head)
        print("writing the " + item + " file.")
        while 1:
            line_num += 1
            line = f.readline()            
            match = item + '-[0-9][0-9][A-Z]-[0-9][0-9][A-Z]-[A-Z0-9]{4}-08'            
            t = re.findall(r'' + match,line)
            if (t):
                g.writelines(line)
            if not line:
                break
        f.close()
    g.close()


def qualified_peptide(input_file,output_file):
    qualified_rows = []
    try:     
        with open(input_file,'r') as fileIn:
            file = csv.DictReader(fileIn)
            for row in file:
                if (float(row['ic50'])<=IC50_THRESHOLD):
                    rows = [row['peptide'],row['ic50']]
                    qualified_rows.append(rows)
    except FileNotFoundError:
        print('NO SUCH FILE!{}'.format(input_file))
            #print(qualified_rows)
    with open (output_file,'w') as fileOut:
        file = csv.writer(fileOut)
        for item in qualified_rows:  
            file.writerow(item)


