#!/bin/bash

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
	$1`basename $file` 9 ../TCGA-LUSC/lusc-fasta/`basename $file`.fa
   fi
  done
}
#函数定义结束，这里用来运行函数
folder="../TCGA-LUSC/lusc-filter/"
fasta $folder