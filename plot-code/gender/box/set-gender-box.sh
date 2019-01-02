#!/bin/bash
# Sun Nov 25 2018

# path: plot-code/gender/box/set-gender-box.sh
# usage: ./set-gender-box.sh type1(xxxx.lower()) type2 type3 type4


function union ()
{
  file_array=()
  let i=0
#这里`为esc下面的按键符号
  for file in `ls $1`
  do
#这里的-d表示是一个directory，即目录/子文件夹
#否则就能够读取该文件的地址
    #echo $1"/"$file
#读取该文件的文件名，basename是提取文件名的关键字
    #echo `basename $file`
    file_array[i]=`basename $file`
    let i=$i+1
  done
  #echo ${file_array[3]}

  for i in {0..4}
  do
    #echo ${file_array[i]}
    if [ $i -eq 0 ]
    then
      #echo ${file_array[i]}
      #echo ${file_array[`expr $i + 1`]}
      cat $1"/"${file_array[i]} $1"/"${file_array[`expr $i + 1`]}|sort|uniq > $1"/tmp-"`expr $i + 1`.csv
    else
      #echo $1"/tmp-"$i
      #echo $1"/"${file_array[i+1]}
      cat $1"/tmp-"$i.csv $1"/"${file_array[i+1]}|sort|uniq > $1"/tmp-"`expr $i + 1`.csv
    fi
  done
  
  for j in {1..4}
  do
    rm $1"/tmp-"$j.csv
  done
  mv $1"/tmp-5.csv" "$3/union-$2.csv"
}


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

:<<EOF
此处因文件太多容易造成inode内存占满的情况
如不存在该问题，并同时想保留过程文件
可以将以下内容的rm语句注释掉
EOF

gender=(male female)
chmod a+x *

for tumor in $@
do
  for gen in ${gender[@]}
	do
		./simulate.py $tumor $gen
		# output box-plot/gender/mid/tumor_type-gender/tcga_id/num(1-1000)/HLA-allele(random 6).csv
		echo "FINISH simulate.py $tumor-$gen"

		# ./union.sh $tumor $gen
		tumor_gender_folder="../../../box-plot/gender/mid/$tumor-$gen/"
		tumor_gender_out_dir="../../../box-plot/gender/extract/$tumor-$gen"
		for tumor_id in `ls $tumor_gender_folder`
		do
			mid_dir=${tumor_gender_folder}${tumor_id}"/"
			tumor_dir=${tumor_gender_out_dir}/${tumor_id}
			mkdir -pv $tumor_dir
			for k in {1..1000}
			do
				dest_dir=${mid_dir}$k
				union $dest_dir $k $tumor_dir
			done
			echo $tumor_id" finish!!!"
		done
		# output box-plot/gender/extract/tumor_type-gender/tcga_id/union-num(1-1000).csv
		echo "FINISH union.sh $tumor-$gen"

		# ./lines.sh $tumor $gen
		tumor_gender_folder="../../../box-plot/gender/extract/$tumor-$gen/"
		tumor_gender_out_dir="../../../box-plot/gender/qualified-lines/$tumor-$gen"
		for tumor_id in `ls $tumor_gender_folder`
		do
			dest_dir="${tumor_gender_folder}${tumor_id}"
			mkdir -pv ${tumor_gender_out_folder}
			tumor_out="${tumor_gender_out_folder}${tumor_id}.csv"
			count_lines $dest_dir $tumor_out
		done
		# output box-plot/gender/qualified-lines/tumor_type-gender/tcga_id.csv
		echo "FINISH lines.sh $tumor-$gen"

		echo "STARTING rm extract!!!"
		rm -rf ../../../box-plot/gender/extract
		echo "FINISH rm extract"

    echo "STARTING rm mid!!!"
    rm -rf ../../../box-plot/gender/mid
    echo "FINISH rm mid"
	done
done

./average.py "$@"
# output box-plot/gender/qualified-lines/tumor_type-gender.csv
echo "FINISH average.py for all"

./antigen.py "$@"
# output box-plot/gender/tumor_type-gender-patient.csv
echo "FINISH antigen.py for all"

./maybe.py "$@"
# output box-plot/gender/maybe-gender.csv
echo "FINISH maybe.py for all"

./box.py "$@"
# output box-plot/gender/box-gender.csv
echo "FINISH box.py $@"
echo "FINISH set-gender-box.sh $@"