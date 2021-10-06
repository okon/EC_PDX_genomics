for vcf in /working/genomeinfo/share/analysis/Pollock_-_Endometrial_cancer_MAPQ60/cromwell/VCFs/all_sp/*sp.vcf.gz; do
	qsub -v input=$vcf /working/lab_nicw/olgaK/Pollock_endometrial_PDX_manuscript/scripts/subset_variants.pbs
done
