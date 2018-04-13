#!/usr/bin/bash
# files needed from Galaxy: 
# Galaxy3-[pBR322.fna].fasta
# Galaxy17-[Sequence_Content_Trimmer_on_data_13_and_data_12].fasta -> Galaxy20-[Sequence_Content_Trimmer_on_data_15_and_data_14].fasta
# Galaxy29-[SAM-to-BAM_on_data_3_and_data_28__converted_BAM].bam -> Galaxy43-[SAM-to-BAM_on_data_3_and_data_41__converted_BAM].bam
# Galaxy29-[SAM-to-BAM_on_data_3_and_data_28__converted_BAM].bai -> Galaxy43-[SAM-to-BAM_on_data_3_and_data_41__converted_BAM].bai
# Galaxy34-[Filter_on_data_33].tabular -> Galaxy53-[Filter_on_data_51].tabular
# 

#get family size table 
awk 'BEGIN {OFS="\t"} />/ {print substr($1, 2, 27), $2}' Galaxy20-[Sequence_Content_Trimmer_on_data_15_and_data_14].fasta > familySizeTable.txt

#get mate alignments     
samtools view -F 2060 -b Galaxy43-[SAM-to-BAM_on_data_3_and_data_41__converted_BAM].bam | samtools fillmd -e - Galaxy3-[pBR322.fna].fasta | grep -v "^@" > mate_aligned.txt 

python mateLinkCall_0828.py 

awk 'BEGIN{while(getline<"Galaxy53-[Filter_on_data_51].tabular"){t=$3;sz[t]=$16;sz2[t]=$17}} {split($1,a,"_");split(a[1],b,"-");split(a[2],c,"-");  print $1"\t"sz[b[1]]"\t"sz[c[1]]"\t"sz2[b[1]]"\t"sz2[c[1]]"\t"$2}' linkage_mates.txt > linkage_mates_MAF.txt

awk 'BEGIN{FS="\t";OFS="\t";while(getline<"familySizeTable.txt"){t=$1;$1="";sz[t]=$0;gsub(/^[ \t]+/,"",sz[t])}} {print $0"\t"sz[$6]}' linkage_mates_MAF.txt > linkage_mates_MAF_famSize.txt

#awk 'BEGIN{FS="\t"}{if ($4 && $5 && $4 <= 1 && $5 <= 1) print $0}' linkage_mates_MAF_famSize.txt > linkage_mates_MAF_Bias_Filtered.txt

rm familySizeTable.txt mate_aligned.txt linkage_mates.txt linkage_mates_MAF.txt 