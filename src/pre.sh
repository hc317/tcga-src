#!/bin/bash

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
  	cd ../TCGA-LUSC/
  	mkdir -pv ../TCGA-LUSC/$3/`basename $file`/$4
  	for line in `cat $2`
  	do
  		echo $line
  		python3 /home/hc317/tcga/mhcnuggets-2.0/mhcnuggets/src/predict.py \
  		-c I \
  		-p $1`basename $file` \
  		-a $line \
  		-o "../TCGA-LUSC/$3/`basename $file`/$4/$line.csv"
  	done
   fi
  done
}


folder="../TCGA-LUSC/lusc-pep/"
hla="../dataset/HLA-A.csv"
stad="lusc-pre"
type="A"
pre $folder $hla $stad $type
folder="../TCGA-LUSC/lusc-pep/"
hla="../dataset/HLA-B.csv"
stad="lusc-pre"
type="B" 
pre $folder $hla $stad $type
folder="../TCGA-LUSC/lusc-pep/"
hla="../dataset/HLA-C.csv" 
stad="lusc-pre"
type="C"
pre $folder $hla $stad $type