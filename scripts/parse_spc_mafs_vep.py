#!/usr/bin/env python3

from glob import glob
import gzip

BROCA_genes=["ATM", "ATR", "BARD1", "BRCA1", "BRCA2", "BRIP1", "CHEK1",
"CHEK2", "MRE11A","MRE11", "NBN", "PALB2", "RAD51C", "RAD51D", "CDK12", 
"FANCA", "FANCB", "FANCC", "FANCD2", "FANCE", "FANCF", "FANCG", 
"FANCI", "FANCL", "FANCM", "RAD50", "RAD51","BRCC5", "RAD51B", 
"ARID1A", "PTEN"]

count=1
geneset=set()
for filename in glob("/working/lab_nicw/olgaK/Pollock_endometrial_PDX_manuscript/data/raw/MAFs/*spc.maf.gz"):
	out_vep = filename.replace('raw/MAFs','processed/MAFs/BROCA').replace('.maf.gz','.BROCA.vep.tsv')
	
	if not count % 10:
		print(f"Processing {count}th file")
	with open(out_vep,"wt") as fout:
		with gzip.open(filename,"rt") as fin:
			for i,line in enumerate(fin):
				if line.startswith("#"):
					continue
				if line.startswith("Hugo_Symbol"):
					fout.write("chromosome\tstart\tend\tallele\tstrand\tidenfier\n")
					continue
				else:
					col=line.strip().split()
					gene=col[0]
					chrom=col[4]
					spos=col[5]
					epos=col[6]
					strand=col[7]
					ref=col[10]
					if col[11]==ref:
						alt=col[12]
					else:
						alt=col[11]
					allele=ref + "/" + alt
					if gene in BROCA_genes:
						geneset.add(gene)						
						fout.write("\t".join([chrom,spos,epos,ref,allele,strand]))
						fout.write("\n")
	count+=1
print(geneset)
