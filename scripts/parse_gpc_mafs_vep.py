#!/usr/bin/env python3

from glob import glob
import gzip

def parse_maf(filename,fout,geneset,header=False):
	BROCA_genes=["ATM", "ATR", "BARD1", "BRCA1", "BRCA2", "BRIP1", "CHEK1",
	"CHEK2", "MRE11A","MRE11", "NBN", "PALB2", "RAD51C", "RAD51D", "CDK12", 
	"FANCA", "FANCB", "FANCC", "FANCD2", "FANCE", "FANCF", "FANCG", 
	"FANCI", "FANCL", "FANCM", "RAD50", "RAD51","BRCC5", "RAD51B", 
	"ARID1A", "PTEN"]
	with gzip.open(filename,"rt") as fin:	
		for i,line in enumerate(fin):
			if line.startswith("#") or line.startswith("Hugo_Symbol"):
			        continue
			#elif line.startswith("Hugo_Symbol") and header:
			#	fout.write("chromosome\tstart\tend\tallele\tstrand\tidenfier\n")
			#elif line.startswith("Hugo_Symbol") and not header:
			#	continue
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
					if ref == "-":
						fout.write("\t".join([chrom,epos,spos,allele,strand]))
					else:
						fout.write("\t".join([chrom,spos,epos,allele,strand]))
					fout.write("\n")
	return(geneset)

count=1
geneset=set()
for filename in glob("/working/lab_nicw/olgaK/Pollock_endometrial_PDX_manuscript/data/raw/MAFs/*gpc.maf.gz"):
	out_vep = filename.replace('raw/MAFs','processed/MAFs/BROCA').replace('.maf.gz','.BROCA.input_vep.tsv')
	if not count % 10:
		print(f"Processing {count}th file")
	with open(out_vep,"wt") as fout:
		geneset = parse_maf(filename,fout,geneset,header=True)
	count+=1
print(count)
print(geneset)
