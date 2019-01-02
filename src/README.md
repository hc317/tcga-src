1. ./gdc_scan.py files download --format MAF --project TCGA-XXXX

2. ./gdc_scan.py files download --project TCGA-XXXX --type "Clinical Supplement"

3. gzip -d *mutect*

4. rm -rf *.gz

5. mv `ls` mutect.maf

6. sed -i '1,5d' mutect.maf

7. ./get_rid_chr.py

8. ./get_id.py

9. ./extract.py

10. ./2vcf.sh

11. ./vep.sh

12. ./cut.py

13. ./filter.sh

14. ./fasta.sh

15. ./pep.sh

16. ./pre.sh

17. ./get_real_pep.py

18. ./ic50.py
