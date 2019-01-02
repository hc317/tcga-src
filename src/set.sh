#!/bin/bash

# Starting at src directory
# Usage: ./set.sh xxxx xxxx (eg ./set.sh luad lusc)

function 2vcf ()
{
#这里`为esc下面的按键符号
	for file in `ls $1`
	do
#这里的-d表示是一个directory，即目录/子文件夹
		if [ -d $1"/"$file ]
		then
#如果子文件夹则递归
			2vcf $1"/"$file
		else
#否则就能够读取该文件的地址
			#echo $1"/"$file
#读取该文件的文件名，basename是提取文件名的关键字
			echo `basename $file`
			perl maf2vcf.pl --input-maf $1`basename $file` --output-dir $2
		fi
	done
}
#函数定义结束，这里用来运行函数


function vep()
{
	echo $1
#这里`为esc下面的按键符号
	for file in `ls $1`
	do
#这里的-d表示是一个directory，即目录/子文件夹
		if [ -d $1"/"$file ]
		then
#如果子文件夹则递归
			vep $1"/"$file
		else
#否则就能够读取该文件的地址
			#echo $1"/"$file
#读取该文件的文件名，basename是提取文件名的关键字
			echo VEP-ing `basename $file`
			echo `date +%H:%M`
			/home/hc317/tcga/ensembl-vep/./vep -i $1`basename $file` \
			-o $2`basename $file` \
			--format vcf --vcf --symbol --terms SO --tsl \
			--hgvs --fasta ../dataset/Homo_sapiens.GRCh38.dna_sm.primary_assembly.fa \
			--cache --dir_cache /home/hc317/tcga/ensembl-vep/cache/ \
			--plugin Downstream --plugin Wildtype \
			--pick --no_stats --fork 2
		fi
	done
}


function filter ()
{
#这里`为esc下面的按键符号
	for file in `ls $1`
	do
#这里的-d表示是一个directory，即目录/子文件夹
		if [ -d $1"/"$file ]
		then
#如果子文件夹则递归
			filter $1"/"$file
		else
#否则就能够读取该文件的地址
			#echo $1"/"$file
#读取该文件的文件名，basename是提取文件名的关键字
			echo `basename $file`
			/home/hc317/tcga/ensembl-vep/./filter_vep \
			-i $1`basename $file` \
			-o $2`basename $file` \
			../ref/ensembl-vep/./filter_vep \
			-filter "Feature != ENST00000589042"
		fi
	done
}


function fasta ()
{
	echo $1
#这里`为esc下面的按键符号
	for file in `ls $1`
	do
#这里的-d表示是一个directory，即目录/子文件夹
		if [ -d $1"/"$file ]
		then
#如果子文件夹则递归
			fasta $1"/"$file
		else
#否则就能够读取该文件的地址
			#echo $1"/"$file
#读取该文件的文件名，basename是提取文件名的关键字
			echo "generate_protein_fasta " `basename $file`
			pvacseq generate_protein_fasta \
			$1`basename $file` 9 $2`basename $file`.fa
		fi
	done
}


function pep()
{
	echo $1
#这里`为esc下面的按键符号
	for file in `ls $1`
	do
#这里的-d表示是一个directory，即目录/子文件夹
		if [ -d $1"/"$file ]
		then
#如果子文件夹则递归
			pep $1"/"$file
		else
#否则就能够读取该文件的地址
			#echo $1"/"$file
#读取该文件的文件名，basename是提取文件名的关键字
			echo PEP-ing `basename $file`
			awk 'NR%2==0' $1`basename $file` >>  $2`basename $file`.pep
		fi
	done
}


function pre ()
{
#这里`为esc下面的按键符号
	for file in `ls $1`
	do
#这里的-d表示是一个directory，即目录/子文件夹
		if [ -d $1"/"$file ]
		then
#如果子文件夹则递归
			pre $1"/"$file
		else
#否则就能够读取该文件的地址
			#echo $1"/"$file
#读取该文件的文件名，basename是提取文件名的关键字
			#echo `basename $file`
			cd ../TCGA-${5^^}/
			mkdir -pv ../TCGA-${5^^}/$3/`basename $file`/$4
			for line in `cat $2`
			do
				echo $line
				python3 /home/hc317/tcga/mhcnuggets-2.0/mhcnuggets/src/predict.py \
				-c I \
				-p $1`basename $file` \
				-a $line \
				-o "../TCGA-${5^^}/$3/`basename $file`/$4/$line.csv"
			done
		fi
	done
}


