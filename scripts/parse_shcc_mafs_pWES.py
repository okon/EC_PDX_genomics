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
for filename in glob("/working/lab_nicw/olgaK/Pollock_endometrial_PDX_manuscript/data/raw/MAFs/pWES/som/*shcc.maf.gz"):
	out_maf = filename.replace('raw/MAFs/pWES/som','processed/MAFs/pWES_BROCA_som').replace('.maf.gz','.BROCA.maf.gz')
	out_vcf = filename.replace('raw/MAFs/pWES/som','processed/MAFs/pWES_BROCA_som').replace('.maf.gz','.BROCA.vcf')
	
	if not count % 10:
		print(f"Processing {count}th file")
	with gzip.open(out_maf,"wt") as fout:
		with open(out_vcf,"w") as fout2:
			fout2.write("##fileformat=VCFv4.1\n")
			fout2.write("##contig=<ID=1,length=249250621,assembly=b37>\n")
			fout2.write("##reference=file:///path/to/human_g1k_v37.fasta\n")
			fout2.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n")	
			with gzip.open(filename,"rt") as fin:
				for i,line in enumerate(fin):
					if line.startswith("#") or line.startswith("Hugo_Symbol"):
						fout.write(line)
						continue
					else:
						col=line.strip().split()
						gene=col[0]
						chrom=col[4]
						pos=col[5]
						ref=col[10]
						if col[11]==ref:
							alt=col[12]
						else:
							alt=col[11]
						if col[13].startswith("rs"):
							rs_id=col[13]
						else:
							rs_id="."
						if gene in BROCA_genes:
							geneset.add(gene)						
							fout.write(line)
							fout2.write("\t".join([chrom,pos,rs_id,ref,alt,".",".",".\n"]))
	count+=1
print(geneset)
