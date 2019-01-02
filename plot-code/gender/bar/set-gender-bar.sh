#!/bin/bash
# Sun Nov 25 2018

# STARTING: plot-code/gender/bar/set-gender-bar.sh
# USAGE: ./set-gender-bar.sh type1(xxxx.lower()) type2 type3 type4

:<<EOF
首先你需要创建一个文件夹，内容包含：
plot-code/
TCGA-IC50/
然后开始执行！
或许还需要额外的一步，给set-gender-bar.sh文件加上执行权限：
chmod a+x set-gender-bar.sh
EOF

gender=(male female)

chmod a+x *

./rename_xml.py "$@"
# output TCGA-IC50/TCGA-tumor_type/tumor_type-all-clinical-files/tcga_id.xml
echo "FINISH rename_xml.py $@"

./split_gender.py "$@"
# output bar-plot/gender/tumor_type-gender-id.cs
echo "FINISH split_gender.py $@"

./hla.py "$@"
# output bar-plot/gender/hla/HLA-allele/tumor_type/tcga_id.csv
echo "FINISH hla.py $@"

# ./hla-union.sh
:<<EOF
首先读取传入的tumor_type参数
然后将每个tumor_type与两个gender搭配
最后依次处理
EOF

let i=0
for tumor in $@
do
	for gen in ${gender[@]}
	do
		tumor_gender[i]="$tumor-$gen"
		let i=i+1
	done
done

for tg in ${tumor_gender[@]}
do
	./hla-union.sh $tg `./tcga_id_num.py $tg`
done

# output bar-plot/gender/hla-union/HLA-allele/tumor_type-gender.csv
echo "FINISH hla-union.sh ${tumor_gender[@]}"

./trans.py "$@"
# output bar-plot/gender/trans/tumor_type-gender/HLA-allele.csv
echo "FINISH trans.py $@"

./count.py "$@"
# output bar-plot/gender/lines/tumor_type-gender.csv
echo "FINISH count.py $@"

./get_frequency.py "$@"
# output bar-plot/gender/frequency-lines/tumor_type-gender.csv
echo "FINISH get_frequency.py $@"

echo "STARTING rm directory!!!"
# 如果希望保留过程文件，就将下面的rm语句注释掉
rm -rf ../../../bar-plot/gender/hla/
rm -rf ../../../bar-plot/gender/hla-union/
rm -rf ../../../bar-plot/gender/trans/
rm -rf ../../../bar-plot/gender/lines/
echo "FINISH rm directory"
cd ../../../bar-plot/gender/frequency-lines/

chmod 777 *
# 该步骤后需要手动操作，对WPS-Excle打开frequency-lines中的文件进行降序排序
echo "modify files in frequency-lines and then run set-bar-more.sh!!!"
:<<EOF
然后手动使用WPS-EXCEL表格对数据进行降序的排序
接下来手动运行 bar.py 和 hla_frequency.py
./bar.py type1(xxxx.lower()) type2 type3 type4
./hla_frequency.py type1(xxxx.lower()) type2 type3 type4
./joint.py type1(xxxx.lower()) type2 type3 type4
或者运行 set-gender-bar-more.sh
./set-gender-bar-more.sh type1 type2 type3 type4
EOF