for tumor in $@
do
	mkdir ../TCGA-${tumor^^}
	cd ../TCGA-${tumor^^}
	
	# gdc_scan.py
	echo "gdc_scan.py mutect"
	python ../src/gdc_scan.py files download \
	                          --format MAF \
	                          --project TCGA-${tumor^^}

	gzip -d *mutect*

	if [ $? == 0 ]
	then
		rm -rf *gz
		mv `ls` mutect.maf
		sed -i '1,5d' mutect.maf
		python3 ../src/get_rid_chr.py TCGA-${tumor^^}

		mkdir ${tumor}-all-clinical-files
		cd ${tumor}-all-clinical-files
		
		# gdc_scan.py again
		echo "gdc_scan.py clinical data"
		python3 ../../src/gdc_scan.py files download \
		                              --project TCGA-${tumor^^} \
		                              --type "Clinical Supplement"

		cd ../../src
		# get_id.py
		echo "get_id.py"
		python3 get_id.py TCGA-${tumor^^}

		# extract.py
		echo "extract.py"
		python3 extract.py TCGA-${tumor^^}

		# 2vcf.sh
		echo "2vcf.sh"
		folder="../TCGA-${tumor^^}/${tumor}-maf/"
		mkdir ../TCGA-${tumor^^}/${tumor}-vcf/
		output="../TCGA-${tumor^^}/${tumor}-vcf/"
		2vcf $folder $output

		rm -f ../TCGA-${tumor^^}/${tumor}-vcf/*pairs.tsv

		# vep.sh
		echo vep.sh
		folder="../TCGA-${tumor^^}/${tumor}-vcf/"
		mkdir ../TCGA-${tumor^^}/${tumor}-vep-vcf/
		output="../TCGA-${tumor^^}/${tumor}-vep-vcf/"
		vep $folder $output

		# cut.py
		echo "cut.py"
		python3 cut.py TCGA-${tumor^^}

		# filter.sh
		echo "filter.sh"
		folder="../TCGA-${tumor^^}/${tumor}-cut/"
		mkdir ../TCGA-${tumor^^}/${tumor}-filter/
		output="../TCGA-${tumor^^}/${tumor}-filter/"
		filter $folder $output

		# fasta.sh
		echo "fasta.sh"
		folder="../TCGA-${tumor^^}/${tumor}-filter/"
		mkdir ../TCGA-${tumor^^}/${tumor}-fasta/
		output="../TCGA-${tumor^^}/${tumor}-fasta/"
		fasta $folder $output

		# pep.sh
		echo "pep.sh"
		folder="../TCGA-${tumor^^}/${tumor}-fasta/"
		mkdir ../TCGA-${tumor^^}/${tumor}-pep/
		output="../TCGA-${tumor^^}/${tumor}-pep/"
		pep  $folder $output

		# pre.sh
		echo "pre.sh"
		folder="../TCGA-${tumor^^}/${tumor}-pep/"
		hla="../dataset/HLA-A.csv"
		stad="${tumor}-pre"
		type="A"
		pre $folder $hla $stad $type $tumor
		folder="../TCGA-${tumor^^}/${tumor}-pep/"
		hla="../dataset/HLA-B.csv"
		stad="${tumor}-pre"
		type="B" 
		pre $folder $hla $stad $type $tumor
		folder="../TCGA-${tumor^^}/${tumor}-pep/"
		hla="../dataset/HLA-C.csv" 
		stad="${tumor}-pre"
		type="C"
		pre $folder $hla $stad $type $tumor

		# get_real_pep.py
		echo "get_real_pep.py"
		python3 get_real_pep.py TCGA-${tumor^^}

		rm -rf ../TCGA-${tumor^^}/${tumor}-pre
		mv ../TCGA-${tumor^^}/${tumor}-real-pep ../TCGA-${tumor^^}/${tumor}-pre

		# ic50.py
		echo "ic50.py"
		python3 ic50.py TCGA-${tumor^^}

		echo "FINISH ${tumor}"

	else
		echo "--The ${tumor}-gzip archive downloaded has some problems--"
		echo "--Please try to run $tumor later AGAIN--"
		rm -rf *
	fi
done