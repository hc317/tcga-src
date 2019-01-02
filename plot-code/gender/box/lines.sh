#!/bin/bash

function count_lines ()
{
#这里`为esc下面的按键符号
  for file in `ls $1`
  do
#这里的-d表示是一个directory，即目录/子文件夹
    if [ -d $1"/"$file ]
    then
#如果子文件夹则递归
      count_lines $1"/"$file $out
    else
#否则就能够读取该文件的地址
      #echo $1"/"$file
#读取该文件的文件名，basename是提取文件名的关键字
  	echo `basename $file`
    echo $1
    echo $2
    cat $1"/"`basename $file`|wc -l>>$2
    fi
  done
}

#luad_male_folder="/adata/paint/extract/luad-male/"
#lusc_male_folder="/adata/paint/extract/lusc-male/"
#luad_female_folder="/adata/paint/extract/luad-female/"
lusc_female_folder="/adata/paint/extract/lusc-female/"

#luad_male_out_folder="/adata/paint/qualified_lines/luad-male/"
#lusc_male_out_folder="/adata/paint/qualified_lines/lusc-male/"
#luad_female_out_folder="/adata/paint/qualified_lines/luad-female/"
lusc_female_out_folder="/adata/paint/qualified_lines/lusc-female/"

#for tumor_id in `ls $luad_male_folder`
#do
#	dest_dir="${luad_male_folder}${tumor_id}"
#	mkdir -pv ${luad_male_out_folder}
#	luad_out="${luad_male_out_folder}${tumor_id}.csv"
#	count_lines $dest_dir $luad_out
#done

#for tumor_id in `ls $lusc_male_folder`
#do
#	dest_dir="${lusc_male_folder}${tumor_id}"
#	mkdir -pv ${lusc_male_out_folder}
#	lusc_out="${lusc_male_out_folder}${tumor_id}.csv"
#	count_lines $dest_dir $lusc_out
#done

#for tumor_id in `ls $luad_female_folder`
#do
#  dest_dir="${luad_female_folder}${tumor_id}"
#  mkdir -pv ${luad_female_out_folder}
#  luad_out="${luad_female_out_folder}${tumor_id}.csv"
#  count_lines $dest_dir $luad_out
#done

for tumor_id in `ls $lusc_female_folder`
do
  dest_dir="${lusc_female_folder}${tumor_id}"
  mkdir -pv ${lusc_female_out_folder}
  lusc_out="${lusc_female_out_folder}${tumor_id}.csv"
  count_lines $dest_dir $lusc_out
done