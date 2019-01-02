#!/bin/bash

function hla_union()
{
	file_array=()
	let i=0
	for file in `ls $1`
	do
		file_array[i]=`basename $file`
		let i=$i+1
	done
	#echo ${file_array[1]}
	let len=$3
	tcga_file=()
	let i=0
	for item in ${file_array[@]}
	do
		dir="$1/$item/$2"
		for file in `ls $dir`
		do
			tcga_file[i]=`basename $file`
			let i=$i+1
			#echo ${tcga_file[i]}
		done
		#echo ${tcga_file[1]}
		for(( j=0; j<=$3; j++))
		do
			if [ $j -eq 0 ]
			then
				cat "$dir/${tcga_file[j]}" "$dir/${tcga_file[`expr $j + 1`]}" |sort|uniq > "$dir/tmp-`expr $j + 1`.csv"
			else
				cat "$dir/tmp-$j.csv" "$dir/${tcga_file[`expr $j + 1`]}" |sort|uniq > "$dir/tmp-`expr $j + 1`.csv"
			fi
		done

		for (( k=1; k<=$3; k++))
		do
			rm "$dir/tmp-$k.csv"
		done
		mkdir -pv "../../../bar-plot/gender/hla-union/$item/"
		mv "$dir/tmp-`expr $3 + 1`.csv" "../../../bar-plot/gender/hla-union/$item/$2.csv"
	done
}

folder="../../../bar-plot/gender/hla/"
type_=$1
len=$2
hla_union $folder $type_ $len