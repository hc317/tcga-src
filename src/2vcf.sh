#!/bin/bash

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
    perl maf2vcf.pl --input-maf $1`basename $file` --output-dir ../TCGA-LUSC/lusc-vcf/
   fi
  done
}
#函数定义结束，这里用来运行函数

folder="../TCGA-LUSC/lusc-maf/"
mkdir ../TCGA-LUSC/lusc-vcf/
2vcf $folder