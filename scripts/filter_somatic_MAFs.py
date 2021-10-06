#!/usr/bin/env python3

from glob import glob

for filename in glob("./data/raw/MAFs/*Maf.maf"):
	print(filename.replace("raw","processed").replace("Maf.maf",".filt_som.maf"))
	with open(filename.replace("raw","processed").replace("Maf.maf",".filt_som.maf"),"w") as fout:
		with open(filename,"r") as fin:
			for i,line in enumerate(fin):
				if line.startswith("#") or line.startswith("Hugo_Symbol"):
					fout.write(line)
				else:
					col=line.strip().split()
					if col[25] == "SOMATIC" and ("SBIASALT" or "MIUN" or "MIN" or "MR" or "HOM") not in col[34]:
						fout.write(line)

