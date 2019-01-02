#!/bin/bash
# Fri Nov 23 2018

# STARTING: plot-code/bar/set-bar.sh
# USAGE: ./set-bar.sh type1(xxxx.lower()) type2 type3 type4

:<<EOF
首先你需要创建一个文件夹，内容包含：
plot-code/
TCGA-IC50/
然后开始执行！
或许还需要额外的一步，给set-bar.sh文件加上执行权限：
chmod a+x set-bar.sh
EOF

chmod a+x *

./get_tcga_id.py "$@"
# output bar-plot/tumor_type/xxxx-new-id.csv
echo "FINISH get_tcga_id.py $tumor"

./hla.py "$@"
# output bar-plot/hla/HLA-allele/tumor_type/tcga_id.csv
echo "FINISH hla.py $tumor"

for tumor in $@
do
	# ./hla-union.sh
	./hla-union.sh $tumor `./tcga_id_num.py $tumor`

	# output bar-plot/hla-union/HLA-allele/tumor_type.csv
	echo "FINISH hla-union.sh $tumor"
done

./trans.py "$@"
# output bar-plot/trans/tumor_type/HLA-allele.csv
echo "FINISH trans.py $tumor"

./count.py "$@"
# output bar-plot/lines/tumor_type.csv
echo "FINISH count.py $tumor"

./get_frequency.py "$@"
# output bar-plot/frequency-lines/tumor_type.csv
echo "FINISH get_frequency.py $tumor"

echo "STARTING rm directory!!!"
# 如果希望保留过程文件，就将下面的rm语句注释掉
#rm -rf ../../bar-plot/hla/
#rm -rf ../../bar-plot/hla-union/
#rm -rf ../../bar-plot/trans/
#rm -rf ../../bar-plot/lines/
echo "FINISH rm directory"
cd ../../bar-plot/frequency-lines/

chmod 777 *
# 该步骤后需要手动操作，对WPS-Excle打开frequency-lines中的文件进行降序排序
echo "modify files in frequency-lines and then run set-bar-more.sh!!!"

:<<EOF
然后手动使用WPS-EXCEL表格对数据进行降序的排序
接下来手动运行 bar.py 和 hla_frequency.py
./bar.py type1(xxxx.lower()) type2 type3 type4
./hla_frequency.py type1(xxxx.lower()) type2 type3 type4
./joint.py type1(xxxx.lower()) type2 type3 type4
或者运行 set-bar-more.sh
./set-bar-more.sh type1 type2 type3 type4
EOF