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

#luad_folder="../../box-plot/extract/luad/"
lusc_folder="../../box-plot/extract/lusc/"


#luad_out_folder="../../box-plot/qualified-lines/luad/"
lusc_out_folder="../../box-plot/qualified-lines/lusc/"


#for tumor_id in `ls $luad_folder`
#do
#	dest_dir="${luad_folder}${tumor_id}"
#	mkdir -pv ${luad_out_folder}
#	luad_out="${luad_out_folder}${tumor_id}.csv"
#	count_lines $dest_dir $luad_out
#done

for tumor_id in `ls $lusc_folder`
do
	dest_dir="${lusc_folder}${tumor_id}"
	mkdir -pv ${lusc_out_folder}
	lusc_out="${lusc_out_folder}${tumor_id}.csv"
	count_lines $dest_dir $lusc_out
done

